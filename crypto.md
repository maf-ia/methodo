<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html)

## Crypto

### Generalites

- Time Attack : Le but d’une timing attack est de comparer les temps de réponse pour en déduire les valeurs des clés car les traitements ne sont pas les mêmes que ce soit ok ou pas.

### [Messages](crypto-messages.html)

### DES
- Tester les weak keys (existe aussi sur d'autres algos)

### GOST
- Version russe du DES

### [Attaque RSA](crypto-rsa.html)

### Outils
#### fcrackzip
1. Par dico 
fcrackzip -v -D -u -p ../../resources/rockyou.txt file-0002.zip 

Existe aussi des dicos dans : ll /usr/share/dict/
-rw-r--r--   1 root root  938848 oct.  23  2011 american-english
-rw-r--r--   1 root root  938969 oct.  23  2011 british-english
-rw-r--r--   1 root root  477238 mars  23 16:42 cracklib-small
-rw-r--r--   1 root root 1542061 avril 30  2012 french

2. Par bruteforce
Méthodes : -c aA1 
Longueur : -l 1-4 (par exemple)

#### hashcat / cudahashcat / oclhashcat
./hashcat-cli64.bin -m 100 -a 3 -1 ?l?u  sha-Abc.txt ?1?1?1

"-m" indique l'algo (100 = sha1)
"-a" méthode d'attaque (3=bruteforce)
"?l?u" les patterns de bf

#### John the Ripper
$ john xxx
[Doc plus complete](crypto-john.html)

#### msieve
Pour décomposer des (assez) grands nombres en facteurs premiers. Peut utiliser CUDA
$ msieve xxx
=> Lire le fichier .log pour la réponse

#### yafu
Pour décomposer des grands nombres en facteurs premiers.
La version windows à l'air de mieux fonctionner que la version linux (mais opérationnelle quand même) :
$ yafu
puis:
factor(xxx)

#### Cracker par XOR
Outre le bf facile à coder, on peut utiliser xortool.py pour détecter les tailles probables, voir attaquer le fichier pour ces tailles





