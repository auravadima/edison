from random import randint
from flask import render_template, request, make_response, url_for
from flaskapp.forms import PostForm
from flaskapp import app

physics = [
    {'name': "Первый экстрасенс",
     'history': [],
     'veracity': 0
     },
    {'name': "Первый экстрасенс",
     'history': [],
     'veracity': 0
     }
]

clients = {}


def getRandomForPhysics():
    answers = []
    for ph in physics:
        answers.append(randint(0, 5))
    return answers


@app.route("/", methods=['GET', 'POST'])
def home():
    sess = request.cookies.get('session')
    client = None
    form = PostForm()
    if sess in clients:
        client = clients[sess]
    else:
        clients[sess] = []
        client = clients[sess]

    if form.validate_on_submit():
        client.append(form.number.data)
        for ind, val in enumerate(getRandomForPhysics()):
            if val == form.number.data:
                physics[ind]['history'].append([val, 'success'])
                physics[ind]['veracity'] += 1
            else:
                physics[ind]['history'].append([val, 'danger'])
                physics[ind]['veracity'] -= 1

    return render_template('index.html', physics=physics, client=client, form=form)
