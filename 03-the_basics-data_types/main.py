import datetime

################################################################################
myNowVariable = datetime.datetime.now()
print(myNowVariable)

################################################################################
myNumber = 1337
myText = "Leet"

print(myNumber, myText)

################################################################################
# Simple Types
x = 10  # integer
y = '10'  # string
z = 13.37  # float

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

################################################################################
# List Types
student_grades = [9.1, 8.8, 7.5]

################################################################################
# Ranges
rangeList = list(range(1, 10))
print(rangeList)

rangeListWithStep = list(range(1, 10, 2))
print(rangeListWithStep)
