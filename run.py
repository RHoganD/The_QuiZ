# Your code goes here.
import gspread
import datetime
from pprint import pprint
from google.oauth2.service_account import Credentials
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
Id = '1al-0Vmf0cv4TWsfcdGuRpcmH_ZIX0MkhjB-pWWIubB0'




def run_quiz(questions):
    """
    Process the quiz
    """
    name = ''
    score = 0
    correct = 0
    incorrect = 0
    count = 0
    questions = random.sample(questions, 6)
    for question in questions:
        answer = input(question.question)
        if answer == question.answer:
            correct += 1
            print("⭐ Correct! ⭐ You got 10 points\U0001F601\n")
            if answer == easy_question_answer:
                score = score+10
                question = "Easy"
            elif answer == medium_questions_answer:
                score = score+20
                question = "Medium"  
            elif answer == hard_questions_answer:
                score = score+30
                question = "Hard"
        else:
            incorrect -= 10
            count += 1
            score = score * correct
            print("Wrong answer!! \U0001F610 You lost 10 points\n")
    print("\n")
    print("Great!! You got " + str(correct) + " Correct & " + str(count) + " Incorrect/out of " + str(len(questions)) + " questions")
    print("Total score:  " + str((score - incorrect) * correct))
    # leaderboard.append_rows(values=['A5:D5', name, score, correct, count])
    # leaderboard.append_rows(range('A5:D5'))
    # leaderboard.sort((5, 'asc'))
    # request = sheet.values().update(spreadsheetId=Id,
    #                        range="sheet6!A5", valueInputOption="row", body={"values":leaderboard}).execute()
    # print('Leaderboard updated successfully!\n')
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
        print((leaderboard).get_all_values())

    if question == "0":
        print("Thanks for playing!")
        quit()


def leaderboard():
    """
    update leaderboard spreadsheet and and new row with the user score
    """
  
    rank = leaderboard.get_all_values()
    board = sh.worksheet("leaderboard")
    leaderboard = [[name], [score], [correct], [count]]
    # leaderboard.sort((5, 'asc'))
    # leaderboard.append_rows(values)(values=['A5:D5', name, score, correct, count])
    # leaderboard.append_rows(range('A5:D5'))
    print("leaderboard updated successfully.\n")
    

# def get_leaderboard_values():
#     """
#     Collects data from leaderboard collumns worksheet, collecting
#     the last 5 entries and returns the data.
#     """
#     print((leaderboard).get_all_values())
#     Name =  name
#     Ranks = leaderboard.col_values('A5')
#     Score = leaderboard.col_values('C5')                  
    
#     for ind in range('A6:C6'):
#         rank = leaderboard.col_values(ind)
#         rank.append(rank[-5:])
      
#     return rank




main_menu()
leaderboard()
run_quiz()








