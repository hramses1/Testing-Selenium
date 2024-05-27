# Automatización de Creación de Usuarios

Este proyecto automatiza el proceso de creación de usuarios en una aplicación web.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```
    git clone https://github.com/tu_usuario/automatizacion-creacion-usuarios.git
    ```

2. Entra al directorio del proyecto:

    ```
    cd automatizacion-creacion-usuarios
    ```

3. Crea un entorno virtual utilizando `virtualenv`. Si no tienes `virtualenv` instalado, puedes instalarlo usando pip:

    ```
    pip install virtualenv
    ```

    Luego, crea el entorno virtual:

    ```
    virtualenv -p python3 env
    ```

4. Activa el entorno virtual. En Windows, puedes hacerlo ejecutando:

    ```
    env\Scripts\activate
    ```

    En sistemas basados en Unix o MacOS, ejecuta:

    ```
    source env/bin/activate
    ```

5. Instala las dependencias del proyecto desde el archivo `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

6. Copia el archivo `.env.example` y renómbralo a `.env`. Luego, proporciona los valores necesarios para las variables de entorno.

7. Ejecuta el siguiente comando para correr la prueba de creación de usuarios:

    ```
    pytest -s tests/test_1_create_user.py > output.txt
    ```

## Estructura del Proyecto

📁 Creacion-usuarios
|   .env
|   .env.example
|   output.txt
|   requirements.txt
|   
📁 .pytest_cache
|   |   .gitignore
|   |   CACHEDIR.TAG
|   |   README.md
|   |   
|   📁 v
|       📁 cache
|           |   lastfailed
|           |   nodeids
|           |   stepwise
|           
📁 common
|   |   drive.py
|   |   fake_data.py
|   |   
|   📁 __pycache__
|           drive.cpython-312.pyc
|           fake_data.cpython-312.pyc
|           
📁 src
|   📁 page
|   |   |   create_new_user.py
|   |   |   login.py
|   |   |   site_administrator.py
|   |   |   __init__.py
|   |   |   
|   |   📁 __pycache__
|   |       |   create_new_user.cpython-312.pyc
|   |       |   login.cpython-312.pyc
|   |       |   site_administrator.cpython-312.pyc
|   |       |   __init__.cpython-312.pyc
|   |       
|   |__ __init__.py
|   |   
|   📁 __pycache__
|           __init__.cpython-312.pyc
|           
📁 tests
|   |   test_1_create_user.py
|   |   __init__.py
|   |   
|   📁 __pycache__
|           test_1_create_user.cpython-312-pytest-8.1.1.pyc
|           __init__.cpython-312.pyc
|           
utils
