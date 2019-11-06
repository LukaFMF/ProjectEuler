#Dave is doing his homework on the balcony and, preparing a presentation 
#about Pythagorean triangles, has just cut out a triangle with side 
#lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind 
#blows the triangle down into the garden. Another gust blows a small 
#ant straight onto this triangle. The poor ant is completely disoriented 
#and starts to crawl straight ahead in random direction in order to get 
#back into the grass.
#
#Assuming that all possible positions of the ant within the triangle 
#and all possible directions of moving on are equiprobable, what is the 
#probability that the ant leaves the triangle along its longest side?
#Give your answer rounded to 10 digits after the decimal point.

import math,random

dolzinaA = 3
dolzinaB = 4
dolzinaC = 5

#tocke v koordinatnem sistemu
tockaA= (0,dolzinaA)
tockaB = (dolzinaB,0)
tockaC = (0,0)

alpha = math.asin(dolzinaA/dolzinaC)
beta = math.asin(dolzinaB/dolzinaC)
gamma = math.pi/2 #pravi kot, nasproti hipotenuzi

stevilo_ponovitev = 10
stevec = 0
verjetnost = 0
while stevec < stevilo_ponovitev:
    kotC = oklepajociKot(tockaA,tockaB,tockaC)
    verjetnost += kotC/2*math.pi
    stevec += 1

verjetnost = round(verjetnost/stevilo_ponovitev,10)
print(verjetnost)


def oklepajociKot(tockaA,tockaB,tockaC):
    ''' Vrne kot z vrhom v nakljucni tocki znotraj trikotnika, katerega nasprotna stranice je hipotenuza trikotnika ''' 
    nakljucniX = random.uniform(0,1) * tockaA[1] #nakljucna koordinata na stranici b 
    maxYvTockiX = -(tockaA[1]/tockaB[0]) * nakljucniX + tockaA[1] #enacba premice skozi tocki A in B v katero vstavimo x 
    nakljucniY = random.uniform(0,1) * maxYvTockiX #nakljucna koordinata na stranici a, ki pa je znotraj trikotnika 

    nakljucnaTocka = nakljucniX,nakljucniY #sestavimo tocko
