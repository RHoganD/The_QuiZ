# The Quiz

![Responsive screenshot](/asset/images/Readme-Images/Responsive-image.png)

# Description 
The objective of this project have a quiz, where the user can test their general knowlage. This quiz the user the option to choose between Easy, Medium or Hard question. the final result or score is storage into spreadsheet in google sheets.
ideas and code for this code has been part taken from tuorials found in youtube and Real Python website
The live site can be found here -[The Quiz](https://rhogand.github.io/      /)
# Table of Content
* Design
* Features
    * Existing Features   
* Testing
* Technologies Used
* Languages Used
* Frameworks, Libraries & Programs Used
* Deployment
* Credits
* Acknowledgments
# Design Diagram 

The quiz is a console base application, which doesnt need visual graphic design. Therefore, a layout has been design to show how the code should work. [Layout](/images/Quiz%20design.png)
# Features
## Existing Features
some of the features of this project has been inpired by the love-Sandwich project.
In here the quiz manage to connect with google spreadsheet.
# Testing

* Code Validation
   *The Riding Centre website has been tested with Samsung galaxy S22 ultra mobile phone. Also with a samsung table.
    The code has been validated via the W3C HTML Validator,  and  W3C CSS Validator. 1 minor error was found when testing the  HTML code with HTML Validation but fixed and documented below.


* Lighthouse Testing
    * Performance - How the page performs whilst  loading.
    * Accessibility - Is the site accessible for all users, and how can it be improved.
    * Best Practices - The site conforms to industry best practices.
    * SEO - Search Engine Optimisation. Is the site optimised for search engine result rankings.

 ![lighthouse](/asset/images/Readme-Images/lighthouse.png)   

 * Bugs Fixed
     * 
* Fixed Bugs

  

# Technologies Used
## Main Languages Used
* Python
## Frameworks, Libraries & Programs Used
* Google spreadsheet
* Google Sheet API
* Google Drive API 
* Pyfiglet fonts 
* GitPod 
* Random
* Heroku - A data base use to deploy and storage the project. 

# Deployment
To prepare for deployment on Heroku a requirements.txt needs to be created in the same folder as the .py file in GitPod. This file needs to contain a list of all libraries the project needs to run as a Heroku App.

Then follow these steps:

Login to Heroku (Create an account if necessary)
Click on New in the Heroku dashboard and select ”Create new app”
Write a name for the app and choose your region and click ”Create App”
In the settings tab for the new application I created two Config vars.
One is named CREDS and contains the credentials key for Google Drive API
One is name PORT and has the value of 8000
Two buildpack scripts were added: Python and Nodejs (in that order)
Heroku CLI was used to deploy the project. The following steps were taken in the terminal in GitPod

Deploying your app to heroku

Login to heroku and enter your details.
command: heroku login -i
Get your app name from heroku.
command: heroku apps
Set the heroku remote. (Replace app_name with your actual app name)
command: heroku git:remote -a app_name
Add, commit and push to github
command: git add . && git commit -m "Deploy to Heroku via CLI"
Push to both github and heroku
command: git push origin main
command: git push heroku main

The live link can be found [here](https://rhogand.github.io/    /)
# Credits
## Credits content
 For code inspiration, design, help and advice. I use the following website
* [Geeksforgeeks tutorial](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - Use of Pyfiglet fonts
* [Youtube video Multiple choice quiz using Class](https://www.youtube.com/watch?v=SgQhwtIoQ7o&ab_channel=MikeDane/)
* [Youtube video Google sheets and quiz](https://www.youtube.com/watch?v=SbKSiJy2WRo&ab_channel=DataBeliever/) 
* [Youtube video](https://www.youtube.com/watch?v=YScd9FqGAZs&ab_channel=TechWithStephen/) - Quiz using dictionary
* [Real Paython tutorial](https://realpython.com/python-quiz-application/#step-2-make-your-application-user-friendly/) - How to create a quiz in python
 ## Media
 # Acknowledgments
The site was completed as part of a Full Stack Software Developer Diploma at the Code Institute, Project 3. 
I would like to thank my mentor Mitko, who has been a great help in this project.