## Curso Django - Canal Hora de Codar

Tenha o ```python3``` e o ```pip``` instalado.

1. Instalado o virtualenv:
    - pip3 install virtualenv --user

1. Criando uma nova virtualenv:
    - virtualenv .venv
 
1. Ativando a .venv:
    - source .venv/bin/activate

1. Instalando os requerimentos do projeto:
    - pip install -r requirements.txt

1. Criando as migrations:
    - python manage.py makemigrations && python manage.py migrate

1. Criando um usuario admin:
    - python manage.py createsuperuser

1. Rodando o projeto:
    - python manage.py runserver


Outros comandos:

1. Criando um novo projeto com o django:
    - django-admin startproject nomeprojeto

1. Criando uma app:
    - django-admin startapp nomedaapp 
