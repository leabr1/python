an=input()
an2=input()
an3=input()
if an=="vertebrado":
    if an2=="ave":
        if an3=="carnivoro":
            print("aguia")
        else:
            print("pomba")
    elif an3=="onivoro":
        print("homem")
    else:
        print("vaca")
elif an2=="inseto":
    if an3=="hematofago":
        print("pulga")
    else:
        print("lagarta")
elif an3=="hematofago":
    print("sanguessuga")
else:
    print("minhoca")