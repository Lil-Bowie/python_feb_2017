from flask import *
app = Flask(__name__)

@app.route('/homepage')
def fhomepage():
    #do something
    return render_template('index.html', name='Bryson')
@app.route('/ninjas')
def fninjas():
    return render_template('ninjas.html')
    #do something
@app.route('/dojos/new')
def fdojo():
    return render_template('dojos.html')
    #do something
app.run(debug=True)
