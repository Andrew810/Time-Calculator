def add_time(start, duration, day=None):
  #Setting up initial variables and splitting the arguments into usable parts.
  carry_the_one = 0
  new_time = [0, 0]
  duration_split = duration.split(":")
  start_split = start.split(":")
  days_added = 0
  x = start_split[1].split(" ") #x is a middleman for j. I can probably cut him out somehow
  start_split[1] = x[0]
  j = x[1] #j keeps track of if am or pm
  
  #adds the time together and creates a multiplier variable as well as a days_added variable
  new_time[1] = int(duration_split[1]) + int(start_split[1])
  if new_time[1] > 59:
    carry_the_one = 1
    new_time[1] -= 60
  new_time[0] = int(start_split[0]) + int(duration_split[0]) + carry_the_one
  multiplier = int(new_time[0] / 12)

  #determines how many days were added and stores in a variable
  if j == "PM" and multiplier == 1:
    days_added = 1
  elif j =="AM" and multiplier == 2:
    days_added = 1
  elif j == "PM" and multiplier > 2 and multiplier % 2 == 1:
    days_added = int(multiplier / 2 + 1)
  else:
    days_added = int(multiplier / 2)

  #checks if there was a starting day specified and then determins the weekday after the time was added.
  if day is not None:
    day = day.capitalize()
    day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day_index = day_of_week.index(day)
    day_index += days_added
    if day_index > 6:
      day_multi = int(day_index / 7)
      day_index -= 7 * day_multi

  #Determines if am or pm. Can probably use days_added to make the code cleaner. Might change later.
  if new_time[0] > 11:
    new_time[0] -= 12 * multiplier 
    if multiplier % 2 == 1 and j == "AM":
      j = "PM"
    elif multiplier % 2 == 1 and j == "PM":
      j = "AM" 
      
  #bug fixes
  if new_time[0] == 0:
    new_time[0] = 12
  if new_time[1] < 10:
    new_time[1] = str(new_time[1]).zfill(2)
  
  #The finisher. 
  finisher = f"{new_time[0]}:{new_time[1]} {j}"
  if day is not None and days_added > 1:
    return finisher + f", {day_of_week[int(day_index)]} ({days_added} days later)"
  elif day is not None and days_added == 1:
    return finisher + f", {day_of_week[int(day_index)]} (next day)"
  elif day is not None and days_added == 0:
    return finisher + f", {day_of_week[int(day_index)]}"
  elif day is None and days_added > 1:
    return finisher + f" ({str(days_added)} days later)"
  elif day is None and days_added == 1:
    return finisher + " (next day)"
  else:
    return finisher
