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
            Tscore = score
            print("Wrong answer!! You lost 10 points\n")

        if question == easy_question_answer:
            score += 10
            question = "Easy"
        if question == medium_questions_answer:
            score += 20
            question = "Medium"
            
        if question == hard_questions_answer:
            score += 30
            question = "Hard"
            print("\n")
    print("Great!! You got  " + str(correct) + "  Correct / out of  " + str(len(questions)) + "  questions")
    print("Total score:  " + str(Tscore)) 

    play = input("Do want to play again?\n")
    if play != "yes":
        print("Sorry you are leaving, lets play another time")
        quit()
    else:
        print("Okay! Let's Play Again! :) \n")

    main_menu()


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

start()
  
def main_menu():
    """
    Shows the option to choose question dificulties
    """
    print( "Please select Quiz Level\n\n   ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Leaderboard")
    print("0. Quit")
    question = input("Enter 1, 2, 3, 4 or 0: ")

    if question == "1":
        print("Loanding Easy question......")
       
        run_quiz(easy_question_answer)

    if question == "2":
        print("Loanding Medium question......")
        
        run_quiz(medium_questions_answer)

    if question == "3":
        print("Loanding Hard question......")

        run_quiz(hard_questions_answer)

    if question == "4":
        show_leaderboard()

    if question == "0":
        print("Thanks for playing!")
        quit()

main_menu()
run_quiz()








