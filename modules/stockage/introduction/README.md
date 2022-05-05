# Sqlite3


> Sqlite3 est la base de donnée la plus [utilisée au monde](https://www.sqlite.org/mostdeployed.html) 🌏 !

Prérequis: 
----------

* Avoir sqlite3 d'installé, nativement c'est fait sur Macos.

Créer une database :
--------------------

Pour créer une base il suffit de lancer la commande : 

```shell
sqlite3 ma-data-base.sqlite
```

Un fichier sera crée à l'endroit ou nous avons lancé la commande, ce fichier va stocker : 
* La définition des tables 
* Les données



Pour créer des tables :
-----------------------

Créer une table travail :
```sql
CREATE TABLE travail
(
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(64)
);
```

Créer une table utilisateur avec une relation sur la table travail : 
```sql
CREATE TABLE utilisateur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom VARCHAR(64),
    prenom VARCHAR(64),
    travail_id INTEGER NOT NULL,
    FOREIGN KEY (travail_id)
       REFERENCES travail (id)                     
);
```

Manipuler les données : INSERT SELECT UPDATE DELETE
---------------------------------------------------

Insertion des données pour la table travail:

```sql
INSERT INTO travail('nom') VALUES ('Data Engineer');
INSERT INTO travail('nom') VALUES ('DevOps');
```

Insertion des données pour la table utilisateur avec `travail_id` comme relation avec la table travail.

```sql
INSERT INTO utilisateur('nom', 'prenom', 'travail_id') VALUES ('Gates','Bill', '1');
INSERT INTO utilisateur('nom', 'prenom', 'travail_id') VALUES ('Musk','Elon', '2');
```

Pour les jointures, on pourra utiliser INNER JOIN, qui nous permettra de récupérer des utilisateurs avec
un travail associé.

```sql
SELECT u.nom, u.prenom, t.nom AS travail 
FROM utilisateur u 
INNER JOIN travail t 
ON u.travail_id = t.id; 
```

Exporter une table en csv:
--------------------------

Pour extraire la donnée vous pouvez lancer les commandes: 
```
.headers on                 # Pour avoir les headers en première ligne
.mode csv                   # Pour sélectionner le format csv
.output data.csv            # Pour commencer à écouter pour écrire dans le fichier data.csv
select * from utilisateur;  # Sélectionner les données à extraire
.quit                       # Pour quitter la console
```

⚠️ Attention à partir de l'action `.output` toutes les actions select sont stockées en mode append.


Importer une table en csv :
---------------------------

Pour importer de la donnée depuis un fichier csv : 
```
.mode csv utilisateur_imported 
.import data.csv utilisateur_imported # Importer les données du fichier data.csv dans la table utilisateur_imported
```

⚠️ Attention le fichier `data.csv` ne doit pas avoir d'headers si la table est déjà définie.



> 💡 Sqlite3 est pratique pour les personnes qui veulent analyser rapidement un dataset csv à travers des
> requêtes sql.
