import random 
# Selects answer as a random pokémon
def get_ansPokemon(cursor):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    ansPokemon = "SELECT pokemon, sprite FROM pokemon ORDER BY RANDOM() LIMIT 1"
    cursor.execute(ansPokemon)
    return cursor.fetchall()

# Gets the evolution method of a pokemon (empty if no evolution was found)
def get_evo_method(cursor, pokemon):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    evo_method = "SELECT method FROM evolutiondata WHERE pre_evolution = '%s'" %(pokemon)
    cursor.execute(evo_method)
    return cursor.fetchall()

# Gets a random ability of the given pokemon    
def get_ability(cursor, pokemon):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    ability = "SELECT ability FROM pokemonabilities WHERE pokemon='%s' ORDER BY RANDOM() LIMIT 1;" %(pokemon)
    cursor.execute(ability)
    return cursor.fetchall()

# Gets a random egg group of the given pokemon    
def get_egggroup(cursor, pokemon):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    egg = "SELECT egg_group FROM eggdata WHERE pokemon='%s' ORDER BY RANDOM() LIMIT 1;" %(pokemon)
    cursor.execute(egg)
    return cursor.fetchall()

# Gets a the stat with the highest value of the given pokemon    
def get_highest_stat(cursor, pokemon):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    statsq = "SELECT hp, attack, defence, spatk, spdef, speed FROM pokemon WHERE pokemon='%s'" %(pokemon)

    cursor.execute(statsq)
    return cursor.fetchall()

# Gets an incorrect answer that does not share both ability and egg group as the input values, but shares whether it is able to evolve.
def get_incorrect(cursor, evolves, ability, egg):
    if (evolves != "it does not evolve"):
        choice = """WITH choices AS (SELECT pokemon, sprite, ability, egg_group
                        FROM pokemon NATURAL JOIN pokemonabilities NATURAL JOIN eggdata)

                    SELECT pokemon, sprite FROM choices
                    WHERE NOT (ability = '%s' AND egg_group = '%s')
                    AND pokemon IN (SELECT pre_evolution FROM evolutiondata)
                    ORDER BY RANDOM() LIMIT 5;""" %(ability, egg)
    if (evolves == "it does not evolve"):
        choice = """WITH choices AS (SELECT pokemon, sprite, ability, egg_group
                        FROM pokemon NATURAL JOIN pokemonabilities NATURAL JOIN eggdata)

                    SELECT pokemon, sprite FROM choices
                    WHERE NOT (ability = '%s' AND egg_group = '%s')
                    AND pokemon NOT IN (SELECT pre_evolution FROM evolutiondata)
                    ORDER BY RANDOM() LIMIT 5;""" %(ability, egg)
        
    cursor.execute(choice)
    return cursor.fetchall() 


def get_hints_quiz_question(cursor):
    ansPokemon = get_ansPokemon(cursor)
    ansPokemon_name = ansPokemon[0]['pokemon']
    ansPokemon_sprite = ansPokemon[0]['sprite']
    evo_method = get_evo_method(cursor, ansPokemon_name)
    if evo_method == []:
        evo_method = "it does not evolve"
    else:
        evo_method = "the evolution method is: " + str(evo_method[0][0])

    ability = get_ability(cursor, ansPokemon_name)[0][0]
    egggroup = get_egggroup(cursor, ansPokemon_name)[0][0]

    statq = get_highest_stat(cursor, ansPokemon_name)
    highest_stat = statq[0].index(max(statq[0]))
    if highest_stat == 0:
        highest_stat = "hp"
    elif highest_stat == 1:
        highest_stat = "attack"
    elif highest_stat == 2:
        highest_stat = "defence"
    elif highest_stat == 3:
        highest_stat = "spatk"
    elif highest_stat == 4:
        highest_stat = "spdef"
    elif highest_stat == 5:
        highest_stat = "speed"

    answer = random.randint(1,4)
    wrong_answer = get_wrong_answer(cursor, evo_method, ability, egggroup)
    print(wrong_answer) 
    quiz_elements = ()
    for i in ([1, 2, 3, 4]):
        if i == answer:
            quiz_elements = quiz_elements + (ansPokemon_name, ansPokemon_sprite)
        else:
            quiz_elements = quiz_elements + (wrong_answer[i]['pokemon'], wrong_answer[i]['sprite'])

    quiz_elements = quiz_elements + (evo_method, ability, egggroup, highest_stat, answer)         
    
    return quiz_elements
        
def get_wrong_answer(cursor, evolves, ability, egg):
    wrong = get_incorrect(cursor, evolves, ability, egg)
    return wrong
    

    
    
    

    