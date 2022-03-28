import requests
from pprint import pprint


def getAllCharacters():
    response = requests.get("http://hp-api.herokuapp.com/api/characters")
    pprint(response.json()) 

def getInfHouse():
    url= "http://hp-api.herokuapp.com/api/characters/house/"
    house = input("Postacie z którego domu chcesz zobaczyć? ")
    url= url + house + "/"
    response = requests.get(url)
    pprint(response.json())

def riddle():
    print("Zgadnij kolor oczu wybranej postaci!")
    name=input("Podaj imię postaci, której kolor oczu chcesz zgadnąć: ")
    response = requests.get("http://hp-api.herokuapp.com/api/characters")
    list_of_characters= response.json()

    for character in list_of_characters:
        if character.get('name') == name:
            eye = character.get('eyeColour')
            eyeGuess= input('Jaki kolor oczu ma ' + name + ': ')
            if eyeGuess == eye:
                print('Brawo!')
            else: 
                print('Niestety nie, spróbuj jeszcze raz')

def listOfSpecies():
    list_species=[]
    response= requests.get("http://hp-api.herokuapp.com/api/characters")
    list_of_characters= response.json()
    for character in list_of_characters:
        list_species.append(character.get('species'))
        print(set(list_species))

    
while True:
    print('1. Zobacz informacje o wszytskich postaciach.')
    print('2. Informacje o postaciach z wybranego domu.')
    print('3. Zagadka.' )
    print('4. Zobacz listę gatunków.')
    print('0. Wyjdź')
    
    option=input("Podaj opcje: ")
    if option =='1':
        getAllCharacters()

    if option=='2':
        getInfHouse()

    elif option=='3':
        riddle()

    elif option=='4':
        listOfSpecies()

    elif option=='0':
        break