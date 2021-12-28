"""
Unit tests for the trivia library

Maily used to test if the API's are still active
"""
import _correct_path
from requests import get    


class TestTrivia:
    def test_api_availability(self):
        """
        Test if the Reddit API is online
        """
        req = get("https://www.reddit.com/r/ik_ihe.json")
        assert req.status_code == 429 or req.status_code == 200
        
    def test_basic_functionality(self):
        """
        Test Basic Python functionality
        """
        assert True