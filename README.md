# django-example

Just a small django application to get familiar with the framework.
It's almost a copy of the one used in the official django documentation.

The steps below describe how the environment is initially setup and how to run it locally.

## Initial setup

- Setting up a clean python environment with pyenv & virtualenv

```bash
mkdir django-example && cd django-example

pyenv virtualenvs # List virtual envs
pyenv virtualenv django-example # Create a virtual env with the same name as the folder
pyenv activate django-example # Activate the virtualenv ()

# It is also recommended to add the following to the .bashrc or .zshrc to automatically activate virtualenvs
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```

- Installing the dependencies and scaffolding the app

```bash
# Install deps
pip install django

# Create a new project
django-admin startproject pollster .
```

## Getting started

Thanks to the first setup, whenever I open a terminal in this `django-example` directory, the python virtualenv will directly change to `(django-example)`.

```bash
# Run the initial migration
python manage.py migrate

# Run the server
python manage.py runserver
```

To create any subsequent apps in the project

```bash
python manage.py startapp polls
```

## Resources

- [Python environments with pyenv and virtualenv](https://fathomtech.io/blog/python-environments-with-pyenv-and-vitualenv/)
- [Managing virtual environments with pyenv](https://towardsdatascience.com/managing-virtual-environment-with-pyenv-ae6f3fb835f8)
