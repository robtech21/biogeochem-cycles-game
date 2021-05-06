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
#sys.path.append(os.path.abspath('src/lib/'))
from gamelib.shortcode import *


class Util:
  
  def make(question,answer,answerlist=False,Score=None):
    answerinputs  = ['a','b','c','d']
    global response
    '''Makes a question
    question    - Value or string with the question
    answer      - The string that is the answer
    answerlist  - Shows an answer list if used (optional)'''
  
    if answerlist != False:

      while True:
        clr()
        if Score != None:
          pnt(color('Score: ',green)+color(str(Score),cyan))
        pnt(color(question+"\n|-----",green))
        for key in answerlist:
          pnt(color('| ',green)+color(key+': '+answerlist[key],yellow)) 
        userinput = inpt(color('|-----\nPlease type your response below:\n> ',green))
        userinput = userinput.lower()
        if userinput != '':
          if userinput == '1':
            userinput = 'a'
          if userinput == '2':
            userinput = 'b'
          if userinput == '3':
            userinput = 'c'
          if userinput == '4':
            userinput = 'd'
          if userinput in answerinputs:
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
    questionList = [
      QA.q1.list,
      QA.q2.list,
      QA.q3.list,
      QA.q4.list,
      QA.q5.list,
      QA.q6.list,
      QA.q7.list,
      QA.q8.list,
      QA.q9.list,
      QA.q10.list
    ]
    list = random.choice(questionList)
    questionInfo = list

    # All of this is here for debugging in case it breaks again

    #pnt('Question Num:  '+questionInfo[0])
    #pnt('Question:      '+questionInfo[1])
    #pnt('Answer:        '+questionInfo[2])
    #pnt('Answer list:   ')
    #pnt(questionInfo[3])
    #inpt()
    return questionInfo

class QA:
  '''Contains questions with data'''
  class null:
    '''Null question as a template, do not use.'''
    num   = ''
    ques  = ''
    ans   = ''
    ans_dict = {
      'a':'',
      'b':'',
      'c':'',
      'd':''
    }
    list = [num,ques,ans,ans_dict]
  class q1:
    num   = '1'
    ques  = 'If two tectonic plates were to collide and slide past each other, which kind of rock would be the output?'
    ans   = 'a'
    ans_dict = {
      'a':'Metamorphic',
      'b':'Igneous',
      'c':'Sediments',
      'd':'Sedimentary'
    }
    list  = [num,ques,ans,ans_dict]
  class q2:
    num   = '2'
    ques  = 'What is the section of the earth that deals with the inorganic matter such as rocks?'
    ans   = 'c'
    ans_dict = {
      'a':'Troposphere',
      'b':'Hydrosphere',
      'c':'Lithosphere',
      'd':'Biosphere'
    }
    list  = [num,ques,ans,ans_dict]
  class q3:
    num   = '3'
    ques  = 'What category of rock is formed by cooling of liquid magma?'
    ans   = 'b'
    ans_dict = {
      'a':'Metamorphic',
      'b':'Igneus',
      'c':'Obsidian',
      'd':'Granite'
    }
    list = [num,ques,ans,ans_dict]
  class q4:
    num   = '4'
    ques  = "What type of rock is formed by compaction of smaller rocks?"
    ans   = "d"
    ans_dict = {
      'a':'Sediments',
      'b':'Metamorphic',
      'c':'Magma',
      'd':'Sedimentary'
    }
    list  = [num,ques,ans,ans_dict]
  class q5:
    num   = '5'
    ques  = 'What is the chemical formula for atmospheric nitrogen?'
    ans   = 'd'
    ans_dict = {
      'a':'NH2',
      'b':'NO2',
      'c':'N3HO3',
      'd':'N2'
    }
    list = [num,ques,ans,ans_dict]
  class q6:
    num   = '6'
    ques  = 'What is the prokaryotic microorganism that can change atmospheric nitrogen into fixed nitrogen?'
    ans   = 'd'
    ans_dict = {
      'a':'Legumes',
      'b':'Nitrifying bacteria',
      'c':'Denitrifying bacteria',
      'd':'Nitrogen fixing bacteria'
    }
    list = [num,ques,ans,ans_dict]
  class q7:
    num   = '7'
    ques  = 'When a divergent event happens underwater, what happens?'
    ans   = 'c'
    ans_dict = {
      'a':'Trench',
      'b':'Subduction',
      'c':'Mountain Range',
      'd':'Earthquake'
    }
    list = [num,ques,ans,ans_dict]
  class q8:
    num   = '8'
    ques  = 'What is the process of an ocean plate sliding under a continental plate called?'
    ans   = 'c'
    ans_dict = {
      'a':'Abduction',
      'b':'Seperation',
      'c':'Subduction',
      'd':'Convergent'
    }
    list = [num,ques,ans,ans_dict]
  class q9:
    num   = '9'
    ques  = 'What are the outputs of cellular respiration?'
    ans   = 'a'
    ans_dict = {
      'a':'ATP, CO2, H2O',
      'b':'ATP, Glucose, H20',
      'c':'Glucose, O2',
      'd':'02, H20'
    }
    list = [num,ques,ans,ans_dict]
  class q10:
    num   = '10'
    ques  = "What is the type of organism that makes it's own food?"
    ans   = 'c'
    ans_dict = {
      'a':'Heterotroph',
      'b':'Organic',
      'c':'Autotrouph',
      'd':'Chloroplast'
    }
    list = [num,ques,ans,ans_dict]