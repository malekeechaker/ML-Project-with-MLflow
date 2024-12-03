import os
import logging

# Configurer le logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Nom du projet
project_name = "ml_project"

# Liste des fichiers à créer
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

# Création des fichiers et des répertoires
for filepath in list_of_files:
    filepath = os.path.normpath(filepath)  # Normaliser le chemin (pour Windows/Linux)
    filedir, filename = os.path.split(filepath)  # Séparer le répertoire et le fichier

    # Créer le répertoire si nécessaire
    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Répertoire créé : {filedir}")

    # Créer le fichier si nécessaire
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # Crée un fichier vide
        logging.info(f"Fichier créé : {filepath}")
    else:
        logging.info(f"Fichier existe déjà : {filepath}")
