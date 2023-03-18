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

# from string import ascii_lowercase


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
            incorrect += 1
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
    print(f'(Great!! {name} Your got  {correct} Correct / out of   {len(questions)}  questions)')
    print(f'(Total score:  {score}  answering {correct} and {incorrect} Incorrect)')
        

start()


def start():
    """
    Shows the start of the quiz and greetings
    """
    slogan = pyfiglet.figlet_format("The Quiz", font = "slant" )
    print(slogan)

    name = input("Enter your name: \n")
    
    print("\n")
    print("Hello", name, "Welcome to the quiz\n")
    playing = input("Do you want to play the quiz? ")

    if playing != "yes":
        print("Sorry you are leaving, lets play another time")
        quit()
    else:
        print("Okay! Let's Play! :) \n")
        run_quiz()
  
menu()

def menu(questions):
    """
    Shows the option to choose question dificulties
    """
    print(  "Please select Quiz Level\n\n   ")
    print("1. Easy")
    Print("2. Medium")
    Print("3. Hard")
    Print("4. Leaderboard")
    Print("0. Quit")
    levels = input("Enter 1, 2, 3, 4 or 0: ")

    if levels == "1.":
        print("Loanding Easy question......")
        clear()
        start_quiz(easy_question_answer)

    if levels == "2":
        print("Loanding Medium question......")
        clear()
        start_quiz(medium_questions_answer)

    if levels == "3":
        print("Loanding Hard question......")
        clear()
        start_quiz(hard_questions_answer)

    if levels == "4":
        show_leaderboard()

    if levels == "0":
        print("Thanks for playing!")
        quit()

start_quiz()









