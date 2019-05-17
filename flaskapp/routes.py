from flask import render_template, session, redirect, url_for
from flaskapp.forms import PostForm, ReadyForm
from flaskapp import app
from flaskapp.physics import update_physic, get_physic_guess, clear_physic_guess, clear_clear_physics
from flaskapp.clients import append_client_history

physics = clear_clear_physics()


@app.route('/', methods=["GET", "POST"])
def home():
    postForm = PostForm()
    readyForm = ReadyForm()
    if postForm.validate_on_submit() and postForm.number.data:
        append_client_history(postForm.number.data)
        for ind, val in enumerate(session['guess']):
            update_physic(physics[ind], val, postForm.number.data)
        clear_physic_guess()
    elif readyForm.validate_on_submit():
        get_physic_guess()
    return render_template('index.html', physics=physics, readyForm=readyForm, postForm=postForm)


@app.route('/clear')
def clear():
    global physics
    physics = clear_clear_physics()
    return redirect(url_for('home'))
