<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Crypto messages</title>
</head>
[Crypto](crypto.html)

## Generalites


### Algorithmes classiques
- Cesar : sur l'alphabet, sur l'ascii
- Vigenere/Rozier/Gronsfeld
- Vernam
- Atbash (chiffre miroir a<->z, b<->y)
- Albam (ROT13)
- Atbah (substitution reverible a->i, cf grille associée)
- ADFGX puis ADFGVX
- AMSCO
- Affine (paramètres a et b)

#### Code composé uniquement de lettres
- Cesar, Vigenere, Atbash
- Table périodique des éléments
- Playfair (surtout si regroupé par 2)
- Substitution
- Railfence / ZigZag
- Vernam

#### Code composé presque uniquement de lettres

- S'il y a en plus des / et à la fin = ou == : il peut s'agir de base64
 

#### Code composé uniquement de chiffres

- Carré de Polybe : coordonnées dans grille 5x5 en général mais on peut imaginer 6x6
- Chiffre des nihilistes : surchiffrement du carré avec une clé à additionner, finalement pas beaucoup plus complexe
- Cadran de l'armée mexicaine
- Cadran chiffrant d'Alberti
- Numéro de la lettre dans l'alphabet
- Code ascii
- Lettre du clavier téléphonique : soit répétée autant que nécessaire, soit juste une valeur pour chaque lettre d'un groupe (plus dur)
- Décomposer en facteurs premier et récupérer les facteurs ou les exposants pour en déduire les lettres ou les codes ascii...
- Faire des conversions de base, par exemple la base 36, 52, 62...



#### Code composé uniquement de chiffres et lettres hexa

- Cela peut être simplement de l'ascii
- Si le bloc de texte à une longueur particulière ou est composé de blocs de même taille, il peut s'agit de hash du texte à reverser (rainbow tables, http://md5cracker.org/, https://crackstation.net/...) (40 car hexa par exemple pour le MD5)

#### Code composé uniquement de chiffres et lettres (autre)

- Un décalage du mot sur les touches du clavier (tester les directions et différents claviers)

#### Code composé uniquement de chiffres, lettres et ponctuation

- Un décalage du mot sur les touches du clavier (tester les directions et différents claviers)
- Un changement de clavier, typiquement qwerty <-> dvorak


#### Code composé de caractères ascii variés

- Notamment s'ils semblent totalement aléatoires et variés, il pet s'agir d'UUENCODE (encore plus si encadré par begin 644 / end). Il peut s'agir aussi d'autres encodages.
- Décalage de type Cesar mais sur la table ascii

#### Composés de symboles
Le plus simple est souvent de chercher sur Google, il s'agit souvent d'une correspondance lettre-symbole simple, en voici quelques uns :
- Alphabet d'Arthur et les Minimoys
- Alphabet Ogham (principalement des traits - origine médiévale celtique)
- Alphabet Pokemon Zarbi (on peut reconnaître les lettres dans les formes de ce pokemon)

Il est aussi possible que les symboles désignent du binaire ou un autre encodage.
Il faut parfois détecter une spécificité du symbole (nombre de boucles, nombre de traits, d'angles...).
Il est aussi possible qu'il y ait plusieurs symboles unitaires pour composer ces symboles (rond, carré, triangle...) et qu'il faille ne considérer ces symboles qu'un à un et regarder la forme que cela donne (juste les carrés puis juste les ronds... chacun donnant une lettre ou un chiffre).

#### Autres
- Texte latin incompréhensible : Ave Maria de Trithème : à chaque lettre correspond 2 mots latins (on en choisi un parmi eux)
- Grille de Cardan : on applique un masque / une grille sur un texte pour faire apparaître les lettres du message
- Grille tournante : sur un texte sous forme de carré 2n * 2n, on applique une grille 4 fois en la tournant à chaque fois de 90° (n² cases lisibles à chaque fois, cf programme de brute force)



