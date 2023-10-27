# Flask Practica


## Introducción a la Aplicación Flask

En este proyecto, estamos desarrollando una aplicación web utilizando el framework Flask de Python. Flask es una herramienta versátil y potente para construir 
aplicaciones web ligeras y eficientes. Nuestra aplicación responderá a diferentes rutas y parámetros, brindando una experiencia personalizada a los usuarios.
Flask nos permite crear rutas y vistas flexibles, lo que facilita la implementación de diversas funcionalidades. Ya sea para crear un blog, una aplicación de
comercio electrónico o una plataforma de análisis de datos, Flask nos proporciona una base sólida.

## 2 Instalación de Flask

Flask es un framework de desarrollo web para Python que te permite crear aplicaciones web de manera rápida y sencilla

#### Paso 1: Verifica la instalación de Python

Asegúrate de tener Python 3.x instalado en tu sistema. Puedes verificarlo ejecutando en CMD:
```
CMD
python --version
```

#### Paso 2 (Opcional pero recomendado): Crea un entorno virtual

Es recomendable crear un entorno virtual para cada proyecto de Flask. Puedes crearlo con el comando:
```
CMD
python -m venv myenv
```

#### Paso 3 (Opcional pero recomendado): Activa el entorno virtual

Activa el entorno virtual con el comando adecuado para tu sistema:
- En Windows:
```
CMD
myenv\Scripts\activate
```

#### Paso 4: Instala Flask
Dentro del entorno virtual, instala Flask con el comando:
```
CMD
pip install flask
```

## Practica 

Crear un archivo .py para poder probarlo.

Ejemplo: 'Practica.py'

## Tenemos el siguiente codigo

```python
# Importar la clase Flask del módulo Flask
from flask import Flask

# Crear una instancia de la clase Flask y asignarla a la variable 'app'
app = Flask(__name__)

# Definir la ruta principal ('/') y la función asociada 'bienvenido'
@app.route('/')
def bienvenido():
    return 'Bienvenido'

# Verificar si el script se está ejecutando directamente y no importado
if __name__ == '__main__':
    # Ejecutar la aplicación Flask
    app.run()
```

Funcionamiento:

- `from flask import Flask`: Importa la clase `Flask` del módulo Flask.  
  Esto permite utilizar Flask para crear una aplicación web.

- `app = Flask(__name__)`: Crea una instancia de la clase `Flask` y la asigna a la variable `app`.  
  Esta instancia representa la aplicación Flask. El argumento `__name__` se refiere al nombre del módulo actual de Python.

- `@app.route('/')`: Define una ruta principal ('/') en la aplicación Flask.  
  Indica que la función que sigue es la que se ejecutará cuando alguien visite la ruta principal ('/') de la aplicación.

- `def bienvenido()`: Define una función llamada `bienvenido`.  
  Esta función se ejecutará cuando alguien acceda a la ruta principal ('/').

Este es el funcionamiento basico de la aplicacion, si buscamos el nuestro navegador usando `http://127.0.0.1:5000` nos dara el mensaje de "Bienvenido".

### Hagamos los siguientes cambios para nuestas variantes

Para entrar con otra ruta que no sea la raiz del localhost. 
Recuerde que cada que se hacen cambios se guardan y se vuelve a cargar el archivo por CMD para que se apliquen los cambios. 


```python
from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/wellcome')
def bienvenido():
    return 'Bienvenido'

if __name__ == '__main__':
    app.run()
```

Funcionamiento: 

Si nos metemos a `http://127.0.0.1:5000` no tendremos respuesta de bienvenida puesto que la ruta a la que intetamos accesder no se puede mostrar ya que no funciona con la raiz sino que con la ruta /wellcome, mientras que usamos `http://127.0.0.1:5000/wellcome` y da bienvenida.

### Con nombre el parametro 

```python
from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/wellcome/<name>')
def bienvenido(name):
    return 'Bienvenido '+ name

if __name__ == '__main__':
    app.run()

```

Funcionamiento: 

Cuando accedes a http:/127.0.0.1:5000/wellcome/Juan%20Perez, el valor "Juan%20Perez" se asigna a la variable <name>. Flask interpreta esto como un valor no nulo y lo pasa a la función. La función devuelve "Bienvenido Juan Perez" ya que toma el valor de <name> y lo concatena al mensaje.
La razon por la que no se puede acceder 

### Con diferentes tipos de datos para los parametros 

| Tipo de Dato | Descripción                                             | Ejemplo de Ruta                      |
|--------------|---------------------------------------------------------|--------------------------------------|
| int          | Captura un valor entero.                                | /usuario/<int:id>                   |
| float        | Captura un valor en punto flotante.                    | /precio/<float:valor>               |
| path         | Captura una cadena que puede incluir barras diagonales (útil para rutas). | /ruta/<path:segmento>   |
| string       | Este es el tipo de datos predeterminado y captura una cadena de caracteres. | /nombre/<string:nombre> |


Int:
```python
from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/usuario/<int:id>')
def bienvenido(id):
    return 'Bienvenido '+ id

if __name__ == '__main__':
    app.run()

```

Se ah definido una ruta /usuario/<int:id>. La variable id es capturada como un entero (int). Cuando alguien accede a la URL /usuario/123, el valor "123" se captura como un número entero y se pasa como argumento a la función. Luego, la función devuelve un mensaje que incluye ese valor. Por ejemplo, si visitas http:/127.0.0.1:5000/usuario/123, la respuesta será "Bienvenido 123".

