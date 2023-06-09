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
        return "https://archives.bulbagarden.net/media/upload/thumb/d/d1/BugIC_SV.png/180px-BugIC_SV.png"
    elif type == 'DARK':
        return "https://archives.bulbagarden.net/media/upload/thumb/3/30/DarkIC_SV.png/180px-DarkIC_SV.png"
    elif type == 'DRAGON':
        return "https://archives.bulbagarden.net/media/upload/thumb/7/7f/DragonIC_SV.png/180px-DragonIC_SV.png"
    elif type == 'ELECTRIC':
        return "https://archives.bulbagarden.net/media/upload/thumb/7/77/ElectricIC_SV.png/180px-ElectricIC_SV.png"
    elif type == 'FAIRY':
        return "https://archives.bulbagarden.net/media/upload/thumb/c/c6/FairyIC_SV.png/180px-FairyIC_SV.png"
    elif type == 'FIGHTING':
        return "https://archives.bulbagarden.net/media/upload/thumb/0/0f/FightingIC_SV.png/180px-FightingIC_SV.png"
    elif type == 'FIRE':
        return "https://archives.bulbagarden.net/media/upload/thumb/a/a2/FireIC_SV.png/180px-FireIC_SV.png"
    elif type == 'FLYING':
        return "https://archives.bulbagarden.net/media/upload/thumb/d/d7/FlyingIC_SV.png/180px-FlyingIC_SV.png"
    elif type == 'GHOST':
        return "https://archives.bulbagarden.net/media/upload/thumb/2/2c/GhostIC_SV.png/180px-GhostIC_SV.png"
    elif type == 'GRASS':
        return "https://archives.bulbagarden.net/media/upload/thumb/7/7b/GrassIC_SV.png/180px-GrassIC_SV.png"
    elif type == 'GROUND':
        return "https://archives.bulbagarden.net/media/upload/thumb/f/f8/GroundIC_SV.png/180px-GroundIC_SV.png"
    elif type == 'ICE':
        return "https://archives.bulbagarden.net/media/upload/thumb/1/13/IceIC_SV.png/180px-IceIC_SV.png"
    elif type == 'NORMAL':
        return "https://archives.bulbagarden.net/media/upload/thumb/0/08/NormalIC_SV.png/180px-NormalIC_SV.png"
    elif type == 'POISON':
        return "https://archives.bulbagarden.net/media/upload/thumb/9/9d/PoisonIC_SV.png/180px-PoisonIC_SV.png"
    elif type == 'PSYCHIC':
        return "https://archives.bulbagarden.net/media/upload/thumb/9/96/PsychicIC_SV.png/180px-PsychicIC_SV.png"
    elif type == 'ROCK':
        return "https://archives.bulbagarden.net/media/upload/thumb/3/32/RockIC_SV.png/180px-RockIC_SV.png"
    elif type == 'STEEL':
        return "https://archives.bulbagarden.net/media/upload/thumb/b/b8/SteelIC_SV.png/180px-SteelIC_SV.png"
    elif type == 'WATER':
        return "https://archives.bulbagarden.net/media/upload/thumb/d/de/WaterIC_SV.png/180px-WaterIC_SV.png"
    else:
        return "https://archives.bulbagarden.net/media/upload/thumb/f/f8/UnknownIC_SV.png/180px-UnknownIC_SV.png"
        