# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
currentNum = 0
while(currentNum < 1000):
    if currentNum % 3 == 0 or currentNum % 5==0:
        sum = sum + currentNum
    currentNum = currentNum + 1
print 'The sum of all the multiples of 3 or 5 below 1000 is:', sum
