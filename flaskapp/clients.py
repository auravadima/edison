from flask import session


def append_client_history(val):
    if 'history' in session:
        history = session['history']
        history.append(val)
        session['history'] = history
    else:
        session['history'] = [val]
