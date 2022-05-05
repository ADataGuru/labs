# Batch Unix:


> Le système Unix permet d’analyser un fichier simplement enchaînant un ensemble de commandes. 
> Cela est rendu possible grâce à une interface commune qui permet de transférer simplement de la donnée
> d’une étape à l’autre !


Prenons comme exemple un serveur web qui ajoute une ligne à fichier log à chaque fois qu'il sert une requête. Par exemple, en utilisant le format de log par défaut de nginx, une ligne de log devrait ressembler à : 

```
216.58.210.78 - - [05/May/2022:17:55:11 +0000] "GET /css/typography.css HTTP/1.1"
200 3377 "https://www.dataguru.fr" "Mozilla/5.0 (Macintosh; Intel Mac OS X
10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115
Safari/537.36"
```

Si on essaie de retrouver la définition de ce log, ça ressemblerait à : 

```
$remote_addr - $remote_user [$time_local] "$request"
$status $body_bytes_sent "$http_referer" "$http_user_agent"
```

Cette ligne de log indique que le 27 février 2015, à 17:55:11 UTC, le serveur a reçu une requête pour le
fichier /css/typography.css de l'adresse IP du client 216.58.210.78. L'utilisateur n'était pas authentifié, donc 
$remote_user est défini comme un tiret(-). Le statut de la réponse est 200 (c'est-à-dire que la demande a abouti), 
et la réponse était de 3 377 octets. Le navigateur Web était Chrome 40, et il a chargé la page https://www.dataguru.fr


Analiser un fichier de log:
---------------------------

Par exemple, disons que vous voulez trouver les cinq pages les plus populaires de votre site Web. Vous pouvez
faire cela dans un shell Unix de la manière suivante:

```shell
cat /var/log/nginx/access.log | # 1️⃣
 awk '{print $7}' |             # 2️⃣
 sort |                         # 3️⃣
 uniq -c |                      # 4️⃣
 sort -r -n |                   # 5️⃣
 head -n 5                      # 6️⃣
```

+ 1️⃣ Lire le fichier log
+ 2️⃣ Divise chaque ligne en champs par des espaces, et ne garde que le septième de ces champs
de chaque ligne, qui se trouve être l'URL demandée. Dans notre exemple, cette URL  est /css/typography.css.
+ 3️⃣ Trier par ordre alphabétique la liste des URLs demandées.
+ 4️⃣ La commande uniq filtre les lignes répétées dans son entrée en vérifiant si deux lignes adjacentes sont identiques. L'option -c lui demande d'afficher un compteur : pour chaque chaque URL distincte, elle indique combien de fois cette URL est apparue dans l'entrée.
+ 5️⃣ Le deuxième tri est effectué en fonction du nombre (-n) au début de chaque ligne, qui correspond au nombre de fois que l'URL a été requêtée. Il renvoie ensuite les résultats dans l'ordre inverse (-r), c'est-à-dire en commençant par le nombre le plus élevé.
+ 6️⃣ Enfin, head ne sort que les cinq premières lignes (-n 5) de l'entrée, et rejette le reste.

> 💡 Bien que la cli parait souvent obscure et non familier, néanmoins ça reste un outil puissant. 
> On peut traiter des Go de logs en quelques secondes. En plus d'être performant, ça reste très custom, au lieu de retrouver
> les pages les plus visitées on pourrait afficher le top 10 des ips des clients les plus importants en changeant 
> l'argument d'awk par '{print $1}'