import numpy as np

m = np.zeros((9,9), dtype = int)

i = 0
j = 0

f = open("sud1.txt", 'r')
while True:

    i = 0
    while True:
        char = f.read(1)
        try:
            m[j, i] = int(char)
        except ValueError:
            break
        i = i+1
    j = j+1
    if not char:
        break

f.close()

f = open("sud1_sol.txt", 'w')
z = 1

while z>0:
    z = 0
    for i in range(0,9):
        for j in range(0,9):
            #raggiunto il numero, controllo se è uno 0
            if m[i,j] == 0:
                z = z+1
                #provo tutti i numeri
                counter = 0
                for n in range(1,10):
                    #parto positivo
                    check = True
                    #check della riga
                    for l in range(0,9):
                        if m[i,l] == n:
                            check = False
                            
                    #check della colonna
                    for l in range(0,9):
                        if m[l,j] == n:
                            check = False
                            
                    #check del quadrato
                    #riga e colonna del quadrato
                    r = i//3
                    r = 3*r
                    c = j//3
                    c = 3*c
                    for l in range(r,r+3):
                        for k in range(c,c+3):
                            if m[l,k] == n:
                                check = False
                                
                    #se è ancora positivo, salva e aggiorna il counter
                    if check:
                        num = n
                        counter = counter + 1

                if (check) and (counter == 1):
                    m[i,j] = num

    if (i == 8) and (j == 8):
        i = 0
        j = 0
print(m)

for i in range(0,9):
    for j in range(0,9):
        f.write(str(m[i,j]))
    f.write("\n")

f.close()
