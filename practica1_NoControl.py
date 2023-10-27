from flask import Flask

app = Flask(__name__)

# Ruta con un parámetro de tipo entero
@app.route('/wellcome/<name>/<int:ncontrol>')
def wellcome(name, ncontrol):
    return f'Bienvenido, {name}, con número de control: {ncontrol}'


if __name__ == '__main__':
    app.run()
