#!/usr/bin/env python3

#    My biogeochemical cycles game
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
#sys.path.append(os.path.abspath('src/lib/'))
from gamelib.framework import *
from gamelib.maingame import *

while True:
  clr()
  choice = inpt(color('''
|==========================|
|Biogeochemical Cycles Game|
|==========================|
|1. Start                  |
|2. Credits                |
|3. Exit                   |
|==========================|
> ''',green))
  if choice == '1':
    clr()
    Game.testgame()
  if choice == '2':
    clr()
    inpt(color('''
Biogeochemical Cycles Game

|===================================================|
|CREDITS:                                           |
|                                                   |
|Developer:                          - Robert Furr  |
|Co-Developer:                       - Cody Dennis  |
|Writer for questions and scenarios: - Ethan Eberly |
|===================================================|

    License:

    My biogeochemical cycles game
    Copyright (C) 2021  Robert Furr

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

Press enter to go back to title
''',green))
  if choice == '3':
    pnt(color('Come again soon!',green))
    exit(0)