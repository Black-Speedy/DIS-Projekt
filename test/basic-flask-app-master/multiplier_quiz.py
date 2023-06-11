def get_defpokemon(cursor):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    defpokemon = "SELECT pokemon, sprite from pokemon ORDER BY RANDOM() LIMIT 1"

    cursor.execute(defpokemon)
    return cursor.fetchall()

def get_poke_and_move(cursor):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    poke_and_move = """SELECT *
                        FROM
                            (SELECT pokemon, sprite, move, moves.type as movetype
                            FROM pokemon natural join pokemonmove natural join moves 
                            WHERE source != 'egg move' and
                            source != 'Past generation only' and source != 'move tutor' and
                            source != 'event' and category != 'STATUS'
                            ORDER BY RANDOM() LIMIT 1) as a
                        NATURAL JOIN (SELECT pokemon, pokemontypes.type as poketype
			            FROM pokemontypes) as b"""
    cursor.execute(poke_and_move)
    return cursor.fetchall()

def get_type_relations(defpokemon, move, cursor):
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    type_relations = """SELECT relation
                        FROM
                            (SELECT deftype, atktype, relation
                             FROM pokemontypes FULL JOIN typerelations 
                             ON pokemontypes.type = typerelations.deftype
                             WHERE pokemontypes.pokemon = '%s') as a
                        NATURAL JOIN (SELECT type as atktype
                                      FROM moves
                                      WHERE move = '%s') as b""" %(defpokemon, move)
    cursor.execute(type_relations)
    return cursor.fetchall()

def get_type_sprite(type):
    if type == 'BUG':
        return "static/images/bugtype.png"
    elif type == 'DARK':
        return "static/images/darktype.png"
    elif type == 'DRAGON':
        return "static/images/dragontype.png"
    elif type == 'ELECTRIC':
        return "static/images/electrictype.png"
    elif type == 'FAIRY':
        return "static/images/fairytype.png"
    elif type == 'FIGHTING':
        return "static/images/fightingtype.png"
    elif type == 'FIRE':
        return "static/images/firetype.png"
    elif type == 'FLYING':
        return "static/images/flyingtype.png"
    elif type == 'GHOST':
        return "static/images/ghosttype.png"
    elif type == 'GRASS':
        return "static/images/grasstype.png"
    elif type == 'GROUND':
        return "static/images/groundtype.png"
    elif type == 'ICE':
        return "static/images/icetype.png"
    elif type == 'NORMAL':
        return "static/images/normaltype.png"
    elif type == 'POISON':
        return "static/images/poisontype.png"
    elif type == 'PSYCHIC':
        return "static/images/psychictype.png"
    elif type == 'ROCK':
        return "static/images/rocktype.png"
    elif type == 'STEEL':
        return "static/images/steeltype.png"
    elif type == 'WATER':
        return "static/images/watertype.png"
    else:
        return "static/images/notype.png"
        

def get_multi_quiz_question(cursor):

    defpokemon = get_defpokemon(cursor)
    poke_and_move = get_poke_and_move(cursor)
    defpoke = defpokemon[0]['pokemon']
    defpokesprite = defpokemon[0]['sprite']
    atkpoke = poke_and_move[0]['pokemon']
    atkpokesprite = poke_and_move[0]['sprite']
    move = poke_and_move[0]['move']
    movetype = poke_and_move[0]['movetype']
    type_relations = get_type_relations(defpoke, move, cursor)
    type_sprite = get_type_sprite(movetype)

    multiplier = 1
    for type in poke_and_move:
        if type['poketype'] == poke_and_move[0]['movetype']:
            multiplier = multiplier * 1.5
    for relation in type_relations:
        if relation[0] == 'weakness':
            multiplier = multiplier * 2
        elif relation[0] == 'resistance':
            multiplier = multiplier * 0.5
        elif relation[0] == 'immunity':
            multiplier = multiplier * 0
    
    return (atkpokesprite, defpokesprite, atkpoke, defpoke, move, type_sprite, movetype, multiplier)