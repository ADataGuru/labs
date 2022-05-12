



Prérequis: 
----------

* Avoir sqlite3 d'installé, nativement c'est fait sur Macos.
* .eqp ON :  activer le explain 
* .headers ON :  pour afficher le nom des colonnes  
* .mode column :  pour afficher en mode colonnes  

Lecture: 
----------
https://www.sqlite.org/eqp.html

Introduction:
------------

```
  - Le SGBD convertit une instruction SQL en un plan de requête
  - Les opérateurs sont disposés dans une arborescence. 
  - Les flux de données proviennent de les feuilles vers la racine. 
  - La sortie du nœud racine dans l'arborescence est le résultat de la requête.
  - Le même plan de requête peut être exécuté de plusieurs manières.
```


```
SQL est un langage déclaratif. Cela signifie que l'utilisateur indique au SGBD la réponse qu'il souhaite, et non comment l'obtenir.
Le SGBD doit traduire une instruction SQL en un plan de requête exécutable. Mais il y a différentes façons d'exécuter une requête (par exemple, les algorithmes de jointure) et 


il y aura des différences de performances pour ces régimes. 

Ainsi, le SGBD a besoin d'un moyen de choisir le "meilleur" plan pour une requête donnée.

C'est le travail du Optimiseur de SGBD.

Il existe deux types de stratégies d'optimisation :
 • Heuristique/Règles : réécrivez la requête pour supprimer les inefficacités. Ne nécessite pas de modèle de coût.
 • Recherche basée sur les coûts : utilisez un modèle de coût pour évaluer plusieurs plans équivalents et choisissez celui qui moindre coût.
```


Initialisation:
------------
```sql
CREATE TABLE magasins (
id   INTEGER PRIMARY KEY AUTOINCREMENT,
nom VARCHAR(16),
ville VARCHAR(32) ,
identifiant_produit INTEGER, 
en_stock BOOLEAN
);
```

```sql
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('microgame','paris', 1, TRUE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('microgame','paris', 3, TRUE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('microgame','paris', 5, FALSE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('macrogame_21','lille', 1, TRUE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('macrogame_21','lille',5, FALSE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('irongame','paris', 4, TRUE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('irongame','paris', 3, TRUE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('irongame','paris', 5, FALSE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('decagame','toulouse', 2, TRUE);
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('decagame','toulouse', 5, TRUE);
```

```sql
CREATE TABLE produits (
identifiant_produit   INTEGER PRIMARY KEY,
nom VARCHAR(16),
gamme VARCHAR(32) ,
pegi INTEGER,
prix INTEGER
);
```

```sql
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (1,'Gta', 'action', 18,30);
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (2,'GodOfWar', 'action', 18,30);
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (3,'AnimalCrossing', 'strategie', 3,40);
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (4,'Warhammer', 'strategie', 16,30);
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (5,'EldenRing', 'action', 18,50);
```


Plan d'execution  pour des cas simple :
------------

Le EXPLAIN nous montre ce que fait la base de donnée en background pour trouver le resultat efficacement; 

```sql
EXPLAIN QUERY PLAN SELECT * FROM produits where prix > 40;
```

```sql
EXPLAIN QUERY PLAN SELECT * FROM produits where gamme = 'action' ORDER BY prix;
```

```sql
CREATE INDEX i1 ON produits(prix);
EXPLAIN QUERY PLAN SELECT * FROM produits where gamme = 'action' ORDER BY prix;
```


Plan d'execution requete  pour un cas complexe :
------------

Exemple de reecriture de requete 

Predicate pushdown : l'optimiseur filtre la donnée avant de faire la jointure. 

```sql
 SELECT m.*,p.* FROM 
   magasins m JOIN produits p 
   ON m.identifiant_produit = p.identifiant_produit
   WHERE p.prix > 40
   OR m.en_stock = TRUE
   ORDER BY m.ville;
```