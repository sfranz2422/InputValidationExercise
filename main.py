keep_running = True
sum=0
count=0
average=0
while keep_running:
  number = input("Enter a number or done\n")
  try:
    sum += int(number)
    count = count+1
    average = sum/count
  except:
    if number.upper() == 'DONE':
      keep_running=False
      print(f"The sum is {sum}")
      print(f"The number of inputs is {count}")
      print(f"The average of your data is {average}")
    else:
      print("Invalid data, Try again")