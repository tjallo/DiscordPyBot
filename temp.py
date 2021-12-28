from requests import get
from json import loads

from src.cogs.trivia import TriviaCog, TriviaQuestion

tg = TriviaCog("asdf")

print(tg._get_question("asdf"))