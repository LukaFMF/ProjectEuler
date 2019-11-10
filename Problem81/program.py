#In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
#by only moving to the right and down, is indicated in bold red and is equal to 2427.
#
#(131)  673   234   103    18
#(201) ( 96) (342)  965   150
# 630   803  (746) (422)  111
# 537   699   497  (121)  956
# 805   732   524  ( 37) (331)
#
#Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), 
#a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right 
#by only moving right and down.

#nedokoncana

def povprecje(tabela):
    return sum(tabela)/len(tabela)

matrika = []
datoteka = open("matrix.txt","r")

stev = 0
while stev < 80:
    matrika.append([int(i) for i in datoteka.readline().split(",")])
    stev += 1

vsota = trenutna = matrika[0][0]
vrstica = stolpec = 0
dolzinaPoti = 80

while vrstica < 79 or stolpec < 79:
    povpVert = povpHori = 2000000000000000
    if vrstica < 79:
        povpVert = povprecje([matrika[i][stolpec] for i in range(vrstica+1,min(vrstica+dolzinaPoti+1,80))])
    if stolpec < 79:    
        povpHori = povprecje([matrika[vrstica][i] for i in range(stolpec+1,min(stolpec+dolzinaPoti+1,80))])
    if povpHori < povpVert: # premik dol
        trenutna = matrika[vrstica][stolpec+1]
        stolpec += 1
    else: # premik desno
        trenutna = matrika[vrstica+1][stolpec]
        vrstica += 1
    print(trenutna)
    vsota += trenutna
print(vsota)

