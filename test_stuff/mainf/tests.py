from unittest.mock import patch, Mock
from django.test import TestCase, Client
import os

class IndexViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        os.environ["SERPAPI_KEY"] = "fake-key"

    @patch("mainf.views.requests.get")
    def test_index_post_returns_first_result_json(self, mock_get):
        fake_response = Mock()
        fake_response.raise_for_status.return_value = None
        fake_response.json.return_value = {
            "organic_results": [
                {"title": "Example", "link": "https://example.com"}
            ]
        }
        mock_get.return_value = fake_response

        response = self.client.post("/", {"query": "test"})

        assert response.status_code == 200
        assert response["Content-Type"] == "application/json"
        assert 'attachment; filename="first_result_test.json"' in response["Content-Disposition"]
        assert b'"title": "Example"' in response.content

    def test_index_post_missing_query_returns_400(self):
        response = self.client.post("/", {"query": ""})
        assert response.status_code == 400
        assert b"No query was provided" in response.content
