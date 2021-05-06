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
sys.path.append(os.path.abspath('src/lib/'))
from gamelib.framework import *

class Game:
  '''Main game class (prevents conflicts)'''
  def startgame():
    '''Starts the game'''
    inpt('There is no game\n')

  def testgame():
    '''A test game to start'''
    