from app import app
from flask import render_template

@app.route('/')
def index():
    user_info = {
        'name':'Wayne Cass',
        'hobbies':['Youtube','Reading Books','Playing Clash of Clans'],
        'interested_books':{
            'Java':['Thinking in Java','Inside the Java virtual machine'],
            'Python':['Fluent Python']
        }
    }
    return render_template('index.html', user=user_info)
