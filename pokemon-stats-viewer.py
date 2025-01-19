import requests

print('\nType "exit" to leave')
while True:
    user_input = input("\nEnter the name of a pokemon to search for: ")

    user_input = user_input.lower()

    if user_input == "exit":
        break

    req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{user_input}/')

    if req.status_code == 404:
        print(f"There is no pokemon with the name {user_input}")
        break

    pokemon = req.json()

    print(f"Name: {pokemon['name'].capitalize()}")

    print("Stats:")
    for stat in pokemon['stats']:
        print(f"\t {stat['stat']['name'].capitalize()}: {stat['base_stat']} points.")


    print(f'Weight: {pokemon['weight']}')

    counter = 1
    print("Abilities:")
    for ability in pokemon['abilities']:
        print(f"\t{counter}. {ability['ability']['name'].capitalize()} - ", end='')

        url = ability['ability']['url']

        ab_req = requests.get(url)

        ability_info = ab_req.json()

        for ability_description in ability_info['effect_entries']:
            if ability_description['language']['name'] == 'en':
                effect = ability_description['effect'].replace('\n', ' ')
                print(effect)
        
        counter += 1

    
    user_input = input("\nDo u want to continue (y/n)? \n")
    while user_input[0] != 'y' and user_input[0] != 'n':
        print("Please, choose a correct answer")
    
    if user_input[0] == 'n':
        break
