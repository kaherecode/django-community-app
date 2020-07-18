Ce projet est l'exemple pratique du tutoriel [Développer vos applications web avec Django](https://www.kaherecode.com/tutorial/developper-vos-applications-web-avec-django) sur **Kaherecode**.

# Installation

Pour installer ce projet, il faut d'abord s'assurer d'avoir la version 3 de python installer sur ton ordinateur. Si c'est le cas, crée un dossier pour ton projet et place toi dans ce dossier. Il faut maintenant créer un environnement virtuel pour ton projet avec `venv`:

```bash
$ python3 -m venv env
```

Une fois l'environnement virtuel créé, il faut ensuite l'activer avec:

```bash
$ source env/bin/activate
```

Tu peux maintenant cloner le projet avec:

```bash
$ git clone https://github.com/kaherecode/django-community-app.git
```

Un dossier `django-community-app` va être créé dans ton dossier courant, il faut te déplacer dans ce dossier et installer les dépendances avec:

```bash
$ pip install -r requirements.txt
```

Une fois les dépendances installer, tu peux maintenant démarrer ton projet avec la commande:

```bash
$ python manage.py runserver
```

Ca y est, tu peux accéder à ton site sur http://127.0.0.1:8000.

> Cette application n'est pas encore terminer, ce fichier sera completer avec l'évolution du tutoriel.

N'hésite pas à te rendre sur le site de [Kaherecode](https://kaherecode.com) pour trouver pleins d'autres tutoriels.

