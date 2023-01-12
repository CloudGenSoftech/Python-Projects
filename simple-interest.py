#write a python program to print simple interest 
price = float(input("Enter Pinciple Amount"))
rate = float(input("Enter Rate of Interest"))
time= float(input("Enter number of Months"))
print("The Given Price is ", price)
print("The Given Rate of Interest is ",rate)
print("The Given Time is ", time)
omr = price * rate/100
print("The One Month Rate of Interest is ", omr)
totint=omr*time
print("The total interest is  ",totint)
tpa=totint+price
print("The total payable amount is ",tpa)

