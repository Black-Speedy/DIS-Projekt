from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='Pokemon Quiz')

@app.route('/results.html')
def results():
    return render_template('results.html', the_title='results')

@app.route('/quizs.html')
def quiz():
    return render_template('quiz.html', the_title='Quiz!')

if __name__ == '__main__':
    app.run(debug=True)
