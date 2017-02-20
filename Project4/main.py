from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

app = Flask(__name__)

config = dict(
    DEBUG = False,
    SECRET_KEY = 'dev'
)

app.config.update(config)

@app.route('/')
@app.route('/index')
def index():
    #TODO query database to send entries to template
    return render_template('index.html')

@app.route('/find', methods=['POST'])
def get_location_data():
    #This will be used to access the API files etc
    flash('Operation succeeded!')

    return redirect(url_for('index'))

def get_keys():
    '''Retrieve API keys from the keys file'''
    keys = []
    with open('keys.txt', 'r') as f:
        for line in f:
            keys.append(line[:len(line - 1)])
    return keys
