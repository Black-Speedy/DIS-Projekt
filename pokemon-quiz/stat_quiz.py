import random
def get_pokemon_stats(cursor):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    defpokemon = """SELECT pokemon, hp, attack, defence, spatk, spdef, speed, total, sprite
                    FROM pokemon
                    ORDER BY RANDOM() LIMIT 4"""

    cursor.execute(defpokemon)
    return cursor.fetchall()

def get_stat_quiz_question(cursor):

    pokemon_stats = get_pokemon_stats(cursor)

    ran_stat = random.randint(0,6)
    if ran_stat == 0:
        stat = 'hp'
    elif ran_stat == 1:
        stat = 'attack'
    elif ran_stat == 2:
        stat = 'defence'
    elif ran_stat == 3:
        stat = 'spatk'
    elif ran_stat == 4:
        stat = 'spdef'
    elif ran_stat == 5:
        stat = 'speed'
    elif ran_stat == 6:
        stat = 'total'

    stats = ()
    for index in range(4):
        stats = stats + (pokemon_stats[index]['pokemon'], pokemon_stats[index][stat], pokemon_stats[index]['sprite'])

    stats = stats + (stat, max(pokemon_stats[0][stat], pokemon_stats[1][stat], pokemon_stats[2][stat], pokemon_stats[3][stat]))

    return stats