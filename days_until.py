#!/usr/bin/python
import datetime
""" Gives days until event date given in (yyyy mm dd) format"""

def days_until(in_date) :
  (e_year,e_month,e_day) = in_date.split(' ')


  todays_date = datetime.datetime.now().date()
  event_date=datetime.date(int(e_year),int(e_month),int(e_day))
  date_until=event_date - todays_date
  print date_until.days



if __name__ == '__main__' :
    days_until(raw_input('Enter the event date (yyyy mm dd):'))
