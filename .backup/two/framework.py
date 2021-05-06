'''
#    Q/A framework library for biogeochemical cycles game
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
import os,sys,random
from gamelib.shortcode import *


class Util:
  def make(question,answer,answerlist=False,type='question'):
    global response
    '''Makes a question
    question    - Value or string with the question
    answer      - The string that is the answer
    answerlist  - Shows an answer list if used (optional)'''
  
    if answerlist != False:
      while True:
        clr()
        pnt(color(question+"\n|-----",green))
        for key in answerlist:
          pnt(color('| '+key+': '+answerlist[key],green)) 
        userinput = inpt(color('|-----\nPlease type your response below:\n> ',green))
        if userinput != '':
          break

    else:
      pnt(color(question,green))
      userinput = inpt(color('Please type your response below:\n> ',green))

    if userinput == answer:
      response = 1
    else:
      response = 0
    return response
  def randQuestion():
    global questionInfo
    questionSelect  = random.randint(1,4)
    if questionSelect == 1:
      list = QA.one.list
    if questionSelect == 2:
      list = QA.two.list
    if questionSelect == 3:
      list = QA.three.list
    if questionSelect == 4:
      list = QA.four.list
    questionInfo = [list[0],list[1],list[2]]
    return questionInfo

class QA:
  '''Questions and answers class'''
  class one:
    ques  = 'If two tectonic plates were to collide and slide past each other, which kind of rock would be the output?'
    ans   = 'a'
    ans_dict = {
      'a':'Metamorphic',
      'b':'Igneous',
      'c':'Sediments',
      'd':'Sedimentary'
    }
    list  = [ques,ans,ans_dict]
  class two:
    ques  = 'What is the section of the earth that deals with the inorganic matter such as rocks?'
    ans   = 'c'
    ans_dict = {
      'a':'Troposphere',
      'b':'Hydrosphere',
      'c':'Lithosphere',
      'd':'Biosphere'
    }
    list  = [ques,ans,ans_dict]
  class three:
    ques  = 'What category of rock is formed by cooling of liquid magma?'
    ans   = 'b'
    ans_dict = {
      'a':'Metamorphic',
      'b':'Igneus',
      'c':'Obsidian',
      'd':'Granite'
    }
    list = [ques,ans,ans_dict]
  class four:
    ques  = "What type of rock is formed by compaction of smaller rocks?"
    ans   = "d"
    ans_dict = {
      'a':'Sediments',
      'b':'Metamorphic',
      'c':'Magma',
      'd':'Sedimentary'
    }
    list  = [ques,ans,ans_dict]