import math
# step 1
firstName = "gabriella"
 
# step 2
lastName = "WILLIAMS"
 
# step 3
print("Hello, ", firstName.upper(), lastName.lower())
 
# step 4
print("\n\n")
 
# step 5
fullName = "Gabriella Williams"
 
# step 6
print(fullName[10:18:1])
 
# step 7
fullName = fullName.replace("Williams", "Williams, Walsh College Student")
print(fullName)
 
# step 8
print('"Start by doing whats necessary; then do whats possible; and suddenly you are doing the impossible - Francis of Assisi"')
 
# step 9
firstDecimal = 3.26
secondDecimal = 4.26
 
# step 10
addition = firstDecimal + secondDecimal
subtraction = firstDecimal - secondDecimal
multiplication = firstDecimal * secondDecimal
division = firstDecimal / secondDecimal
 
# step 11
print("\n", firstDecimal, "plus", secondDecimal, "equals", addition)
print("\n", str(firstDecimal), "minus " + str(secondDecimal) + " equals " + str(subtraction))
print("\n {} multiplied by {} is {}".format(firstDecimal, secondDecimal, multiplication))
print(f"\n {firstDecimal} divided by {secondDecimal} equals {division}")
 
# step 12
sq_root = round(math.sqrt(multiplication), 2)
print("\nThe square root of", multiplication, "is", sq_root)
 
# step 13
currentMonth = "October"
currentDay = 25
 
# step 14
print(f"\n\t\t Today is day {currentDay} of the month of {currentMonth}")
