# Your code goes here.
import gspread
from google.oauth2.service_account import Credentials
import click
import time
from Question import easy_question_answer
from Question import medium_questions_answer
from Question import hard_questions_answer
import pyfiglet
from pyfiglet import figlet_format
import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("The_Quiz")
worksheet = SHEET.worksheet("leaderboard")
leaderboard = worksheet

def run_quiz(questions):
    """
    Process the quiz
    """
    score = 0
    correct = 0
    incorrect = 0
    count = 0
    questions = random.sample(questions, 6)
    for question in questions:
        while True:
            answer = input(question.question)     
            if answer not in {'a', 'b', 'c', 'd'}:
                print("invalid character. Type: a/b/c/d. Please try again!")
            else:
                break
        if answer == question.answer:
            correct += 1
            score = score + 10
            print(Fore.GREEN + "⭐ Correct! ⭐ You got 10 points\U0001F601\n")
            print('\033[39m')
            if answer == easy_question_answer:
                question = "Easy"
            elif answer == medium_questions_answer:
                question = "Medium"
            elif answer == hard_questions_answer:
                question = "Hard"
        else:
            incorrect -= 10
            count += 1
            print(Fore.RED + "Wrong answer!! \U0001F610 You lost 10 points\n")
            print('\033[39m')
        flag2 = input("Do you want to quit the quiz (Yes/No)\n")
        if flag2 == "yes":
            break
    print("Good Job!! You got " + str(correct) + " Correct / " + str(count) + " incorrect out of "
                                                            + str(len(questions)) + " questions")
    print("Total score: " , score)
    print("updating leadearboard .....")
    time.sleep(2)
    update_sheet([player_name], score, 'leaderboard')
    print("\n")
    play = input("Do want to play again?\U0001F914\n")
    if play != "yes":
        print("Sorry you are leaving, lets play another time")
        bye = pyfiglet.figlet_format("Thank you", font = "slant")
        print(bye)
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
    player_name = input("Enter your name: \n")   
    print("\n")
    print("Hello", player_name, "Welcome to the quiz\n")
    playing = input("Do you want to play the quiz? (Yes/No)")
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
    print("\n")
    if question == "1":
        print("\n")
        print("Loanding Easy question......\n")
        time.sleep(2.4)
        clrscr()
        run_quiz(easy_question_answer)
    if question == "2":
        print("\n")
        print("Loanding Medium question......\n")
        time.sleep(2.4)
        clrscr()
        run_quiz(medium_questions_answer)
    if question == "3":
        print("\n")
        print("Loanding Hard question......")
        time.sleep(2.4)
        clrscr()
        run_quiz(hard_questions_answer)
    if question == "4":
        print(worksheet)
    if question == "0":
        print("Thanks for playing!")
        quit()

def clrscr():
    """
    Clear screen using click.clear() function
   """
    click.clear()

def update_sheet(player_name, score, worksheet):
    """"
    Function to update the leaderboard Google Sheet
    """
    add_data = SHEET.worksheet(worksheet)
    add_data.append_row([player_name, score])
    score = score
    player_name = player_name
    rank = leaderboard.get_all_values()
    

main_menu()
leaderboard()
run_quiz()