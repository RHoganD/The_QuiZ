class Question:
    """
    Questions class that gets the question
    and the answer
    """
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


easy_question = [

"What's the biggest animal in the world\n a) Elefant\n b) Giraffe\n c) The blue whale\n d) Mouse\n\n",
"What is the largest country in the world?\n a) Russia\n b) The UK\n c) Germany\n d) Africa\n\n",
"What is the most sold flavour of Walker's crisps?\n a) Cheese\n b) Cheese and Onion\n c) Sea salt\n d) None of the avobe\n\n",
"What is the capital of spain?\n a) Berlin\n b) London\n c) Paris\n d) Madrid\n\n",
"What was Queen Elizabeth II's surname?\n a) Windsor\n b) Smith\n c) Dunbar\n d) Scott\n\n",
"What's a baby rabbit called?\n a) Sheep\n b) A kit\n c) A Kid\n d) Cow\n\n",
"Who painted the Mona Lisa?\n a) Lionard de Vincy\n b) Issac Newton\n c) Boris Johnson\n d) Leonardo da Vinci\n\n",
"How many minutes in a game of rugby league\n a) 80 minutes\n b) 90 minutes\n c) 60 minutes\n d) 85 minutes\n\n",
"What month was Prince George born?\n a) January\n b) July\n c) August\n d) March\n\n",
"Where was the mojito cocktail created?\n a) Mexico\n b) Cuba\n c) Santo Domingo\n d) Colombia\n\n"

]

easy_question_answer = [
    Question(easy_question[0], "c"),
    Question(easy_question[1], "a"),
    Question(easy_question[2], "b"),
    Question(easy_question[3], "d"),
    Question(easy_question[4], "a"),
    Question(easy_question[5], "b"),
    Question(easy_question[6], "d"),
    Question(easy_question[7], "a"),
    Question(easy_question[8], "b"),
    Question(easy_question[9], "b")
]


medium_questions = [

"Which supermodel was born in Streatham, London?\n a) Bella Hadid\n b) Kate moss\n c) Naomi Campbell\n d) Cindy Crawford\n\n",
"How many sides does a heptadecagon have?\n a) 17\n b) 20\n c) 10\n d) 6\n\n",
"What grain is the Japanese spirit Sake made from?\n a) Wheat\n b) Rice\n c) Oatmeal\n d) Quinoa\n\n",
"What star sign would someone born on August 24th be?\n a) Libra\n b) Leo\n c) Sagitario\n d) virgo\n\n",
"What is the smallest country in the world?\n a) creece\n b) Vatican City\n c) Venice\n d) Vatican\n\n",
"When was the first iPhone released?\n a) 2006\n b) 2005\n c) 2008\n d) 2007\n\n",
"What is the capital city of Brazil?\n a) Brasília\n b) Distrito Federal\n c) São Paulo\n d) Rio de Janeiro\n\n",
"Which one of these is a fish\n a) Whale\n b) Shark\n c) Dolphin\n d) Shellfish\n\n",
"Which planet is closest to the sun\n a) Mercury\n b) Earth\n c) Mars\n d) Venus\n\n",
"To a single decimal point, many kilometers in a mile\n a) 1.2km\n b) 1.4km\n c) 1.5km\n d) 1.6km\n\n"
]


medium_questions_answer = [

    Question(medium_questions[0], "c"),
    Question(medium_questions[1], "a"),
    Question(medium_questions[2], "b"),
    Question(medium_questions[3], "d"),
    Question(medium_questions[4], "b"),
    Question(medium_questions[5], "d"),
    Question(medium_questions[6], "a"),
    Question(medium_questions[7], "b"),
    Question(medium_questions[8], "a"),
    Question(medium_questions[9], "d"),
]


hard_questions = [

"What are Canada's two national sports?\n a) Lacrosse & Ice Hockey\n b) Hockey & ski jumping\n c) Ice Hockey & Basket ball\n d) Running & ski jumping\n\n",
"Which one is a landlocked country in Europe\n a) Andorra\n b) Austria\n c) Hungary\n d) All of the above\n\n",
"Who has been the First Minister of Wales since December 2018?\n a) Carwyn Jones\n b) Alun Michael\n c) Mark Drakeford\n d) Rhodri Morgan\n\n",
"Typically, what's the strongest muscle in the human body?\n a) Gluteus maximus\n b) The masseter\n c) The Stapedius\n d) None of the above\n\n",
"How many valves does the heart have?\n a) 6\n b) 5\n c) 3\n d) 4\n\n",
"Who plays Delboy Trotter in Only Fools And Horses?\n a) Nicholas Lyndhurst\n b) Buster Merryfield\n c) David Jason\n d) Lennard Pearce\n\n",
"What is the capital of Iceland?\n a) Reykjavík\n b) Kópavogur\n c) Akureyr\n d) Reykjanesbær-Keflavík\n\n",
"What is the name of Bridget Jones' baby in the third Bridget Jones film?\n a) William\n b) Jonas\n c) Gabriel\n d) Scott\n\n",
"How many times has Andy Murray won Wimbledon playing singles?\n a) 2\n b) 3\n c) 4\n d) 1\n\n",
"Which book begins with the line, Last night I dreamt I went to Manderley again…?\n a) The Scapegoat by Daphne Du Maurier\n b) Rebecca by Daphne Du Maurier\n c) The King's General by Daphne Du Maurier\n d) Mary Anne by Daphne Du Maurier\n\n"

]

hard_questions_answer = [

     Question(hard_questions[0], "a"),
     Question(hard_questions[1], "d"),
     Question(hard_questions[2], "c"),
     Question(hard_questions[3], "b"),
     Question(hard_questions[4], "d"),
     Question(hard_questions[5], "c"),
     Question(hard_questions[6], "a"),
     Question(hard_questions[7], "a"),
     Question(hard_questions[8], "c"),
     Question(hard_questions[9], "b"),

]