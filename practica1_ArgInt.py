from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/usuario/<int:id>')
def bienvenido(id):
    return 'Bienvenido '+ id

if __name__ == '__main__':
    app.run()
