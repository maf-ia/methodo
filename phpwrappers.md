<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html) [Hacking](hacking.html)

### PHP Filters
Une faille pas super connue mais dévastatrice, car elle permet de lire du code source php !
(on peut lire des fichier de config, ou se trouve les identifiants de connexion a la bdd mysql par exemple...)
 
Si vous ne connaissez pas les wrappers php et les filters, c'est ça : php://. Oui, ça existe :D.
Imaginez une faille include basique.
 
Code :
index.php?page=index
 
Vous pouvez evidemment inclure config.php : index.php?page=config.
Mais le probleme est que comme vous includez un fichier php, le php est éxécuté !
Et il est impossible de voir la source PHP.
 
C'est là qu'interviennent les wrappers PHP et leurs filters. Il suffit de rentrer ceci :
Code :
index.php?page=php://filter/read=convert.base64-encode/resource=config
 
Pour se retrouver avec config.php ! Oui, sauf que le code php de config se serait éxécuté...
Si on avait pas utilisé les filters php pour encoder le fichier en base64 ! Et en plus de ça, le résultat des wrappers php se retrouve dans le stdout donc vous avez le base64 de config.php devant les yeux !
Reste plus qu'a decoder et voilà ^^ (ps: le coup du null byte %00 marche toujours si jamais vous devez changer l'extension !)
 
Pour l'info : il existe d'autres techniques dans le genre, comme data:// par exemple.
Testez de faire :
Code :
<?php echo file_get_contents('data://text/plain;base64,KHRhIHByaXMgbGEgcGVpbmUgZGUgZGVjb2RlciBjZSBiYXNlNjQgPyk='); ?>
 
Résultat : le base64 a été décodé et affiché. Ça peut etre utile dans certaines situations... ;)[/code]
Luxerails 

data://text/plain;base64,php://filter/read=convert.base64-encode/resource= 

Ex: http://www.xxx.org/includes.php?page=data://text/plain,maf => pour afficher "maf"
