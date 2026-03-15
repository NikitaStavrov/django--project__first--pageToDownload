import os
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):
    
    if request.method == "POST":
        text = request.POST.get("query")
        if not text:
            return HttpResponse("Error: No query was provided.", status=400)
        
        try:
            api_key = os.getenv("SERPAPI_KEY")
            if not api_key:
                return HttpResponse("Error: SERPAPI_KEY not found in .env file.", status=500)
            
            url = "https://serpapi.com/search"
            params = {
                "engine": "google",
                "q": text,
                "api_key": api_key,
                "num": 10,
            }
            
            api_response = requests.get(url, params=params, timeout=15)
            api_response.raise_for_status()
            
            results = api_response.json()
            
            organic_results = results.get("organic_results", [])
            
            if not organic_results:
                return HttpResponse("Nothing was found.", status=404)
            
            first_result = organic_results[0]
            
            json_data = json.dumps(first_result, indent=4, ensure_ascii=False)
            
            response = HttpResponse(json_data, content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="first_result_{text}.json"'
            
            return response

        except requests.RequestException as e:
            return HttpResponse(f"Error with API request: {str(e)}", status=500)
        except Exception as e:
            return HttpResponse(f"Noone knows which Error occurred: {str(e)}", status=500)
    # end of if, which is for POST method
    
    return render(request, "index.html")