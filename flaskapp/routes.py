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


def get_client():
    sess = request.cookies.get('session')
    client = None
    if sess in clients:
        client = clients[sess]
    else:
        clients[sess] = []
        client = clients[sess]
    return client


def update_physic(physic, val, right):
    if val == right:
        physic['history'].append([val, 'success'])
        physic['veracity'] += 1
    else:
        physic['history'].append([val, 'danger'])
        physic['veracity'] -= 1


@app.route("/", methods=['GET', 'POST'])
def home():
    form = PostForm()
    client = get_client()
    if form.validate_on_submit():
        pass
        client.append(form.number.data)
        for ind, val in enumerate(getRandomForPhysics()):
            update_physic(physics[ind], val, form.number.data)
    return render_template('index.html', physics=physics, client=client, form=form)
