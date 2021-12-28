"""
Unit tests for the trivia library

Maily used to test if the API's are still active
"""
import _correct_path
from src.cogs.trivia import TriviaCog, TriviaQuestion


class TestTrivia:
    def test_api_availability(self):
        """
        Test if the trivia API is online
        """
        self.trivia_cog = TriviaCog("not_a_bot")
        question = self.trivia_cog._get_question()
        assert type(question) == TriviaQuestion
