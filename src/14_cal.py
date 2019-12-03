"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

user_input = input( 'Enter year(not necessary) and month seperated by a space:')

user_stuff = user_input.split(' ')

def log_input(ui):
  print(ui)

def generate_calendar(ui):
  
    print(calendar.month(2019, 12))

  # if len(ui) =0:
  #       print(calendar.month(2019, 12))
  #   elif len(ui) =1:
  #       print(calandar.month(2019, ui[0]))
  #   else:
  #       print(calandar.month(ui[1], ui[0]))

generate_calendar(user_stuff)