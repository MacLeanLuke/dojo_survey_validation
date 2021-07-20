from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojos import Dojo


@app.route('/')
def index():
    # session.clear()
    return redirect('/dojos')


@app.route('/dojos')
def show_all_authors():
    # session.clear()
    return render_template('index.html')


@app.route('/dojo/create', methods=['POST'])
def create_dojos():
    if (Dojo.validate_employee(request.form)):
        print('survey form is good!')
        session['dojo'] = True
        session['survey'] = Dojo.create_dojo(request.form)
    else:
        print('employee form is not good.')
        return redirect('/')
    
    return redirect('/dojo')


@app.route('/dojo')
def author_info():
    if 'dojo' in session:
        data = {
            'id': session['survey']
        }
        results = Dojo.get_dojo_by_id(data)
        survey_data = {
            'id': results[0]['id'],
            'name': results[0]['name'],
            'location': results[0]['location'],
            'language': results[0]['language'],
            'comment': results[0]['comment']
        }
        dojo_survey = Dojo(survey_data)
        
        
    return render_template('generic.html', dojo_survey=dojo_survey)


# from flask_app.models.user import User
# @app.route('/register', methods=['POST'])
# def register():
#     if not User.validate_user(request.form):
#         # we redirect to the template with the form.
#         return redirect('/')
#     # ... do other things
#     return redirect('/dashboard')