Float:
```python
from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/precio/<float:valor>')
def bienvenido(valor):
    return f'precio {valor} $'

if __name__ == '__main__':
    app.run()

```

Se ah definido una ruta /precio/<float:valor>. La variable valor es capturada como un número en punto flotante (float). Cuando alguien accede a la URL /precio/3.14, el valor "3.14" se captura como un número de punto flotante y se pasa como argumento a la función. Luego, la función devuelve un mensaje que incluye ese valor. Por ejemplo, si visitas http:/127.0.0.1:5000/precio/3.14, la respuesta será "precio 3.14 $".

Path:
```python
from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/ruta/<path:segmento>')
def bienvenido(segmento):
    return f'Segmento capturado: {segmento}'

if __name__ == '__main__':
    app.run()

```

Se ah definido una ruta /ruta/<path:segmento>. La variable segmento es capturada como una cadena que puede incluir barras diagonales. Esto es útil cuando necesitas capturar una parte de la URL que puede contener múltiples segmentos. Cuando alguien accede a la URL /ruta/segmento/otro-segmento, el valor "segmento/otro-segmento" se captura como una cadena y se pasa como argumento a la función. Luego, la función devuelve un mensaje que incluye ese valor. Por ejemplo, si visitas http:/127.0.0.1:5000/ruta/segmento/otro-segmento, la respuesta será "Segmento capturado: segmento/otro-segmento".

String:
```python
from flask import Flask

# Crear una instancia de la clase Flask
app = Flask(__name__)

# Definir la ruta principal y la función asociada
@app.route('/nombre/<string:nombre>')
def mostrar_nombre(nombre):
    return f'Nombre capturado: {nombre}'

if __name__ == '__main__':
    app.run()

```

Se ah definido una ruta /nombre/<string:nombre>. La variable nombre es capturada como una cadena de caracteres (string). Cuando alguien accede a la URL /nombre/Juan, el valor "Juan" se captura como una cadena y se pasa como argumento a la función. Luego, la función devuelve un mensaje que incluye ese valor. Por ejemplo, si visitas http:/127.0.0.1:5000/nombre/Juan, la respuesta será "Nombre capturado: Juan".

## Usando numero de control

```python
from flask import Flask

app = Flask(__name__)

# Ruta con un parámetro de tipo entero
@app.route('/wellcome/<int:ncontrol>')
def wellcome(ncontrol):
    return f'Bienvenido,, con número de control: {ncontrol}'


if __name__ == '__main__':
    app.run()
```

/wellcome/<número-de-control>, la función asociada toma el valor proporcionado en la URL y lo utiliza para generar un mensaje de bienvenida personalizado. Por ejemplo, si alguien usa http://127.0.0.1:5000/wellcome/20490713, la aplicación mostrará el mensaje "Bienvenido, con número de control: 20490713". 
Utiliza el formato f para hacerlo mas presentable.
En este caso tenemos que si ponemos algun numero en particular se imprime pero de lo contrario una cadena de caracteres te dara un error en la pagina. 


Usar 2 parametros

```python

from flask import Flask

app = Flask(__name__)

# Ruta con un parámetro de tipo entero
@app.route('/wellcome/<name>/<int:ncontrol>')
def wellcome(name, ncontrol):
    return f'Bienvenido, {name}, con número de control: {ncontrol}'


if __name__ == '__main__':
    app.run()
```
Funcionamiento: 

Cuando alguien accede a una URL como http://127.0.0.1:5000/wellcome/Juan/12345, la función wellcome toma "Juan" como el valor del parámetro name y "12345" como el valor del parámetro ncontrol. Luego, se genera un mensaje de bienvenida que combina ambos valores en el formato "Bienvenido, Juan, con número de control: 12345".

Si solo se proporciona un parámetro en la URL, el código Flask que has proporcionado no funcionará tal como está definido. En ese caso, Flask intentará asignar el valor del parámetro proporcionado a la variable name, que se espera que sea el primer parámetro, y si no se proporciona un segundo valor, Flask generará un error.

## Sobrecarga de metodos 

```python
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
```


El código que has proporcionado utiliza la sobrecarga de métodos en Flask para manejar diferentes rutas y parámetros en una aplicación web. 

- `/wellcome/`: Esta ruta no espera ningún parámetro y devuelve un mensaje de bienvenida genérico.

- `/wellcome/<name>`: Esta ruta captura un parámetro `name`, que es una cadena de caracteres, y devuelve un mensaje de bienvenida personalizado con el nombre proporcionado.

- `/wellcome/<int:ncontrol>`: Esta ruta captura un parámetro `ncontrol`, que se espera que sea un número entero, y muestra un mensaje que indica que se ha recibido un número de control.

- `/wellcome/<name>/<int:ncontrol>`: Esta ruta captura dos parámetros, `name` y `ncontrol`, y muestra un mensaje de bienvenida personalizado que incluye tanto el nombre como el número de control.

Este enfoque permite crear rutas dinámicas y personalizadas en una aplicación Flask, lo que facilita la generación de respuestas adaptadas a diferentes situaciones y parámetros.


Posibles Errores:

Requiere manejo de excepciones: Si un usuario accede a una ruta con un tipo de parámetro diferente al esperado (por ejemplo, un texto en lugar de un número entero en una ruta que espera un número entero), Flask podría generar una excepción. Se debe considerar agregar manejo de excepciones para evitar que la aplicación se rompa en tales situaciones.





