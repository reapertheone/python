import random

def gameplay():
    
    number = random.randint(0,100)
    NString=str(number)
    print(number)
    guess=''
    tippek=[]
    while guess!=NString:

        
       # for x in tippek:
        print(tippek)

        guess=input('Tipped: ')
        if guess!=NString:
            if int(guess)<number:
                print('Tul alacsony')
                tippek.append(u"\u2193"+guess)
            else:
                print('Tul magas')
                tippek.append(u"\u2191"+guess)
    else:
        x=len(tippek)
        z=str(x)
        print('Kitalaltad '+z+' probalkozasbol')
        play=input('Uj jatek?\nigen/nem\n')
        if play=='igen':
            gameplay()

    
        


play=input('szeretnel jatszani?\n igen/nem\n')
if play=='igen' :
    print("Jatszol")
    gameplay()
else :
    print('Nem jatszol')
