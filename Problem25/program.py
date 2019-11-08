#The Fibonacci sequence is defined by the recurrence relation:
#
#    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#
#Hence the first 12 terms will be:
#
#    F1 = 1
#    F2 = 1
#    F3 = 2
#    F4 = 3
#    F5 = 5
#    F6 = 8
#    F7 = 13
#    F8 = 21
#    F9 = 34
#    F10 = 55
#    F11 = 89
#    F12 = 144
#
#The 12th term, F12, is the first term to contain three digits.
#
#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import math,time
prejsnja2 = 1 # vrednost zaporedja za n - 2
prejsnja1 = 1 # vrednost zaporedja za n - 1
trenutna = 2  # vrednost zaporedja za n
stev = 3
while int(math.log10(trenutna) + 1) < 1000: # izkaze se, da log10 vraca stevilo stevk -1, v desetiskem stevilu, 
    prejsnja2 = prejsnja1                   # ce odsekamo decimalni del in pristejemo 1 je rezultat tocen
    trenutna += prejsnja1
    prejsnja1 = trenutna - prejsnja2
    stev += 1
print(stev)