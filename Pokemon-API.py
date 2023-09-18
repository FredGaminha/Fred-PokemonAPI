import requests as r

def PokeAPI_pokemon():
    print("You want to know basic info about one pokemon")
    pokeName = input("Type your pokemon > ")

    pokeURL = "https://pokeapi.co/api/v2/pokemon/" + pokeName.lower()
    response = r.request("GET", pokeURL)

    if response.status_code == 200:
        repository = response.json()

        print("Pokemon Found! Let's show some info...")
        print("Name:", repository['name'])
        print("Height:", repository['height'], ' | ', "Weight:", repository['weight'])

        print("Type:")
        for a in repository["types"]:
            types = a["type"]['name']
            print(f'- {types}')
            #print(types, end = ' ')
        
        print("Abilities:")
        
        for i in repository["abilities"]:
            abilities = i["ability"]["name"]
            abilityURL = "https://pokeapi.co/api/v2/ability/" + i["ability"]["name"]
            responseAbility = r.request("GET", abilityURL)

            if response.status_code == 200:
                abilityRep = responseAbility.json()

                for x in abilityRep["names"]:
                    if x["language"]["name"] == "en":
                        for z in abilityRep["effect_entries"]:
                            if z["language"]["name"] == "en":
                                print(x["name"], ": ", z["short_effect"])

                        

        """
        for i in repository["abilities"]:
            abilities = i["ability"]['name']
            abilityURL = "https://pokeapi.co/api/v2/ability/" + i["ability"]["name"]
            responseAbility = r.request("GET", abilityURL)
            abilityRep = responseAbility.json()
            
            for ab in abilityRep["effect_entries"]:
                if ab["language"]["name"] == "en":
                    abilityEffect = ab['effect_entries']['short_effect']
                    print(f'- {abilities}: {abilityEffect}')
        """
            
            #print(abilityRep['effect_entries'][1]['short_effect'])

        print("You want to search for another pokemon?")
        print("[1] - Yes | [2] - No")
        
        choice = int(input("Select > "))

        if (choice == 1):
            PokeAPI_pokemon()
        elif (choice == 2):
            chooseOption()

    else:
        print("Something went wrong...")
        print(response.status_code)

    return

def PokeAPI_move():
    print("You want to know basic info about one move")
    moveName = input("Type your move > ")

    moveURL = "https://pokeapi.co/api/v2/move/" + moveName.lower()
    response = r.request("GET", moveURL)
	
    if response.status_code == 200:
        repository = response.json()
		
        print("Move Found! Let's show some info...")

        for i in repository["names"]:
            if i["language"]["name"] == "en":
                print("Name: ", i["name"], " | ", "PP:", repository['pp'], " | ", "Power:", repository['power'])

        print("Description:", repository['effect_entries'][0]['short_effect'])
        print("Class:", repository["damage_class"]['name'], ' | ', "Type:", repository["type"]['name'])
		
        print(f'You want to see which pokemon can learn {repository["name"]}?')
        print("[1] - Yes | [2] - No")

        seeMoves = int(input("Select > "))

        if seeMoves == 1:
            print("===================================")
            print("This move can be learned to:")
            
            for i in repository["learned_by_pokemon"]:
                moveLearn = i['name']
                print(f'- {moveLearn}')

        print("You want to search for another move?")
        print("[1] - Yes | [2] - No")
        
        choice = int(input("Select > "))

        if (choice == 1):
            PokeAPI_move()
        elif (choice == 2):
            chooseOption()
	
    elif response.status_code == 404:
        print("Move not found... Did you type correctly?")
		
    else:
        print(response.status_code)
    
    return

def PokeAPI_ability():
    print("You want to know basic info about one ability")
    abilityName = input("Type your ability > ")

    abilityURL = "https://pokeapi.co/api/v2/ability/" + abilityName.lower()
    response = r.request("GET", abilityURL)

    if response.status_code == 200:
        repository = response.json() 

        print("Ability Found! Let's show some info...")

        for x in repository["names"]:
            if x["language"]["name"] == "en":
                print("Name: ", x["name"])

        print("Introduced on", repository['generation']['name'])

        for i in repository["effect_entries"]:
            if i["language"]["name"] == "en":
                print("Effect:", i["short_effect"])
    
        print("You want to search for another ability?")
        print("[1] - Yes | [2] - No")

        choice = int(input("Select > "))

        if(choice == 1):
            PokeAPI_ability()
        elif(choice == 2):
            chooseOption()
    return

def PokeAPI_item():
    print("You want to know about a item")
    itemName = input("Type your item > ")

    itemURL = "https://pokeapi.co/api/v2/item/" + itemName.lower()
    response = r.request("GET", itemURL)

    if response.status_code == 200:
        repository = response.json()

        for x in repository["names"]:
            if x["language"]["name"] == "en":
                print("Name:", x["name"], ' | ', "Category: ", repository['category']['name'])

        for i in repository["effect_entries"]:
            if i["language"]["name"] == "en":
                print(i['short_effect'])

        print("You want to find another item?")
        print("[1] - Yes | [2] - No")

        choice = int(input("Select > "))

        if choice == 1:
            PokeAPI_item()
        elif choice == 2:
            chooseOption()
        else:
            print("Invalid option. Abording program")

    elif response.status_code == 400:
        print("Item not found. Did you type correctly?")
        PokeAPI_item()

    else:
        print("Something went wrong, but i detect the error: ", response.status_code)

    return

def chooseOption():
    print("Choose a option from below:")
    print("1. Pokemon")
    print("2. Move")
    print("3. Ability")
    print("4. Item")
    print("5. Leave")

    choice = int(input("Select > "))

    if (choice == 1):
        PokeAPI_pokemon()
    elif (choice == 2):
        PokeAPI_move()
    elif (choice == 3):
        PokeAPI_ability()
    elif (choice == 4):
        PokeAPI_item()
    elif (choice == 5):
        print("Leaving")
    else:
        print("Option not found. Choose a option from 1 to 5")
        chooseOption()
    return

print("Welcome to the Pokemon API")
chooseOption()
