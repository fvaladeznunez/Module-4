currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

currentTimeInt = int(currentTimeStr)
if currentTimeInt<=23 and currentTimeInt >= 0:
    print ("The current time is (in hours <=23)")
    
    
    
    waitTimeInt = int(waitTimeStr)

    finalTimeInt = currentTimeInt + waitTimeInt
    print(finalTimeInt)
else:
    print("The current time is invalid if > 23")
