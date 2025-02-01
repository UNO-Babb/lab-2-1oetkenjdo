#FutureTime.py
#Name:
#Date:
#Assignment:

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24 #utc-6 timezone
  currentMinute = now.minute

  #Ask user for hours
  userinput = input("What time will it be after ____ hours, and ____ minutes? (Enter as 'H MM'): ")
 
  #split answer - hrs and min
  addHours, addMinutes = map(int, userinput.split())

  #Calculate the time after the user-supplied time has passed. (NEW TIME)
  totalMins = currentMinute + addMinutes
  totalHrs = currentHour + addHours + (totalMins // 60)

  futureHrs = totalHrs % 24 #(wraps around after 24hrs)
  futureMin = totalMins % 60 #(wraps around after 60 min)

  #Output the future time in standard format "HH:MM"
  print(f"In {addHours} hours and {addMinutes} minutes, it will be {futureHrs:02d}:{futureMin:02d}.")


if __name__ == '__main__':
  main()
