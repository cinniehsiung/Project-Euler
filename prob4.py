# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is:
#                           9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindrome = 0;
firstNum = 100;

while firstNum < 1000:
    secondNum = firstNum

    while secondNum < 1000:
        product = firstNum * secondNum
        productArray = map(int, str(product))
        productArray2 = list(reversed(productArray));

        if productArray == productArray2:
            if product > palindrome:
                palindrome = product

        secondNum = secondNum + 1

    firstNum = firstNum + 1

print 'The largest palindrome is: ', palindrome
