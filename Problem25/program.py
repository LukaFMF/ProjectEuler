import math 
prejsnja1 = 0
prejsnja2 = 0
trenutna = 1
stev = 0
while int(math.log10(trenutna) + 1) < 1000:
    if stev == 0 or stev == 1:
        trenutna = 1
    else:  
        trenutna = prejsnja1 + prejsnja2
    prejsnja2 = prejsnja1
    prejsnja1 = trenutna
    stev += 1
print(stev)