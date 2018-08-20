"""This is a basic CRUD calendar application made in Python"""
from time import sleep, strftime

NAME = "George"

calendar = {}

def welcome():
  print("Welcome", NAME)
  print("Opening calendar...")
  sleep(1)
  print(strftime("%A %B %d, %Y"))
  print(strftime("%H:%M:%S"))
  sleep(1)
  print("What would you like to do?")
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("Enter one of the following: \n A to Add: \n U to Update: \n V to View: \n D to Delete: \n X to exit: \n")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) == 0:
        print("The calendar is currently empty.")
      else:
        print(calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print("Calendar updated!")
      print(calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print("Please enter the date in the proper (MM/DD/YYYY) format")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print("Event successfully added!")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) == 0:
        print("The calendar is currently empty. There is nothing to delete!")
      else:
      	event = input("What event?")
      	for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("Event deleted!")
            print(calendar)
            break
          else:
            print("You entered a non-existent event!")
    elif user_choice == "X":
      start = False
    else:
      print("Invalid command")
      break
    
start_calendar()

