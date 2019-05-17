from random import randint
from flask import session

physics = [
    {'name': "Первый экстрасенс",
     'history': [],
     'veracity': 0
     },
    {'name': "Второй экстрасенс",
     'history': [],
     'veracity': 0
     }
]


def get_clear_physics():
    return [
        {'name': "Первый экстрасенс",
         'history': [],
         'veracity': 0
         },
        {'name': "Второй экстрасенс",
         'history': [],
         'veracity': 0
         }
    ]


def get_physic_guess():
    answers = []
    for ph in physics:
        answers.append(randint(0, 99))
    session['guess'] = answers


def clear_physic_guess():
    session['guess'] = []


def update_physic(physic, val, right):
    if val == right:
        physic['history'].append([val, 'success'])
        physic['veracity'] += 1
    else:
        physic['history'].append([val, 'danger'])
        physic['veracity'] -= 1
