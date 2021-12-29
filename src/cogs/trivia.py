from typing import List
from discord.ext import commands
from requests import get
from json import loads
from random import shuffle
from html import unescape
from discord import Member


class TriviaQuestion:
    def __init__(
        self,
        category: str,
        type: str,
        difficulty: str,
        question: str,
        correct_answer: str,
        inccorect_answers: List[str],
    ) -> None:
        self.category = category
        self.type = type
        self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = list(inccorect_answers)
        self.all_answers = self._shuffle_answers(
            self.correct_answer, self.incorrect_answers
        )

    def check_answer(self, index):
        """
        Checks if the given index (0 through 3) contains the right answer.
        """
        return self.all_answers[index] == self.correct_answer

    def _shuffle_answers(self, correct_ans, inccorect_ans):
        all_ans = inccorect_ans.copy()
        all_ans.append(correct_ans)

        shuffle(all_ans)

        return all_ans

    def __str__(self) -> str:
        return f"TriviaQuestion({self.category=}\n{self.type=}\n{self.difficulty=}\n{self.question=}\n{self.correct_answer=}\n{self.incorrect_answers=}\n{self.all_answers=}\n)"


class TriviaCog(commands.Cog, name="Trivia"):
    def __init__(self, bot) -> None:
        self.bot = bot
        self.SESSION_TOKEN = self._get_session_token()
        self.categories = self._get_categories()
        self.possible_categories = [int(x.split(":")[0]) for x in self.categories]

    def _get_session_token(self) -> str:
        return loads(get("https://opentdb.com/api_token.php?command=request").text)[
            "token"
        ]

    def _get_categories(self) -> List[str]:
        try:
            res = loads(get("https://opentdb.com/api_category.php").text)[
                "trivia_categories"
            ]
            result = [f"{x['id']}: {x['name']}" for x in res]
            return result
        except:
            return None

    def _get_question(self, category_id: int = None) -> TriviaQuestion:
        url = "https://opentdb.com/api.php?amount=1&type=multiple"
        if category_id != None and str(category_id).isnumeric():
            url = f"https://opentdb.com/api.php?amount=1&category={category_id}&type=multiple"

        try:
            res = loads(get(url).text)["results"][0]
            category = unescape(res["category"])
            q_type = unescape(res["type"])
            difficulty = unescape(res["difficulty"])
            question = unescape(res["question"])
            correct_answer = unescape(res["correct_answer"])
            incorrect_answers = [unescape(x) for x in res["incorrect_answers"]]
            category = unescape(res["category"])
            question_obj = TriviaQuestion(
                category,
                q_type,
                difficulty,
                question,
                correct_answer,
                incorrect_answers,
            )

            return question_obj
        except Exception as e:
            print(e)
            return None

    @commands.command(name="questionCategories")
    async def question_categories(self, ctx, *, member: Member = None):
        member = member or ctx.author

        message = "\n".join(self.categories)

        await ctx.send(message)

    @commands.command(name="question")
    async def question(self, ctx, arg=None, member: Member = None):
        """- Gives a trivia question can be used with the questionCategory command e.g. !question 10 will give you a question of the 10th category"""
        member = member or ctx.author

        try:
            q_index = int(arg)
        except Exception:
            q_index = False

        if q_index and q_index in self.possible_categories:
            question: TriviaQuestion = self._get_question(q_index)
        else:
            question: TriviaQuestion = self._get_question()

        qst_msg = f"""*Category: {question.category}*
**{question.question}**
\t1: {question.all_answers[0]}
\t2: {question.all_answers[1]}
\t3: {question.all_answers[2]}
\t4: {question.all_answers[3]}
        """

        msg = await ctx.send(qst_msg)

        # Unicode codepoints for 1 through 4 with cap enclosing codepoint (To Make 1 through 4 keycap emojis)
        emojis = ["\u0031\u20E3", "\u0032\u20E3", "\u0033\u20E3", "\u0034\u20E3"]

        for emoji in emojis:
            await msg.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in emojis

        reaction, user = await self.bot.wait_for(
            "reaction_add", timeout=10.0, check=check
        )

        user: Member = user

        reaction = str(reaction)

        if reaction in emojis:

            index = emojis.index(reaction)

            ans_correct = question.check_answer(index)

            m = ""

            if ans_correct:
                m = f"**{question.correct_answer}** was indeed the correct answer! Well done {user.mention}."
            else:
                m = f"*{question.all_answers[index]}* was the incorrect answer, the correct answer was **{question.correct_answer}**. Better luck next time {user.mention}."

            return await ctx.send(m)

        # If the answer is to late.
        await ctx.send("Cancceld trivia, answer was to late")
