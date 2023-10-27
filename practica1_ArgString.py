from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/nombre/<string:nombre>')
def mostrar_nombre(nombre):
    return f'Nombre capturado: {nombre}'

if __name__ == '__main__':
    app.run()
