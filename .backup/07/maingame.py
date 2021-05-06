'''
#    Main game stuff for biogeochemical cycles game
#    Copyright (C) 2021  Robert Furr
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import os,sys
#sys.path.append(os.path.abspath('src/lib/'))
from gamelib.framework import *

class Game:
  '''Main game class (prevents conflicts)'''
  def startquestion():
    questionInfo = Util.randQuestion()
    Util.make(questionInfo[0],questionInfo[1],questionInfo[2])
  def startgame():
    '''Starts the game'''
    global questions_wrong,questions_right,score,streak,answered
    # Key:
    # 0 - Question number
    # 1 - Question
    # 2 - Answer
    # 3 - Answer List
    def extrapoint():
      global score
      pnt(color("What's this? Looks like you got an extra point! :)",cyan))
      score = score + 1
    scorelimit        = 20
    score             = 0
    questions_wrong   = 0
    questions_right   = 0
    answered          = 0
    streak            = 0
    previousQuestion  = None
    pnt(color('Pre-Game Config',green))
    choice = inpt(color('What score to play to? (Leave empty for default of 20)\n> ',green))
    if choice != '':
      try:
        scorelimit = int(choice)    
      except ValueError:
        pass
    while score < scorelimit:
      if score < 0:
        score = 0
      questionInfo = Util.randQuestion()
      if questionInfo[0] != previousQuestion:
        response = Util.make(questionInfo[1],questionInfo[2],questionInfo[3],Score=score,Streak=streak,Answered=answered)
        if response == 0:
          questions_wrong = questions_wrong + 1
          streak = 0
          pnt(color('Incorrect :(\nStreak lost',red))
          pnt(color('The correct answer is: ',green)+color(questionInfo[2].upper(),cyan))
          if random.randint(1,1000) == 1:
            pnt(color("What's this? You didn't lose any points! :)",cyan))
            score = score - 0
          else:
            score = score - 1
        if response == 1:
          questions_right = questions_right + 1
          streak          = streak + 1
          score           = score  + 1
          pnt(color('Correct!',cyan))
          if streak < 5:
            if random.randint(1,300) == 1:
              extrapoint()
          if streak >= 5 and streak < 10:
            if random.randint(1,250) == 1:
              extrapoint()
          if streak >= 10 and streak < 15:
            if random.randint(1,200) == 1:
              extrapoint()
          if streak >=15 and streak <= 20:
            if random.randint(1,150) == 1:
              extrapoint()
        answered = answered + 1
        inpt(color('Press Enter\n',green))
      previousQuestion = questionInfo[0]
    clr()
    pnt(color('''Game Finished
|=====
|Stats:''',green))
    pnt(color('|',green)+color('Questions Wrong:    '+str(questions_wrong),red))
    pnt(color('|',green)+color('Questions Right:    '+str(questions_right),cyan))
    pnt(color('|',green)+color('Questions Answered: '+str(answered),'magenta'))
    inpt(color('|=====\nPress enter to go to title\n',green))
