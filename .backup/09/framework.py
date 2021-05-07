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
  '''Utility Class'''
  def make(question,answer,answerlist=False,Score=None,Streak=None,Answered=None):
    answerinputs  = ['a','b','c','d']
    global response
    '''Makes a question
    question    - Value or string with the question
    answer      - The string that is the answer
    answerlist  - Displays an answer list (optional)
    Score       - Displays a score counter (optional)
    Streak      - Displays a streak counter (optional)'''
  
    if answerlist != False:

      while True:
        clr()
        if Score != None:
          if Streak != None:
            pnt(color('Streak:   ',green)+color(str(Streak),yellow))
          if Answered != None:
            pnt(color('Answered: ',green)+color(str(Answered),'magenta'))
          pnt(color('Score:    ',green)+color(str(Score),cyan))
        pnt(color(question+"\n|-----",green))
        for key in answerlist:
          pnt(color('| ',green)+color(key+': '+answerlist[key],yellow)) 
        userinput = inpt(color('|-----\nPlease type your response below (e.g. "a") and press enter:\n> ',green))
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
      userinput = inpt(color('Please type your response below and press enter:\n> ',green))

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
      QA.q10.list,
      QA.q11.list,
      QA.q12.list,
      QA.q13.list,
      QA.q14.list,
      QA.q15.list,
      QA.q16.list,
      QA.q17.list,
      QA.q18.list,
      QA.q19.list,
      QA.q20.list,
      QA.q21.list,
      QA.q22.list,
      QA.q23.list,
      QA.q24.list,
      QA.q25.list,
      QA.q26.list,
      QA.q27.list,
      QA.q28.list,
      QA.q29.list,
      QA.q30.list,
      QA.q31.list,
      QA.q32.list,
      QA.q33.list,
      QA.q34.list,
      QA.q35.list,
      QA.q36.list,
      QA.q37.list,
      QA.q38.list,
      QA.q39.list,
      QA.q40.list,
      QA.q41.list,
      QA.q42.list,
      QA.q43.list,
      QA.q44.list,
      QA.q45.list,
      QA.q46.list,
      QA.q47.list,
      QA.q48.list,
      QA.q49.list,
      QA.q50.list
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
  class q11:
    num   = '11'
    ques  = 'What is the product of photosynthesis?'
    ans   = 'b'
    ans_dict = {
      'a':'Glucose and ATP',
      'b':'O2 and Glucose',
      'c':'CO2 and H2O',
      'd':'CO2 and ATP'
    }
    list = [num,ques,ans,ans_dict]
  class q12:
    num   = '12'
    ques  = 'The movement of a substance through places and compartments is called...'
    ans   = 'a'
    ans_dict = {
      'a':'Flux',
      'b':'Step',
      'c':'Process',
      'd':'Sink'
    }
    list = [num,ques,ans,ans_dict]
  class q13:
    num   = '13'
    ques  = 'A storage place for substances'
    ans   = 'a'
    ans_dict = {
      'a':'Sink',
      'b':'Lithosphere',
      'c':'Hydrosphere',
      'd':'Atmosphere'
    }
    list = [num,ques,ans,ans_dict]
  class q14:
    num   = '14'
    ques  = 'The partitioning and cycling of chemical elements and compounds between parts of an ecosystem.'
    ans   = 'a'
    ans_dict = {
      'a':'Biogeochemical Cycle',
      'b':'The Rock Cycle',
      'c':'The Water Cycle',
      'd':'The Nitrogen Cycle'
    }
    list = [num,ques,ans,ans_dict]
  class q15:
    num   = '15'
    ques  = 'The chemicals we find under the ground that are made from remains of past living things.'
    ans   = 'b'
    ans_dict = {
      'a':'Ammonium',
      'b':'Fossil Fuels',
      'c':'Acid',
      'd':'Unfix Nitrogen'
    }
    list = [num,ques,ans,ans_dict]
  class q16:
    num   = '16'
    ques  = 'Most abundant gas in the atmosphere?'
    ans   = 'c'
    ans_dict = {
      'a':'Carbon Dioxide',
      'b':'Oxygen',
      'c':'Nitrogen',
      'd':'Argon'
    }
    list = [num,ques,ans,ans_dict]
  class q17:
    num   = '17'
    ques  = 'Which one is "Abiotic"?'
    ans   = 'b'
    ans_dict = {
      'a':'Fish',
      'b':'Rock',
      'c':'Dog',
      'd':'Kangaroo'
    }
    list = [num,ques,ans,ans_dict]
  class q18:
    num   = '18'
    ques  = 'What word describes "occurring and reoccurring"?'
    ans   = 'a'
    ans_dict = {
      'a':'Constants',
      'b':'Products',
      'c':'Reactants',
      'd':'Flux'
    }
    list = [num,ques,ans,ans_dict]
  class q19:
    num   = '19'
    ques  = 'What is the name of the ecosystem made up of parts of Earth made out of water like oceans and rivers?'
    ans   = 'd'
    ans_dict = {
      'a':'Biosphere',
      'b':'Lithosphere',
      'c':'Atmosphere',
      'd':'Hydrosphere'
    }
    list = [num,ques,ans,ans_dict]
  class q20:
    num   = '20'
    ques  = 'What is the name of the ecosystem made up of living things like plants and animals?'
    ans   = 'a'
    ans_dict = {
      'a':'Biosphere',
      'b':'Atmosphere',
      'c':'Biochemical Sphere',
      'd':'Lithosphere'
    }
    list = [num,ques,ans,ans_dict]
  class q21:
    num   = '21'
    ques  = 'What rock forms from magma below the surface'
    ans   = 'a'
    ans_dict = {
      'a':'Intrusive Igneus Rocks',
      'b':'Extrusive Igneus Rocks'
    }
    list = [num,ques,ans,ans_dict]
  class q22:
    num   = '22'
    ques  = 'What rock is formed when chemical reactions with hot fluids, tremendous heat, and great pressure occur? '
    ans   = 'b'
    ans_dict = {
      'a':'Sedimentary',
      'b':'Metamorphic',
      'c':'Divergent',
      'd':'Volcano'
    }
    list = [num,ques,ans,ans_dict]
  class q23:
    num   = '23'
    ques  = 'The ocean is a sink'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q24:
    num   = '24'
    ques  = 'Foliated rocks are thin flat metamorphic rocks with layers.'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q25:
    num   = '25'
    ques  = 'What is the name for “liquid to solid”?'
    ans   = 'c'
    ans_dict = {
      'a':'Lification',
      'b':'Melting',
      'c':'Crystalization',
      'd':'Erosion'
    }
    list = [num,ques,ans,ans_dict]
  class q26:
    num   = '26'
    ques  = 'The process in which loose sediments are cemented together.'
    ans   = 'b'
    ans_dict = {
      'a':'Erosion',
      'b':'Lification',
      'c':'Weathering',
      'd':'Clastic'
    }
    list = [num,ques,ans,ans_dict]
  class q27:
    num   = '27'
    ques  = 'MYA means "Million Years Again"'
    ans   = 'b'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q28:
    num   = '28'
    ques  = 'What occurs at subduction zones?'
    ans   = 'c'
    ans_dict = {
      'a':'Hurricanes',
      'b':'Folded Mountains',
      'c':'Volcanoes',
      'd':'Mid-Ocean Range'
    }
    list = [num,ques,ans,ans_dict]
  class q29:
    num   = '29'
    ques  = 'A transformative boundary is when two plates slide past each other.'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q30:
    num   = '30'
    ques  = 'What is the partially melted layer below the crust'
    ans   = 'd'
    ans_dict = {
      'a':'Atmosphere',
      'b':'Lithosphere',
      'c':'Rocksphere',
      'd':'Asthenosphere'
    }
    list = [num,ques,ans,ans_dict]
  class q31:
    num   = '31'
    ques  = 'What happens when a divergent boundary even occurs?'
    ans   = 'd'
    ans_dict = {
      'a':'Volcanoes',
      'b':'Trench',
      'c':'Hurricane',
      'd':'Sea Floor Spreading'
    }
    list = [num,ques,ans,ans_dict]
  class q32:
    num   = '32'
    ques  = 'What can earthquakes cause? They may affect people and communities.'
    ans   = 'b'
    ans_dict = {
      'a':'Mountains',
      'b':'Tsunamis',
      'c':'Sedimentary Rocks',
      'd':'Lithosphere'
    }
    list = [num,ques,ans,ans_dict]
  class q33:
    num   = '33'
    ques  = 'What happens when two tectonic plates slide past each other?'
    ans   = 'b'
    ans_dict = {
      'a':'Volcanoes',
      'b':'Earthquakes',
      'c':'Igneous',
      'd':'Mid-Ocean Range'
    }
    list = [num,ques,ans,ans_dict]
  class q34:
    num   = '34'
    ques  = 'What is the name for the industrial process in which ammonia is produced from nitrogen and hydrogen?'
    ans   = 'b'
    ans_dict = {
      'a':'Nitrogen Uptake',
      'b':'Haber Process',
      'c':'Legume',
      'd':'Ammonification'
    }
    list = [num,ques,ans,ans_dict]
  class q35:
    num   = '35'
    ques  = 'What is Mineral Apatite?'
    ans   = 'a'
    ans_dict = {
      'a':'Phosphorus Rich Mineral',
      'b':'Metamorphic',
      'c':'Decomposition',
      'd':'ATP'
    }
    list = [num,ques,ans,ans_dict]
  class q36:
    num   = '36'
    ques  = 'When sea ice melts it changes the water level'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q37:
    num   = '37'
    ques  = 'Combustion is a sink'
    ans   = 'b'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q38:
    num   = '38'
    ques  = 'Transpiration is a flux'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q39:
    num   = '39'
    ques  = 'A convergent boundary is two plates colliding'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q40:
    num   = '40'
    ques  = 'What is the name for ash and rock from a volcano'
    ans   = 'a'
    ans_dict = {
      'a':'Tephra',
      'b':'Foliated',
      'c':'Extrusive',
      'd':'Chemical'
    }
    list = [num,ques,ans,ans_dict]
  class q41:
    num   = '41'
    ques  = 'A plastic chair is biotic'
    ans   = 'b'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q42:
    num   = '42'
    ques  = 'What is the chemical formula for Nitrates?'
    ans   = 'd'
    ans_dict = {
      'a':'N2',
      'b':'NO3',
      'c':'CO2',
      'd':'NO2'
    }
    list = [num,ques,ans,ans_dict]
  class q43:
    num   = '43'
    ques  = 'Ammonium is present in the nitrogen cycle'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q44:
    num   = '44'
    ques  = 'What can massive rainfall cause?'
    ans   = 'b'
    ans_dict = {
      'a':'Earthquake',
      'b':'Flooding',
      'c':'Forest Fire',
      'd':'Volcano'
    }
    list = [num,ques,ans,ans_dict]
  class q45:
    num   = '45'
    ques  = 'A tree is a sink'
    ans   = 'a'
    ans_dict = {
      'a':'True',
      'b':'False'
    }
    list = [num,ques,ans,ans_dict]
  class q46:
    num   = '46'
    ques  = 'What is the word for a usually rapid chemical process (such as oxidation) that produces heat and usually light?'
    ans   = 'c'
    ans_dict = {
      'a':'Photosynthesis',
      'b':'Respiration',
      'c':'Combustion',
      'd':'Nitrogen fixation'
    }
    list = [num,ques,ans,ans_dict]
  class q47:
    num   = '47'
    ques  = 'What is the name of a rock that is formed chiefly by accumulation of organic remains (such as shells or coral), consists mainly of calcium carbonate, is extensively used in building, and yields lime when burned?'
    ans   = 'a'
    ans_dict = {
      'a':'Limestone',
      'b':'Igneous',
      'c':'Granite',
      'd':'Diorite'
    }
    list = [num,ques,ans,ans_dict]
  class q48:
    num   = '48'
    ques  = 'What rock type is formed from weathered fragments put together?'
    ans   = 'a'
    ans_dict = {
      'a':'Sedimentary',
      'b':'Granite',
      'c':'Obsidian',
      'd':'Sandstone'
    }
    list = [num,ques,ans,ans_dict]
  class q49:
    num   = '49'
    ques  = 'What is magma called when it cools and hardens?'
    ans   = 'a'
    ans_dict = {
      'a':'Lava',
      'b':'Still called magma',
      'c':'Hot stuff'
    }
    list = [num,ques,ans,ans_dict]
  class q50:
    num   = '50'
    ques  = 'What rock is made from plants that lived millions of years ago?'
    ans   = 'a'
    ans_dict = {
      'a':'Coal',
      'b':'Limestone',
      'c':'Sedimentary',
      'd':'Fossils (Bones)'
    }
    list = [num,ques,ans,ans_dict]