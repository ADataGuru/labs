
Prérequis: 
----------

* Avoir sqlite3 d'installé, nativement c'est fait sur Macos.
* .headers ON :  pour afficher le nom des colonnes  
* .mode column :  pour afficher en mode colonnes  

Introduction:
------------

```
SQLite est une base de données transactionnelle dans laquelle toutes les modifications et requêtes sont atomiques, cohérentes, isolées et durables (ACID).

  - Atomique: Un changement ne peut pas être décomposé. Lorsque vous validez une transaction, la totalité de la transaction est appliquée ou rien.
  - Cohérent : Lorsque la transaction est validée ou annulée, il est important que la transaction maintienne la cohérence de la base de données.
  - Isolation : une transaction en attente effectuée par une session doit être isolée des autres sessions.
  - Durable : si une transaction est validée avec succès, les modifications doivent être permanentes dans la base de données, meme en cas de panne. Au contraire, 
    si le programme plante avant que la transaction ne soit validée, la modification ne devrait pas persister.
 ```


   ![img_3.png](img_3.png)


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
```

```sql
CREATE TABLE produits (
identifiant_produit   INTEGER PRIMARY KEY,
nom VARCHAR(16),
gamme VARCHAR(32) ,
pegi INTEGER NOT NULL,
prix INTEGER NOT NULL,
CHECK(prix >= 0)
);
```

```sql
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (1,'Gta', 'action', 18,30);
INSERT INTO produits('identifiant_produit', 'nom','gamme', 'pegi','prix') VALUES (2,'GodOfWar', 'action', 18,30);
```



LES ETAPES D'UNE TRANSACTION:
------------

On commence une transaction avec l'instrcution suivante

```sql
BEGIN TRANSACTION;
```

On ferme une transaction soit avec 

 - Un commit pour confirmer: 
  
  ```sql
    COMMIT;
  ```
   

 - Un rollback pour ne pas la stocké :

  ```sql
    ROLLBACK;
  ```

Exemple de transaction  :
------------


```sql
select * from produits;
select * from magasins;
```

On a des rédcutions de prix et de nouveaux magasins 

```sql
BEGIN TRANSACTION;

UPDATE produits
   SET prix = prix - 5
 WHERE nom = 'Gta';
 
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('nouveau_magasin','paris', 2, TRUE);

COMMIT;
```

```sql
select * from produits;
select * from magasins;
```

On a des  nouvelles rédcutions de prix pour un des produits :

```sql
BEGIN TRANSACTION;

UPDATE produits
   SET prix = prix - 27
 WHERE nom = 'Gta';
 
INSERT INTO magasins('nom', 'ville','identifiant_produit', 'en_stock') VALUES ('encore_un_magasin','paris', 1, TRUE);
```

On remarque que le changement est visible sur la table magasins (que sur la session)

```sql
select * from produits;
select * from magasins;
```
On annule la dernière transaction

```sql
ROLLBACK ;
```

On remarque que tous les changements de la transaction sont annulés

```sql
select * from produits;
select * from magasins;
```