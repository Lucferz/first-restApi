# first-restApi
First REST API made with django framework

# Requerimientos del proyecto 
1. Python 3.10

# Pasos para crear el proyecto 

1. Crear un entorno virtual y actuvarlo
    python -m venv .venv
    ** Activacion en Linux **
    source .venv/bin/activate
    ** Activacion en Windows **
    .\.venv\Scripts\activate
2. Instalar la dependencia django
    > Dentro del entorno virtual
    ` pip install django `
3. Crear un proyecto django
    ` django-admin startproject drf_bootcamp . `
4. Crear una aplicacion llamada api
    ` python manage.py startapp api `
5. Instalar dependencia de django rest
    ` pip install djangorestframework `