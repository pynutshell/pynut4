# run this server using the command "flask --app flask_example run"

import datetime, flask

app = flask.Flask(__name__)

# secret key for cryptographic components such as encoding session cookies
# for production use, use secrets.token_bytes()
app.secret_key = b'\xc5\x8f\xbc\xa2\x1d\xeb\xb3\x94;:d\x03'


@app.route('/')
def greet():
    lastvisit = flask.session.get('lastvisit')
    now = datetime.datetime.now()
    newvisit = now.ctime()
    template = '''
      <html><head><title>Hello, visitor!</title>
      </head><body>
      {% if lastvisit %}
        <p>Welcome back to this site!</p>
        <p>You last visited on {{lastvisit}} UTC</p>
        <p>This visit on {{newvisit}} UTC</p>
      {% else %}
        <p>Welcome to this site on your first visit!</p>
        <p>This visit on {{newvisit}} UTC</p>
        <p>Please Refresh the web page to proceed</p>
      {% endif %}
      </body></html>'''
    flask.session['lastvisit'] = newvisit
    return flask.render_template_string(
        template, newvisit=newvisit, lastvisit=lastvisit)


@app.after_request
def set_lastvisit(response):
    now = datetime.datetime.now()
    flask.session['lastvisit'] = now.ctime()
    return response

