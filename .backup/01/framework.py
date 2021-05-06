#    framework library for biogeochemical cycles game
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

import os,sys
sys.path.append(os.path.abspath('src/lib/'))
from gamelib.shortcode import *


class Util:
  def make(question,answer,answerlist=False,type='question'):
    global response
    '''Makes a question
    question    - value with the question
    answer      - The value or string that is the answer
    answerlist  - Shows an answer list if used (optional)'''
    if answerlist != False:
      pnt(color(question+"\n|-----",green))
      [print(color("|"+i,green)) for i in answerlist]
      userinput = inpt(color('''|-----
Please type your response below:\n> ''',green))
    else:
      pnt(color(question,green))
      userinput = inpt(color('Please type your response below:\n> ',green))
    if userinput == answer:
      response = 1
    else:
      response = 0
class Question:
  '''Questions class'''
  One = 'This is an example question'
class Answer:
  '''Answers class'''
  One = 'a'