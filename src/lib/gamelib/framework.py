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
  def make(question,answer,answerlist=False):
    global response
    '''Makes a question
    question    - value with the question
    answer      - The value or string that is the answer
    answerlist  - Shows an answer list if used (optional)'''
    if answerlist != False:
      pnt(question)
      [print(i) for i in answerlist]
      response = inpt('''-----
Please type your response below:
> ''')
    else:
      pnt(question)
      response = inpt('''Please type your response below:
> ''')
class Question:
  '''Questions class'''
  One = 'This is an example question'
class Answer:
  '''Answers class'''
  One = 'a'