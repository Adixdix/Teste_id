def teste_ID(erreur = 0)-> str:
    dico = {"AH":"1983","LC":"1234"} 
    ID=str(input("id:"))
    if ID == "AH" and str(input("mot de passe:")) == dico[ID]:
        print("Binvenue Adam")
        return ID
    elif ID == "LC" and str(input("mot de passe:")) == "1234":
        print("Binvenue Lenny")
        return ID
    else:
        erreur = erreur + 1
        print("ID ou Mot de passe incorecte plus que",3-erreur,"tentative")
        if erreur == 3:
            print("trop d'erreur")
            return False
        else:
            teste_ID(erreur)




if teste_ID() == "AH":
    print("ok")