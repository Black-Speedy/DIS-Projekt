from psycopg2.extras import DictCursor
import psycopg2
from flask import Flask, render_template, request
from multiplier_quiz import *
from stat_quiz import *

app = Flask(__name__)

count = 0
answers = []
correctAnswers = []
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
    global answers
    answers = []
    global correctAnswers
    correctAnswers = []
    return render_template('index.html', the_title='Pokemon Quiz')


@app.route('/multiquiz_startpage.html')
def multi_start():
    global count
    count = 0
    global answers
    answers = []
    global correctAnswers
    correctAnswers = []
    return render_template('mult_startpg.html')


@app.route('/results.html', methods=['POST'])
def results():
    global answers
    print("answers: ", answers)
    print(answers)
    global score
    score = calculate_score(answers, correctAnswers)
    return render_template('results.html', the_title='Results', answers=answers, correctAnswers=correctAnswers, score=score)


@app.route('/multi_quiz.html')
def multi_quiz():
    (sprite1, sprite2, pokemon1, pokemon2, move, type_sprite, movetype, multiplier) = get_quiz_questions("multi_quiz")
    global count
    global correctAnswers
    correctAnswers.append(float(multiplier))
    count = count + 1

    if count > 10:
        return results()
    else:
        return render_template('multi_quiz.html', count=count, sprite1=sprite1, sprite2=sprite2,
                               pokemon1=pokemon1, pokemon2=pokemon2, move=move, type_sprite=type_sprite, movetype=movetype, multiplier=multiplier)


@app.route('/stat_quiz.html')
def stat_quiz():
    (pokemon1, stat1, sprite1, pokemon2, stat2, sprite2, pokemon3, stat3, sprite3, pokemon4, stat4, sprite4, stat, answer) = get_quiz_questions("stat_quiz")
    global count
    global correctAnswers
    correctAnswers.append(int(answer))
    count = count + 1
    if count > 10:
        return results()
    else:
        return render_template('stat_quiz.html', count=count, pokemon1=pokemon1, pokemon2=pokemon2, pokemon3=pokemon3, pokemon4=pokemon4,
                                stat1=stat1, stat2=stat2, stat3=stat3, stat4=stat4, 
                                sprite1=sprite1, sprite2=sprite2, sprite3=sprite3, sprite4=sprite4, stat=stat, answer=answer)


def get_quiz_questions(quiz_type):

    if quiz_type == "multi_quiz":
        return get_multi_quiz_question(cursor)
    elif quiz_type == "stat_quiz":
        return get_stat_quiz_question(cursor)


def calculate_score(answers, correct_answers):
    score = 0
    for i in range(len(answers)):
        if answers[i] == correct_answers[i]:
            score = score + 1
    return score


@app.route('/get_answer', methods=['POST'])
def get_answer():
    x = request.form.get('answer')
    global answers
    answers.append(float(x))
    print(answers)
    return multi_quiz()
    

if __name__ == '__main__':
    app.run(debug=True)
