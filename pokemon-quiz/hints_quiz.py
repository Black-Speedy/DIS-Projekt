# Selects answer as a random pokémon
def get_ansPokemon(cursor):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    ansPokemon = "SELECT pokemon FROM pokemon-all ORDER BY RANDOM() LIMIT 1"
    cursor.execute(ansPokemon)
    return cursor.fetchall()

# Gets the evolution of a pokemon (empty if none were found)
def get_evo(cursor, pokemon):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    evo = "SELECT pokemon FROM pokemon-evolution-data WHERE pre_evolution = '%s'" %(pokemon)
    cursor.execute(evo)
    return cursor.fetchall()

# Gets a random ability of the given pokemon    
def get_ability(cursor, pokemon):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    ability = "SELECT ability FROM pokemonabilities WHERE pokemon='%s' ORDER BY RANDOM() LIMIT 1;" %(pokemon)
    cursor.execute(ability)
    return cursor.fetchall()

# Gets a random ability of the given pokemon    
def get_egggroup(cursor, pokemon):
    ability = "SELECT ability FROM pokemonabilities WHERE pokemon='%s' ORDER BY RANDOM() LIMIT 1;" %(pokemon)
    cursor.execute(ability)
    return cursor.fetchall()
