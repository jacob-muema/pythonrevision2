numbers =[1,2,3,4,5,6]
target = int(input("Enter a number"))

for num in numbers:
   if num ==target:
       print("number found")
       break
else:
    print("Number not found")