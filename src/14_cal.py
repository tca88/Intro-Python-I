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
from datetime import date

sys_arg = sys.argv

datem = datetime.today()

def my_calendar(*user_inputs):
    if (len(user_inputs) == 1):
        year = datem.year
        month = datem.month
    elif (len(user_inputs) == 2):
        year = datem.year
        month = user_inputs[1]
    else:
        month = user_inputs[1]
        year = user_inputs[2]
    if(month and year):
        c = calendar.TextCalendar(calendar.SUNDAY)
        formated_c = c.formatmonth(int(year), int(month))
        return formated_c


print(my_calendar(*sys_arg))