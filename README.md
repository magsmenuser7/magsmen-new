# magsmen-new
# magsmen
#django

#install env
#pip install virtualenv
# create virtual environment
#python -m venv env-magsmen

# activate virtual environment
#env-magsmen\Scripts\activate

# install libs
pip freeze > requirements.txt 
pip install -r requirements.txt

# create django  project
Django-admin startproject "PROJECTNAME"

# create django app 
python manage.py startapp "APP NAME"

# create super user 
python manage.py createsuperuser
# migration process 

python manage.py makemigrations 

# run migrations 
python manage.py migrate 

# Run project or applications
python manage.py runserver
