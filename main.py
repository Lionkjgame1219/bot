import webbrowser
import os
from datetime import datetime
import subprocess

def juan():
    print("""   1-création d'un dossier\n
    2-supprimer un dossier\n
    3-ouvre un fichier\n
    4-Youtube\n
    5-google\n
    6-création d'un fichier\n
    7-suppression d'un fichier\n
    8-renommer un fichier\n
    9-creation d'un dossier sur le bureau\n
    10-suppresion d'un dossier dans le bureau\n
    11-recherche internet le .(votre référence) est imperatif!\n
    12-Supprimer le dossier avec le répertoire que vous-voulez\n
    13-quitter le programmer\n
    h or help for more info\n""")

    for choix in range(50):
        choix = input("Enter a number: ")

        if choix == "1":
            create_folder()

        if choix == "2":
            suppression()

        if choix == "3":
            ouvrir_unfile()

        if choix == "4":
            youtube()

        if choix == "5":
            google()

        if choix == "6":
            file_create()

        if choix == "7":
            suprimer_fichier()

        if choix == "8":
            rename()

        if choix == "9":
            bureau()

        if choix == "10":
            bureau_sup()

        if choix == "11":
            url3()

        if choix == "13" or  choix == 'cls':
            break

        if choix == "math":
            math()

        if choix == 'year':
            print("2021")

        if choix == 'date':
            print(datetime.now())


        if choix == 'h' or choix == 'help':
            print("math\nyear\ndate\nmeteo\nnews\n")

        if choix == 'meteo':
            meteo()

        if choix == '20 minute' or choix == 'news':
            info()

        if choix == '12':
            suppficher()


def create_folder():
    creation = input("Nom du dossier: ")
    folder = os.mkdir(creation)
    print(f"Le dossier {creation} à bien été crée")


def suppression():
    suppresionn = input("Nom du dossier à effacé: ")
    supprimer = os.rmdir(suppresionn)
    print(f"Le dossier {suppresionn} à bien été effacé ")

def ouvrir_unfile():
    ouvrir = input("Fichier à ouvrir: ")
    ouvrir_un_fichier = open(f"{ouvrir}", "w")
    ecrire = input("Ecrivez quelque chose: ")
    ouvrir_un_fichier.write(ecrire)
    ouvrir_un_fichier.close()

def file_create():
    create = input("Fichier à crée: ")
    create_file = open(f"{create}", "w+")
    print(f"Le fichier {create} à bien été crée!")


def google():
    url = webbrowser.open_new("https://google.com")

def youtube():
    url2 = webbrowser.open("https://youtube.com")

def suprimer_fichier():

    supp = input("Fichier à supprimer: ")
    print("Etes vous sur de vouloir supprimer le fichier {}".format(supp))
    suppr = input("Y or N")

    if suppr == 'Y' and suppr == 'y':
        suprimmer_fichier = os.remove(supp)
        print(f"Le fichier {supp} à bien été supprimer!")
    else:
        print("Suppression annulée!")

def rename():
    fichier_rename = input("fichier à renommer: ")
    fichier_rename2 = input("Renommer: ")
    fichier_rename3 = os.rename(f"{fichier_rename}", f"{fichier_rename2}")

def bureau():
    dosiier = input("Nom du dossier: ")
    file_bureau = os.mkdir(f'/Users/lionkjgame/Desktop/{dosiier}')
    print(f"Dossier {dosiier} à bien été crée")

def bureau_sup():
    dosiiier = input("Dossier à supprimer: ")
    file_supp = os.rmdir(f'/Users/lionkjgame/Desktop/{dosiiier}')
    print("Le dossier à bien été supprimer")

def url3():
    fun = input("Nom de votre recherche: ")
    url3_url = webbrowser.open_new(f"https://{fun}/")

