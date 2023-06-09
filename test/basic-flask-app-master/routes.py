from psycopg2.extras import DictCursor
import psycopg2
from flask import Flask, render_template, request
from multiplier_quiz import *

app = Flask(__name__)

count = 0
answers = {}
score = 0

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="0301"
)

cursor = conn.cursor(cursor_factory=DictCursor)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    global count
    count = 0
    return render_template('index.html', the_title='Pokemon Quiz')


@app.route('/results.html', methods=['POST'])
def results():
    # Retrieve the submitted answers from the form
    answers = {key: request.form.get(key) for key in request.form}

    # Retrieve the correct answers from the database
    correct_answers = get_correct_answers()

    # Calculate the score
    score = calculate_score(answers, correct_answers)

    return render_template('results.html', the_title='Results', score=score)

@app.route('/quizs.html')
def quiz():
    (sprite1, sprite2, pokemon1, pokemon2, move, movetype, multiplier) = get_quiz_questions()
    global count
    count = count + 1
    if count > 10:
        return render_template('results.html', the_title='Results', score=score)
    else:
        return render_template('quiz.html', the_title='Quiz!', count=count, sprite1=sprite1, sprite2=sprite2,
                               pokemon1=pokemon1, pokemon2=pokemon2, move=move, movetype=movetype, multiplier=multiplier)

    

def get_quiz_questions():
    """ with open('path/to/quiz_questions.sql', 'r') as file:
        query = file.read() """
    query = "SELECT * FROM pokemon ORDER BY RANDOM() LIMIT 2;"  

    defpokemon = get_defpokemon(cursor)
    poke_and_move = get_poke_and_move(cursor)
    defpoke = defpokemon[0]['pokemon']
    defpokesprite = defpokemon[0]['sprite']
    atkpoke = poke_and_move[0]['pokemon']
    atkpokesprite = poke_and_move[0]['sprite']
    move = poke_and_move[0]['move']
    movetype = poke_and_move[0]['movetype']
    type_relations = get_type_relations(defpoke, move, cursor)

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
    
    return (atkpokesprite, defpokesprite, atkpoke, defpoke, move, movetype, multiplier)



@app.route('/update-variable', methods=['POST'])
def update_variable():
    answer = request.form.get('answer')
    # Update global variables or perform logic based on the 'answer' value

    return 'Variable updated'  # Or any other response you want

def calculate_score(answers, correct_answers):
    score = 0
    for key in answers:
        if answers[key] == correct_answers[key]:
            score += 1
    return score


def get_correct_answers():
    return True

# rendering the HTML page which has the button


@app.route('/json')
def json():
    return render_template('json.html')

# background process happening without any refreshing


@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return ("nothing")

if __name__ == '__main__':
    app.run(debug=True)
