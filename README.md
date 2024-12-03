# MLOps - TP 7 : Projet MLOps 1

## Description du Projet
Ce projet vise à appliquer les principes de MLOps pour développer un pipeline complet de machine learning, allant de l’ingestion des données à la mise en production d’un modèle de prédiction.

## Workflow Général
Le développement du projet suit les étapes suivantes :

1. **Configuration des fichiers YAML** :
   - `config.yaml` : Paramètres généraux du projet.
   - `schema.yaml` : Schéma des données.
   - `params.yaml` : Hyperparamètres du modèle.

2. **Définition des Entités (Entities)** :
   - Classes décrivant la structure des données et les configurations utilisées dans le projet.

3. **Développement des Composants** :
   - Implémentation des composants pour l’ingestion, la validation et la préparation des données.

4. **Création des Pipelines** :
   - Pipelines pour l’entraînement et la prédiction des modèles.

5. **Exécution via `main.py`** :
   - Fichier central pour orchestrer les pipelines du projet.

6. **Interface utilisateur (éventuelle)** :
   - Création d'une interface pour interagir avec le modèle via `app.py`.

## Organisation du Projet

Voici la structure de base du projet :

```
mlops_project/
|-- src/
|   |-- mlProject/
|   |   |-- __init__.py
|   |   |-- components/
|   |   |-- pipelines/
|   |   |-- utils/
|   |       |-- common.py
|   |-- config/
|       |-- config.yaml
|       |-- schema.yaml
|       |-- params.yaml
|-- notebooks/
|-- tests/
|-- requirements.txt
|-- setup.py
|-- main.py
|-- README.md
```

### Contenu Clé des Dossiers

- **src/mlProject/components/** : Contient les classes pour la gestion des données et l'entraînement.
- **src/mlProject/pipelines/** : Implémente les pipelines d'entraînement et de prédiction.
- **src/mlProject/utils/common.py** : Contient des fonctions réutilisables comme `ConfigBox` et `Ensure Annotation`.
- **notebooks/** : Contient les notebooks pour tester des parties du projet.
- **tests/** : Unit tests pour les différents composants.
- **requirements.txt** : Liste des bibliothèques Python requises.
- **setup.py** : Configuration pour créer un package installable.
- **main.py** : Point d'entrée principal pour l'exécution du projet.

## Démarrage Rapide

### Prérequis
- **Python** (>= 3.8)
- **Git**

### Installation
1. Clonez le dépôt :
   ```bash
   git clone <URL-du-dépôt>
   cd mlops_project
   ```
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Installez le projet comme package local :
   ```bash
   pip install -e .
   ```

### Exécution

1. Configurez les paramètres dans `config/config.yaml`.
2. Lancez le pipeline d'entraînement :
   ```bash
   python main.py
   ```
3. Optionnel : Exposez le modèle via une API avec `app.py`.

### Journalisation
Les logs sont gérés par le module `logging` et enregistrés dans un fichier local pour le suivi et la détection des anomalies.

## Contribution
1. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/nom_fonctionnalité
   ```
2. Poussez les modifications et ouvrez une pull request.

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus de détails.

