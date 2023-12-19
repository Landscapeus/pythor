print("Witaj w kalkulatorze objętości brył!")#what is wrong with deepl
aeiou=0
while (aeiou==0):
    print("Wybierz bryłę, której chcesz obliczyć objętość. \n1 = sześcian\n2 = prostopadłościan\n3 = graniastosłup\n4 = ostrosłup\n5 = walec\n6 = stożek\n7 = kula")
    weed=int(input())
    if weed==1:
        bokniejeden=int(input("Podaj długość krawędzi "))
        obj=bokniejeden**3
        print("Objętość sześcianu wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))#for some reason, when you put zero here it redirects you to
    elif weed==2:
        bokniejeden=int(input("Podaj długość krawędzi "))
        boksrodek=int(input("Podaj długość krawędzi "))
        boktre=int(input("Podaj długość krawędzi "))
        obj=bokniejeden*boktre*boksrodek
        print("Objętość prostopadłościanu wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))
    elif weed==3:
        bokniejeden=int(input("Podaj długość wysokości "))
        krawonc=int(input("Podaj pole podstawy "))
        obj=bokniejeden*krawonc
        print("Objętość graniastosłupa wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))
    elif weed==4:
        bokniejeden=int(input("Podaj długość wysokosci "))
        swaws=int(input("Podaj pole podstawy "))
        obj=bokniejeden*swaws*0.33
        print("Objętość ostrosłupa wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))
    elif weed==5:
        bokniejeden=int(input("Podaj długość wysokości "))
        r=int(input("Podaj długość promienia podstawy "))
        obj=3.14*r**2*bokniejeden
        print("Objętość walca wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))
    elif weed==6:
        bokniejeden=int(input("Podaj długość krawędzi "))
        kermit=int(input("Podaj długość promienia podstawy "))
        obj=bokniejeden*0.33*3.14*r**2
        print("Objętość stożka wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))
    elif weed==7:
        żabol=int(input("Podaj długość promienia kuli "))
        obj=żabol**3*1.33*3.14
        print("Objętość kuli wynosi ",obj)
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))
    else:
        print("Zły numer")#here, and I don't know why
        aeiou=int(input("By skorzystać z kalkulatora jescze raz, wpisz 0. By zakończyć akcję, wpisz 1. "))#nevermind elif exists and I forgot about it