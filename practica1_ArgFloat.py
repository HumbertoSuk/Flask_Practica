from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/precio/<float:valor>')
def bienvenido(valor):
    return f'precio {valor} $'

if __name__ == '__main__':
    app.run()
