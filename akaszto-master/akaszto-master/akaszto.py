import random
def beolvas(filenev):
    lista = []
    forrasfile = open(filenev,mode='r',encoding='UTF-8')
    for sor in forrasfile:
        lista.append(sor.strip())
    forrasfile.close()
    return lista

def feladvany(szo):
    return szo[0] + "." * (len(szo) - 2) + szo[-1]

def cserel(feladvany, szo, betu):
    eredmeny = szo[0]
    for i in range(1, len(szo)-1):
        if szo[i] == betu:
            eredmeny += betu
        else:
            eredmeny += feladvany[i]
    eredmeny += szo[-1]
    return eredmeny 



def keres(feladvany, lista):
    eredmeny=[]
    for helyseg in lista:
        if len(feladvany) == len(helyseg) and helyseg[0] == feladvany[0] and helyseg[-1] == feladvany[-1]:
            eredmeny.append(helyseg)
    return eredmeny

def betutipp(feladvany:str, helyseg):
    index = feladvany.index('.')
    return helyseg[index]

def ellenor(eredeti, uj, betu):
    if len(eredeti) != len(uj):
        return False
    for i in range(len(eredeti)):
        if eredeti[i] != uj[i]:
            if eredeti[i] != '.':
                return False
            else:
                if uj[i] != betu:
                    return False  
    return True

def kizar(lista, betu):
    eredmeny=[]
    for helyseg in lista:         
        if not betu in helyseg[1:-1]:
            eredmeny.append(helyseg)
    return eredmeny
  
def fh_gondol(helysegek):  
    print("Gondolj egy magyar telpülésre!")
    kiirando=input("Írd be a feladványt:")
    lehetsegesek = keres(kiirando, helysegek)
    #print(lehetsegesek)
    # while ciklus inkább, amíg több mint 1 lehetséges van!
    if len(lehetsegesek) == 0:
        print("Nincs ilyen település.")
    elif len(lehetsegesek) == 1:
        print(lehetsegesek[0], "a gondolt város.")
    else:
        print(lehetsegesek)
        
        


def main():
    helysegek = beolvas("helyek.txt")
    feladat = random.choice(helysegek)
    kiirando = feladvany(feladat)
    print(kiirando)
    proba = 6
    while "." in kiirando and proba > 0:
        betu = input("Adj meg egy betűt: ")
        if len(betu) > 1:
            if betu.lower() != feladat.lower():            
                proba = 0
            break

        if betu in feladat[1: -1]:
            kiirando = cserel(kiirando, feladat, betu)
        else:
            proba -= 1
            print("A hiányzó betű között nem található", proba, "tipped van még!")            
        print(kiirando)

    if proba > 0:
        print("Gratulálok!")
    else:
        print("A gondolt szó: ", feladat)


main()