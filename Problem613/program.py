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

#neresen problem
import math,random

def oklepajociKot(tockaA,tockaB,tockaC):
    ''' Vrne kot z vrhom v nakljucni tocki znotraj trikotnika, katerega nasprotna stranice je hipotenuza trikotnika ''' 
    nakljucniX = random.uniform(0,1) * tockaA[1] #nakljucna koordinata na stranici b 
    maxYvTockiX = -(tockaA[1]/tockaB[0]) * nakljucniX + tockaA[1] #enacba premice skozi tocki A in B v katero vstavimo x 
    nakljucniY = random.uniform(0,1) * maxYvTockiX #nakljucna koordinata na stranici a, ki pa je znotraj trikotnika

    nakljucnaTockaT = (nakljucniX,nakljucniY) #sestavimo tocko
    vecTA = (tockaA[0] - nakljucnaTockaT[0],tockaA[1] - nakljucnaTockaT[1]) #vektor od T do A
    vecTB = (tockaB[0] - nakljucnaTockaT[0],tockaB[1] - nakljucnaTockaT[1]) #vektor od T do B

    skalarniProdTATB = vecTA[0]*vecTB[0] + vecTA[1]*vecTB[1] 
    normTA = math.sqrt(vecTA[0]**2 + vecTA[1]**2)
    notmTB = math.sqrt(vecTB[0]**2 + vecTB[1]**2)
    return math.acos(skalarniProdTATB/(normTA*notmTB)) #izpeljano iz definicije skalarnega produkta: a*b = |a|*|b|*cos(kotMedVektorjema)

dolzinaA = 3
dolzinaB = 4
dolzinaC = 5

#tocke v koordinatnem sistemu
tockaA= (0,dolzinaA)
tockaB = (dolzinaB,0)
tockaC = (0,0)

stevilo_ponovitev = 5*10e6
stevec = 0
stev2 = 0
verjetnost = 0
while stevec < stevilo_ponovitev:
    if stev2 > 10000:
        print(round(verjetnost/stevec,10))
        stev2 = 0
    kotC = oklepajociKot(tockaA,tockaB,tockaC)
    verjetnost += kotC/(2*math.pi)
    stevec += 1
    stev2 += 1

verjetnost = round(verjetnost/stevilo_ponovitev,10)
print(verjetnost)
