#If we list all the natural numbers below 10 that are multiples of
#3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

stevilo = 1
vsota = 0

while stevilo < 1000:
    if stevilo % 3 == 0 or stevilo % 5 == 0:    # ce je stevilo deljivo s 3 ali s 5 
        vsota += stevilo                        # ga pristejemo vsoti
    stevilo += 1
print(vsota) 