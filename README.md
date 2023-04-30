# django-example

Just a small django application to get familiar with the framework.
It's almost a copy of the one used in the official django documentation.

The steps below describe how the environment is initially setup and how to run it locally.

## Initial setup (already configured)

- Setting up a clean python environment with pyenv & virtualenv

```bash
mkdir django-example && cd django-example

pyenv virtualenvs # List virtual envs
pyenv virtualenv django-example # Create a virtual env with the same name as the folder
pyenv activate django-example # Activate the virtualenv ()

# It is also recommended to add the following to the .bashrc or .zshrc to automatically activate virtualenvs
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```

- Installing the dependencies

```bash
# Install deps
pip install django

# Write a requirements.txt file
pip install pipreqs
pipreqs .
```

- Scaffolding the app

```bash
# Create a new project
django-admin startproject pollster .

# Create an app
python manage.py startapp polls
```

## Getting started

Thanks to the first setup, whenever a terminal session is started in this `django-example` directory, the python virtualenv will directly change to `(django-example)`.

```bash
# Install the dependencies
pip install -r requirements.txt

# Run the initial migration
python manage.py migrate

# Run the server
python manage.py runserver
```

## Useful commands

- Creating a migration file for the polls app

```bash
python manage.py makemigrations polls
```

- Applying the migration

```bash
python manage.py migrate
```

### Resources

- [Python environments with pyenv and virtualenv](https://fathomtech.io/blog/python-environments-with-pyenv-and-vitualenv/)
- [Managing virtual environments with pyenv](https://towardsdatascience.com/managing-virtual-environment-with-pyenv-ae6f3fb835f8)
- [Python Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU)
