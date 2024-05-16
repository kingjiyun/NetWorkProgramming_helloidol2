# hello idol2
---

1. startproject helloidol2
    1. python - m pip install django~=4.2
    2. django-admin startproject helloidol2
    3. File > Settings... > Language & Frameworks > Django
       [v] Enable Django Support
    4. Run>Edit Configurations...> + > Django Server > Name: runserver
    5. VCS > Enable Version Control Integration... > Git > OK
2. startapp 소닉
   1. python manage.py startapp 소닉
   2. '소닉', in INSTALLED_APPS in settings.py
3. 소닉/
      1. models
         1. Character
            1. name, feature, created_at, updated_at
            2. `__str__()`
         2. python manage.py makemigraions 소닉
         3. python manage.py migrate
      2. admin
         1. python manage.py createsuperuser
         2. localhost:8000/admin/
         3. Character