def math():
    for nombre in range (3):
        nombre = int(input("Ecrivez un nombre:"))
        nombre2 = input("Ecrivez la syntaxe")
        nombre3 = int(input("Ecrivez un nombre"))
        syntaxe = ["/", "+", "x", "-", "^", "cls"]

        if nombre2 == syntaxe[0]:
            n = nombre / nombre3
            print(f"Le resultat est de: {n}\n ")

        if nombre2 == syntaxe[1]:
            nombre_quatre  = nombre+nombre3
            print(f"resultat: {nombre_quatre}\n")

        if nombre2 == syntaxe[2]:
            calcul = nombre*nombre3
            print(f"resultat: {calcul}\n ")

        if nombre2 == syntaxe[3]:
            calcul2 = nombre-nombre3
            print(f"resultat: {calcul2}\n")

        if nombre2 == syntaxe[4]:
            calculpuissance = nombre**nombre3
            print(f"resultat: {calculpuissance}\n")

        if nombre2 == syntaxe[5]:
            break

def meteo():
    import requests
    import json
    import datetime

    #récupération de la ville choisie par l'utilisateur
    print("Entrez la ville dont vous voulez connaitre la meteo en indiquant son pays : Paris,fr Londres,uk...")
    ville = input("De quelle ville voulez vous connaitre la meteo ?:  ")

    #récupère le temps actuel
    url_weather = "http://api.openweathermap.org/data/2.5/weather?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
    #url="http://api.openweathermap.org/data/2.5/weather?q=Londres,uk&APPID=beb97c1ce62559bba4e81e28de8be095"

    r_weather = requests.get(url_weather)
    data = r_weather.json()
    #print(data)

    print("Vous êtes a " + ville)

    #temperature moyenne
    t = data['main']['temp']
    print("La temperature moyenne est de {} degres Celsius".format(t-273.15))
    #écart de température
    t_min = data['main']['temp_min']
    t_max = data['main']['temp_max']
    print("Les temperatures varient entre {}".format(t_min-273.15) + " a {} degres Celsius".format(t_max-273.15))
    #taux d'humidité
    humidite = data['main']['humidity']
    print("Taux d'humidite de {}".format(humidite) + "%")
    #état du ciel
    temps = data['weather'][0]['description']
    print("Conditions climatiques : {}".format(temps))


    #jour = input("De quel jour voulez vous la météo ?")
    #date = datetime.datetime(year=2017, month=5, day= jour)
    ville = input("De quelle ville voulez vous connaitre les previsions ?: ")
    url_forecast = "http://api.openweathermap.org/data/2.5/forecast?q="+ville+"&APPID=beb97c1ce62559bba4e81e28de8be095"
    r_forecast = requests.get(url_forecast)
    data = r_forecast.json()
    #print(data)

    for i in range (0,25):
        t = data['list'][i]['main']['temp']
        temps = data['list'][i]['weather'][0]['description']
        time = data['list'][i]['dt_txt']
        print("Previsions pour le {}".format(time))
        print("La temperature moyenne est de {} degres Celsius".format(t-273.15))
        print("Conditions climatiques : {}".format(temps))

def info():
    print("1-Réseaux Suisse\n2-Réseaux Français")
    reseau = input()
    if reseau == '1':
        print("1-20min\n2-Le matin\n3-RTS\n4-tdg")
    for info_choice in range(3):
        info_choice = input()

        if info_choice == '1':
            webbrowser.open_new("https://www.20min.ch/fr")

        if info_choice == '2':
            webbrowser.open_new('https://www.lematin.ch/')

        if info_choice == '3':
            webbrowser.open_new('https://www.rts.ch/info/suisse/')

        if info_choice == '4':
            webbrowser.open_new('https://www.tdg.ch/')

    if reseau == '2':
        print("1-france-24\n2-france info tv\n3-")
        for info_choice3 in range(4):
            info_choice3 = input()

            if info_choice3 == '1':
                webbrowser.open_new('https://www.france24.com/fr/')

            if info_choice3 == '2':
                webbrowser.open_new('https://www.francetvinfo.fr/')

            if info_choice3 == '3':
                webbrowser.open_new('https://www.lci.fr/')

            if info_choice3 == '4':
               webbrowser.open_new('https://www.leparisien.fr/')


def suppficher():
    suppfichier2 = input("Entrez le chemin de vôtre dossier>> ")
    suppfichier = os.rmdir(f"{suppfichier2}")
    print("Le dossier à bien été supprimer!")



juan()
