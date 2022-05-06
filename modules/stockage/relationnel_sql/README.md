



Prérequis: 
----------

* Avoir sqlite3 d'installé, nativement c'est fait sur Macos.
* .headers ON :  pour afficher le nom des colonnes  
* .mode column :  pour afficher en mode colonnes  



Introduction:
------------

```
Edgar Codd a publié un article majeur sur les modèles relationnels au début des années 1970. Il ne définissait à l'origine que
la notation mathématique de la façon dont un SGBD pourrait exécuter des requêtes sur un SGBD modèle relationnel.
```

```
L'utilisateur n'a qu'à spécifier le résultat qu'il souhaite en utilisant un langage déclaratif (c'est-à-dire SQL). Le
Le SGBD est chargé de déterminer le plan le plus efficace pour produire cette réponse.
```

```
SQL: Structured Query Language
IBM l'appelait à l'origine « SEQUEL ».

• Composé de différentes classes de commandes :

1. Langage de manipulation de données (DML) : SÉLECTIONNER, INSÉRER, METTRE À JOUR, SUPPRIMER.
2. Langage de définition de données (DDL) : définition de schéma.
3. Data Control Language (DCL) : Sécurité, contrôles d'accès.

• SQL n'est pas un langage mort. Il est mis à jour avec de nouvelles fonctionnalités tous les deux ans !
```

Initialisation:
------------
Créer une table eleves : 
```sql
CREATE TABLE eleves (
id   INTEGER PRIMARY KEY AUTOINCREMENT,
nom VARCHAR(16),
prenom VARCHAR(32) ,
travail VARCHAR(32), 
age SMALLINT
);
```

```sql
INSERT INTO eleves('nom', 'prenom','travail', 'age') VALUES ('Gates','Bill', 'Geek', 23);
INSERT INTO eleves('nom', 'prenom','travail', 'age') VALUES ('Musk','Elon', 'Geek',19);
INSERT INTO eleves('nom', 'prenom','travail', 'age') VALUES ('Kafka','Franz', 'Ecrivain',20);
INSERT INTO eleves('nom', 'prenom','travail', 'age') VALUES ('Ernest','Hemingway', 'Ecrivain',20);
```


Aggregation:
------------

Une fonction d'agrégation prend un ensemble de tuples en entrée et produit une seule valeur scalaire en sortie.

```sql
SELECT COUNT(*) FROM eleves WHERE travail LIKE '%ain';
```

```sql
SELECT travail,AVG(age) FROM eleves group by travail ;
```


```sql
SELECT travail,AVG(age) FROM eleves group by travail HAVING travail LIKE '%ain';
```


Redirection de la sortie:
------------
Au lieu d'avoir le résultat d'une requête renvoyée au client (par exemple, terminal), vous pouvez dire au SGBD de
stocker les résultats dans une autre table.

```sql
CREATE TABLE travail AS SELECT travail,AVG(age) FROM eleves group by travail;
```


Requêtes imbriquées:
------------

Appelez des requêtes à l'intérieur d'autres requêtes pour exécuter une logique plus complexe dans une seule requête.

```sql
 select * from 
   eleves e ,
   (SELECT travail,AVG(age)  as age_moyen FROM eleves group by travail) a
 where e.age > a.age_moyen;
```

Window:
------------

Effectue un calcul sur un ensemble de tuples. Comme une agrégation mais il renvoie toujours la ligne original
tuples.

```sql
SELECT nom, prenom, ROW_NUMBER() OVER (PARTITION BY travail)
FROM eleves ORDER BY age;
```