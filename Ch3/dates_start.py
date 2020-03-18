#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  timenow = datetime.now()
  #print("Date is: ", today)
  Month = ["Jan", "Feb", "Mar", "Apr"]

  # print out the date's individual components
  days = ["mon", "tue", "wed", "thu", "fri" "sat", "sun"]
  #print("Date Components: ", days[today.weekday()])


  # retrieve today's weekday (0=Monday, 6=Sunday)
  days = ["Mon", "Tue", "Wed", "Thu", "Fri" "Sat", "Sun"]
  #print("Date Components: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  print(days[today.weekday()],"",Month[today.month-1],"",timenow.strftime("%I:%M:%S %p"))

  # Get the current time


  
if __name__ == "__main__":
  main();
  