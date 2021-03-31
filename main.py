import random
ans = random.randint(1, 20)
chance=3
high_count=0
low_count=0
close_count=0
name = input("Enter Player Name: ")
print("-------------------------------------------------------------------")
print("Rules:\n")
print("1. You will have 3 chances to Guess\n")
print("2. With every Wrong Answer your chance will be Deducted\n")
print("-------------------------------------------------------------------")
while(chance>0):
  predict = int(input("\nTry to Guess By Writing Number Here: "))
  if predict > ans:
    print("Your Guess is too High. Try Something Low\n")
    chance = chance-1
    high_count = high_count+1
    print("Remaining Chances: "+str(chance))
    print("-------------------------------------------------------------------\n")
  elif predict == ans:
    print("Bravo!!")
    print(name+", Your Guessing Power is phenomenon\n")
    exit()
  elif predict > (ans+5):
    print("You are Too close my Friend\n")
    chance = chance-1
    close_count = close_count+1
    print("Remaining Chances: "+str(chance))
    print("-------------------------------------------------------------------\n")
  elif predict < (ans+5):
    print("You are Too close my Friend\n")
    chance = chance-1
    close_count = close_count+1
    print("Remaining Chances: "+str(chance))
    print("-------------------------------------------------------------------\n")
  else:
    print("Too much Low! Try Some thing High\n")
    chance = chance-1
    low_count = low_count+1
    print("Remaining Chances: "+str(chance))
    print("-------------------------------------------------------------------\n")
else:
  print("Game Over : You Were Not able to Guess\n")
  print("Correct Answer was: "+str(ans))
  print("")
  print("Player Stats:")
  print("Player Name: "+name)
  print("Number of times your value was greater than Actual Value: "+str(high_count))
  print("Number of times your value was less than Actual Value: "+str(low_count))
  print("Number of times your value was near to the Actual Value: "+str(close_count))
  if close_count>low_count and close_count>high_count:
    print("Your Prediction was very much Close")
  else:
    print("Try to improve your Guessing Power")
  print("-------------------------------------------------------------------\n")

