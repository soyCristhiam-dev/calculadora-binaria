# Calculadora Binaria (Django)


Proyecto en Django que convierte números binarios a decimal, octal y hexadecimal.


## Requisitos
- Python 3.10+ (o 3.8+)
- pip
- virtualenv (recomendado)


## Instalación local


```bash
# clonar el repositorio
git clone https://github.com/soyCristhiam-dev/calculadora-binaria.git
cd conversiones

# crear y activar virtualenv
python -m venv venv

# Windows
venv\Scripts\activate


# instalar dependencias
pip install -r requirements.txt


# ejecutar migraciones y levantar servidor
python manage.py migrate
python manage.py runserver

