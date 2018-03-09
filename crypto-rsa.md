<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Crypto RSA</title>
</head>
[Crypto](crypto.html)

## Lire un fichiers de clés
$ openssl asn1parse -in cles.pub 

    0:d=0  hl=3 l= 159 cons: SEQUENCE          
    3:d=1  hl=2 l=  13 cons: SEQUENCE          
    5:d=2  hl=2 l=   9 prim: OBJECT            :rsaEncryption
    16:d=2  hl=2 l=   0 prim: NULL              
    18:d=1  hl=3 l= 141 prim: BIT STRING 
=> L'objet qui nous intéresse a l'ID 18
   
$ openssl asn1parse -in cles.pub -i -strparse 18

    0:d=0  hl=3 l= 137 cons: SEQUENCE          
    3:d=1  hl=3 l= 129 prim:  INTEGER           :86E996013E77C41699000E0941D480C046B2F71A4F95B350AC1A4D426372923D8A4561D96FBFB0240595907201AD3225CF6EDED7DE02D91C386FFAC280B72D0F95CAE71F42EBE0D3EDAEACE7CEA3195FA32C1C6080D90EF853D06DD4572C92B9F8310BBC0C635A5E26952511751030A6590816554E763031BCBB31E3F119C65F
    135:d=1  hl=2 l=   3 prim:  INTEGER           :010001

  Ce qui nous donne n et e (=0x010001 ou 65537)

## Utiliser RSA
Utiliser par exemple "sage" (extension python pour les calculs mathématiques):

### Calculer d connaissant p et q
sage: d = inverse_mod(e,(p-1)*(q-1))

### Chiffrer
sage: m = 42 // le message
sage: chiffre = pow(message,e,n)

### Dechiffrer
sage: message = pow(chiffre,d,n)

## Attaques connues

### Factoriser la clé
- Factoriser la clé via le site [factordb](http://factordb.com/)
- Utiliser msieve ou yafu (cf outils sur la page crypto)
- Avec sage (petites valeurs) : p,q = factor(n)

### Oracle de déchiffrement

Si on possède un oracle de déchiffrement (hors le message à trouver), on peut calculer cb = 2**e [n]. On demande alors à déchiffrer cb.c et on divise par 2 le résultat.

### Clés privées partiellement partagées

Utiliser par exemple "sage" (extension python pour les calculs mathématiques):

    sage: pubkey1 = 0x...
    sage: pubkey2 = 0x...
    sage: q = gcd(pubkey1,pubkey2)
Si gcd() renvoie un nombre, pubkey1 et pubkey2 partagent un facteur

### Attaque de Hastad (théorème des restes chinois)
Si on connaît plusieurs chiffré du même message (avec des clés différentes), par exemple 3 chiffrés alors que e=3
crt() puis racine cubique

On peut utiliser sage qui implémente crt(), sinon j'ai un script python mais peut poser pb si les nombres sont trop grands (par ex, solution de SaveWorld dans WeChall)

### Utilisation du théorème de Bezout

Si on connait 2 chiffrés d'un même message utilisant le même n pour clé privée mais des valeurs de e différentes
Dans le cas où e1 et e2 sont premiers entre eux :
Sous sage : e1.xgcd(e2) => donne la décomposition 1 = a.e1 + b.e2
b étant négatif, il faut calculer l'inverse modulaire de c2 : rev2 = inverse_mod(c2,n)
On a alors m = pow(c1,a,n) * pow(rev2,-b,n)

### Attaque de Wiener
Cette attaque se base sur une décomposition en fractions continues pour trouver d qui fait partie de cette décomposition.
Utiliser par exemple "sage" (extension python pour les calculs mathématiques):

    sage: n = 0x...
    sage: e = 0x...
    sage: c_fracs = continued_fraction(e/n).convergents()
    sage: test_message = 42
    sage: test_encrypted = pow(test_message,e,n)
    sage: found = False
          for i in xrange(len(c_fracs)):
            if pow(test_encrypted,c_fracs[i].denom(),n) == test_message:
                d = c_fracs[i].denom()
                found = True
                break

                
### Franklin-Reiter Related Message Attack
Si on a 2 cryptés avec les mêmes clés et qu'il existe une relation afine du genre m2 = f(m) = a.m + b
                
### Copersmith and LLL algorithm
Pour petites valeurs de e
                
### Coppersmith short pad attack
Si on a deux messages quasi-identiques (la fin change) : m1 = 2**m.M + r1 et m2 = 2**m.M+r2 cryptés, on peut retrouver M avec juste la clé publique
    
### Partial Key Exposure attack
Si on connait 1/4 des bits de "d" et e<sqrt(N), on peut retrouver d (théorème de Coppersmith et de Boneh Durfee Frankel

   
### Attaque de boneh_durfee

