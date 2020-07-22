x=input("adj meg egy szamot")
xI=int(x)
tomb=[]
tomb.append(xI)
atlag=0
while (x!="ennyi"):




    x=input("Adj meg egy ujabb szamot")
    if x=="ennyi":
        print("Max ertek a tombben: ")
        print(max(tomb))
        print("Minimum ertek a tombben: ")
        print(min(tomb))
        for i in range(0,len(tomb)):
            atlag+=tomb[i]
        
        print("A szamok atlaga:")
        print(atlag/len(tomb))
    else:
        xI=int(x)
        tomb.append(xI)
        print(tomb)



#print(tomb)
