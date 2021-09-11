

![picture of the game](/assets/images/game.jpg)


# [LINK FOR LIVE VIEW](https://battleships-odimac.herokuapp.com/)

# Content

1. Introduction
2. User experience (UX)
3. Possible features to add
4. Testing
5. Bugs
6. Deploying to Heroko
7. Validation
8. Tech used
9. Media used
10. Credits




# Introduction
Going into this project i wanted to build a small game, and something that i can evolve after this course comes to an end. therefore i picked a battleship game and sofar this only got the most basic functions but possibilities to evolve it will be presented further down.

# User experience (UX)
Coming down to the looks of the game its a basic terminal game and therefore it wont be the best looking game. the functions of the game is explained and what you need to do is therefore easy to understand. i added so that when you start the game you will see the rules of the game and what your goal will be. 

![picture of the rules](/assets/images/start_game.jpg)

# Possible features to add  #

As stated above this game has alot of possibilities to evolve. I will list some of the features that i will work on in the future.

- A mode where you can play against the computer. having someone shooting back at you

- A mode where you can play against someone else at the same computer or over the internet.

- Possibilities to place your own ships.

- Ships in diffrent sizes.

- Difficulty against the computer.

The computer mode was supposed to come in this project but due to some bugs I found right before deployment i made a choice to rether have a fully functional smaller game then a broken bigger.

# Testing

All testing has been done through out the project and i will present some of the bigger bugs that i ran into and also the fixes that was done for these. some bugs was harder to debug then others and some was just mistakes done while typing. But the listed ones are the ones that gave me a headache.

## Testing pictures ##

![picture of computer winning](/assets/images/computer_wins.jpg)
![picture of the rules](/assets/images/winning.jpg)
![picture of the rules](/assets/images/gameplay1.jpg)

# Bugs

- Ships didnt get deployed, this bug was a mistake frommy side and mostly happend cause i was copying the code from visual studio where i wrote it to gitpod. 
FIXED: i forgot to add "from random import randint" in my run.py file

- Deployed one ship only, i got an index error and this i got help from my mentor solving on a call, he gave me hints and finally i could sort it.
FIXED: I didnt compensate for the 0 that comes in the array and therefore the app tried to deploy ships outside of the map, resulting in an error.

- Counter for sinked ships didnt work, This bug is the nemisis of this project. for 2 hours i was sitting trying to find the logic that was wrong. since i didnt get any errors on it i didnt get any help with finding the broken part. and even if knowing what function wasent working it still took me forever to find the typo that caused the problem.
FIXED: Corrected a typo from "colums" to "column" 

- Wasent able to shoot last line
FIXED: missed to att the 9 as one of the active numbers in the code. (line 65)

![picture of one bug](/assets/images/bugfix1.jpg)

# Deploying to Heroku

- First you need to have the project ready on Github.
    - Make sure that your Creds file is in gitignore if needed
    - Add the requirements.txt my using the command "pip3 freeze > requirements.txt"
    - Add \n to the input lines.

- Now when this is set we can move on

- Go onto [Heroku](https://id.heroku.com/login)

- Login or create a new account if you dont have one already.

- Click create new app.

- Choose name for your project, and your region.

- Go to setting shown in picture below. (red first picture)

- Click on reveal config vars (green)
    - Here you need to add Key: PORT and Value: 8000 (black)
    - Also you need to add your CREDS file if you are using API for the project beeing able to access this one.

- Next we add build packs (yellow)
    - We start by adding python (brown)
    - AFTER this we add nodejs (pink)
    - Order here is important.

- Now head over to Deploy (purple)

- Connect to github (blue) login.

- The grey marking wil show a box where you can search for your repos. type in your repo name. and connect to this one with the button. 

- After this we click the green marked button at the bottom and the project will be deployed and at the bottom we will get your link when all is done. 

![picture of settings for heroku](/assets/images/heroko_settings.jpg)
![picture of deployment](/assets/images/heroku_deploy.jpg)


# Validation
 Pep validation been done twice first one came back with some errors as shown below. all of these have after that been fixed and its now a clean slate. pictures below illustrates before and after.

 ![picture of the rules](/assets/images/first_pep8.jpg)
 ![picture of the rules](/assets/images/pep8_finished.jpg)



# Tech used

Game is built using Python alone.  

- [GitHub](https://www.github.com)
Hold the respiratory for this project along with files.
    
- [Gitpod](https://www.gitpod.io)
The platform ive been submitting and writing the final code.
    
- [Heroku](https://id.heroku.com/login)
To deploy the code in an app.
     
- Visual Studio (desktop)
Been coding in Visual Studio first and tested the code before i copied it up to github for commits.

- [Extendsclass](https://extendsclass.com/python.html)
For live testing my code

- [Replit](https://replit.com)
For even furter live testing of the code.
    

# Media

- [Youtube](https://youtube.com) Been watching countless of videos on Youtube for inspiration and watching code in action. 

- [Google](https://google.com) Searches for both coding assistance or finding a specific command that i was looking for. 


# Credit

- As usual thx to my mentor Felipe Souza, this time you really saved my with your knowledge, thx for not giving up.

-  Aswell as the slack community, not very much help with the code this time around but keeping the spirit up and chatting when needed. 
