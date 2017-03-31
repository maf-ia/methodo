<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[Crypto](crypto.html)

## Composés de chiffres uniquement
- Numéro de la lettre dans l'alphabet
- Code ascii
- Lettre du clavier téléphonique : soit répétée autant que nécessaire, soit juste une valeur pour chaque lettre d'un groupe (plus dur)
- Carré de Polybe : coordonnées dans grille 5x5 en général mais on peut imaginer 6x6
- Chiffre des Nihilistes : surchiffrement du carré avec une clé à additionner, finalement pas beaucoup plus complexe
- Table périodique des éléments
- Décomposer en facteurs premier et récupérer les facteurs ou les exposants pour en déduire les lettres ou les codes ascii...


## Composés de lettres uniquement
- Playfair (surtout si regroupé par 2)
- Substitution
- Railfence
- Vernam



## Generalites


### Algorithmes classiques
- Cesar : sur l'alphabet, sur l'ascii
- Vigenere/Rozier/Gronsfeld
- Vernam
- Atbash (chiffre miroir)
- Albam (ROT13)
- Atbah

#### Code composé presque uniquement de lettres

- S'il y a en plus des / et à la fin = ou == : il peut s'agir de base64
 

#### Code composé uniquement de chiffres

- Carré de Polybe : coordonnées dans grille 5x5 en général mais on peut imaginer 6x6
- Chiffre des nihilistes : surchiffrement du carré avec une clé à additionner, finalement pas beaucoup plus complexe

#### Code composé uniquement de chiffres et lettres hexa

- Cela peut être simplement de l'ascii
- Si le bloc de texte à une longueur particulière ou est composé de blocs de même taille, il peut s'agit de hash du texte à reverser (rainbow tables, http://md5cracker.org/, https://crackstation.net/...) (40 car hexa par exemple pour le MD5)

#### Code composé uniquement de chiffres et lettres (autre)



#### Code composé de caractères ascii variés

- Notamment s'ils semblent totalement aléatoires et variés, il pet s'agir d'UUENCODE (encore plus si encadré par begin 644 / end). Il peut s'agir aussi d'autres encodages.
- Décalage de type Cesar mais sur la table ascii

