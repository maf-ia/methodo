<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html)

## Stegano

### Analyse basique 
- file filename (vérification type de fichier)
- strings filename (chaines en clair contenues... on peut imposer un nombre minimal de caractères)
- hachoir-metadata filename (il existe aussi d'autres exif tools)
- hachoir-subfile filename ==> détecte s'il y a des fichiers d'inclus/caché à l'intérieur

### Textes
- Début (lettre ou mot) de mot, début de ligne, début de phrase, etc
- Si le texte fait partie d'une image, certains signes (ponctuation ou "traces" sur le fond peuvent permettre de sélectionner certaines lettres
- Tous les "n" lettres ou tous les "n" mots
- Conserver les majuscules
- Alphabet bilitère de Lord Bacon. Ex: 
- Espaces entre les mots (surtout sur du html -> regarder la source)
- Utilisation d'homoglyphes, ie le fait d’écrire un message en unicode avec des caractères de code différents mais dont le rendu est très proche (différents “e”, espaces…). On peut trouver sur [http://holloway.co.nz/steg/](http://holloway.co.nz/steg/) un algo pour cacher/lire les messages sur ce système

### Images 
- Zoomer chaque partie
- Il faut parfois redécouper et recomposer des morceaux d'image, façon puzzle
- Jouer sur la luminosité et le contratse
- Jouer sur les seuils, filtrer
- Si c'est un gif, ouvrir avec gimp par exemple pour voir toutes les images de l'animation
- Si des bandes de 2 couleurs : traduire en binaire
- Regarder la palette de couleur
- Regarder les valeurs hexa de chaque couleur : conversion en ascii par exemple
- LSB, plans couleur (stegsolve, steganabara pour une première approche, sinon outil maison).
- Pour le LSB utiliser zsteg : "zsteg imagefile" et sinon "zsteg imagefile -o ALL"
- Si l'image contient un texte, regarder si certaines lettres (ou mots) ne sont pas marqués (auquel cas les conserver uniquement)
- Extraire (par exemple pour les jpg) le thumbnail et l'examiner (voire le thumbnail du thumbnail...). Utiliser par exemple exiftool: [http://owl.phy.queensu.ca/~phil/exiftool/examples.html](http://owl.phy.queensu.ca/~phil/exiftool/examples.html) : "exiftool -b -ThumbnailImage image.jpg > thumb.jpg". Ou encore  "$exif2 l_image_de_base ­et le_nom_de_la_miniature_a_extraireegarder la vignette extraite". Peut aussi se faire avec hachoir-urwid
- Si c'est un png, regarder s'il n'y a pas des chunks inutilisés (qui contiendraient un autre fichier)
- Si c'est un bmp (par exemple), regarder si la taille de l'image correspond à ce qui est indiqué dans le header (x*y*nbc couleurs). Le header a p-e ete trafique pour masquer une partie de l'image
- L'image peut avoir été générée par un programme depuis un mot, comme par exemple le langage piet
- Retrouver sur le web (google image ou https://www.tineye.com/) l'image originale pour faire un diff

#### Image brouillée
- Autostéréogramme (utiliser stegsolve ?)
- Générée depuis un son ? (utiliser audacity et ses différents imports raw))
- Algorithme de type catmap (cf par exemple Arnold's Cat Map mais il y en a plusieurs autres) : c'est une transformation qui semble transformer l'image en random mais si on l'applique suffisamment de fois on revient sur l'image d'origine)

### Sons
- Regarder avec audacity pour séparer les canaux
- Sur le signal : crête = 1, creux = 0
- Inverser l'ordre, amplifier, ralentir le son
- Spectrogramme (avec outil sonic-visualiser par exemple) : visuellement cela peut afficher un mot
- Différence LSB entre 2 canaux
- Sous windows, il existe un (vieil) outil appelé MP3Stego

### Videos
- Regarder chaque frame

### Outils
- Steghide (date de 2003) : cache/extrait pour les formats JPEG, BMP, WAV and AU files
- OpenPuff (windows... non testé)