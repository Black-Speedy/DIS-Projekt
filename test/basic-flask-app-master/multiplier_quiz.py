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