# Your code goes here.
import gspread

from google.oauth2.service_account import Credentials
from Question import Question
from Question import easy_question_answer
from Question import medium_questions_answer
from Question import hard_questions_answer

import pyfiglet
from pyfiglet import figlet_format
import random
from string import ascii_lowercase


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

GC = gspread.service_account("creds.json")
sh = GC.open("The_Quiz")
wk = sh.sheet1
leaderboard = sh.worksheet('leaderboard')

# print((leaderboard).get_all_values())


def run_quiz(questions):
    """
    Process the quiz
    """
    score = 0
    correct = 0
    incorrect = 0

    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            correct += 1
            print("⭐ Correct! ⭐ You got 10 point\n")
        else:
            score = -10
            print("Wrong answer!! You lost 10 points\n")

        if question == easy_question_answer:
            question = "Easy"
            score += 10
        if question == medium_questions_answer:
            question = "Medium"
            score += 20
        if question == hard_questions_answer:
            question = "Hard"
            score += 30
    print("Great!!", name,  "Your got " + int(score) + " Correct / out of " + str(len(questions)),  "questions\n")
    print("Total score: " + str(score) + "  answering" + (correct) + (incorrect))
        

run_quiz(easy_question_answer)



