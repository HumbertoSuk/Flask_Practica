from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/')
@app.route('/wellcome/<name>')
@app.route('/wellcome/<int:ncontrol>')
@app.route('/wellcome/<name>/<int:ncontrol>')
def bienvenido(name=None, ncontrol=None):
    if name is None and ncontrol is None:
        return 'Bienvenido'
    elif name is not None and ncontrol is None:
        return f'Bienvenido, {name}'
    elif name is None and ncontrol is not None:
        return f'El número recibido es: {ncontrol}'
    else:
        return f'Bienvenido, {name}, tu número de control es: {ncontrol}'

if __name__ == '__main__':
    app.run()
