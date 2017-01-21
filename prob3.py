# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number
#                   600851475143?

number = 600851475143

divisor = 2
while number != 1:
    if number % divisor == 0:
        number = number / divisor

    else:
        divisor = divisor + 1

print 'The largest prime factor is: ', divisor
