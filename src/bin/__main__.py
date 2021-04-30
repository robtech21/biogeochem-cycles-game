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
sys.path.append(os.path.abspath('src/lib/'))
from gamelib.framework import *

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
    Util.make(Question.One,Answer.One,answerlist=['a','b','c','d'])
  if choice == '2':
    inpt(color('''
CREDITS:

Developer:    Robert Furr - https://github.com/robtech21
Modules used: termcolor   - https://pypi.org/project/termcolor/

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
    exit(0)