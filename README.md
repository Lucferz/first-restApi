# first-restApi
First REST API made with django framework

# Requerimientos del proyecto 
1. Python 3.10

# Pasos para crear el proyecto 

1. Crear un entorno virtual y activarlo<br>
    ` python -m venv .venv `<br>
    **Activacion en Linux**<br>
    ` source .venv/bin/activate `<br>
    **Activacion en Windows**<br>
    ` .\.venv\Scripts\activate `
2. Instalar la dependencia django
    > Dentro del entorno virtual<br>
    ` pip install django `
3. Crear un proyecto django<br>
    ` django-admin startproject drf_bootcamp . `
4. Crear una aplicacion llamada api<br>
    ` python manage.py startapp api `
5. Instalar dependencia de django rest<br>
    ` pip install djangorestframework `
6. Correr las migraciones<br>
    ` python manage.py migrate `