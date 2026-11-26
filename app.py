
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/investigacion')
def investigacion():
    return render_template('investigacion.html')

@app.route('/receta')
def receta():
    return render_template('receta.html')

@app.route('/envase')
def envase():
    return render_template('envase.html')

@app.route('/creditos')
def creditos():
    return render_template('creditos.html')

@app.route('/promocion')
def promocion():
    return render_template('promocion.html')

if __name__ == '__main__':
    app.run(debug=True)
