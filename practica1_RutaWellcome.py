from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/wellcome')
def bienvenido():
    return 'Bienvenido'

if __name__ == '__main__':
    app.run()
