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
    inpt('There is no game\n')

  def testgame():
    global questions_wrong,questions_right,score
    '''A test game to start'''
    # Key:
    # 0 - Question number
    # 1 - Question
    # 2 - Answer
    # 3 - Answer List
    score             = 0
    questions_wrong   = 0
    questions_right   = 0
    previousQuestion  = None
    while score < 10:
      clr()
      questionInfo = Util.randQuestion()
      if questionInfo[0] != previousQuestion:
        response = Util.make(questionInfo[1],questionInfo[2],questionInfo[3],Score=score)
      if response == 0:
        pnt(color('Incorrect :(',red))
        pnt(color('The correct answer is: ',green)+color(questionInfo[2].upper(),cyan))
      if response == 1:
        pnt(color('Correct!',cyan))
      score = score + response
      inpt(color('Press Enter\n',green))
      

    clr()
    pnt(color('''Game Finished
=====
Stats:''',green))
    pnt(color('Questions Wrong: '+questions_wrong,red))
    pnt(color('Questions Right: '+questions_right,green))
    inpt(color('=====\nPress enter to go to title\n',green))
