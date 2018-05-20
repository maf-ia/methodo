<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Stegano</title>
</head>
[index](index.html)

## Stegano

### Analyse basique 
- file filename (vérification type de fichier)
- strings filename (chaines en clair contenues... on peut imposer un nombre minimal de caractères)
- hachoir-metadata filename (il existe aussi d'autres exif tools)
- hachoir-subfile filename ==> détecte s'il y a des fichiers d'inclus/caché à l'intérieur
- foremost/binwalk : peut lui aussi détecter des fichiers inclus dans un autre

### Textes
- Début (lettre ou mot) de mot, début de ligne, début de phrase, etc
- Si le texte fait partie d'une image, certains signes (ponctuation ou "traces" sur le fond peuvent permettre de sélectionner certaines lettres
- Tous les "n" lettres ou tous les "n" mots
- Conserver les majuscules
- Alphabet bilitère de Lord Bacon. Ex: 
- Espaces entre les mots (surtout sur du html -> regarder la source)
- Une (longue) suite de chaînes en base64 ou base32... Il peut s'agir de bits cachés dans le padding (cf toolbox)
- Utilisation d'homoglyphes, ie le fait d’écrire un message en unicode avec des caractères de code différents mais dont le rendu est très proche (différents “e”, espaces…). On peut trouver sur [http://holloway.co.nz/steg/](http://holloway.co.nz/steg/) un algo pour cacher/lire les messages sur ce système

### Images 
- Zoomer chaque partie
- Il faut parfois redécouper et recomposer des morceaux d'image, façon puzzle
- Jouer sur la luminosité et le contraste, la sélection par couleur stricte (baguette magique gimp) pour détecter les écritures de type blanc sur blanc ou noir sur noir.
- Jouer sur les seuils, filtrer
- Regarder les metadata, les commentaires de l'image
- Editer en hexa et voir s'il n'y a pas des données lisibles (dans les data ou après la fin de l'image par exemple)
- Si des bandes de 2 couleurs : traduire en binaire
- Regarder la palette de couleur
- Regarder les valeurs hexa de chaque couleur : conversion en ascii par exemple
- LSB, plans couleur (stegsolve, steganabara pour une première approche, sinon outil maison).
- Pour le LSB utiliser zsteg : "zsteg imagefile" et sinon "zsteg imagefile -o ALL"
- L'image peut cacher une autre par transformée de Fourier, on peut alors utiliser des outils comme http://www.ejectamenta.com/Imaging-Experiments/fourierimagefiltering.html pour faire apparaître.
- Si l'image contient un texte, regarder si certaines lettres (ou mots) ne sont pas marqués (auquel cas les conserver uniquement)
- Extraire (par exemple pour les jpg) le thumbnail et l'examiner (voire le thumbnail du thumbnail...). Utiliser par exemple exiftool: [http://owl.phy.queensu.ca/~phil/exiftool/examples.html](http://owl.phy.queensu.ca/~phil/exiftool/examples.html) : "exiftool -b -ThumbnailImage image.jpg > thumb.jpg". Ou encore  "$exif2 l_image_de_base ­et le_nom_de_la_miniature_a_extraireegarder la vignette extraite". Peut aussi se faire avec hachoir-urwid
- [GIF] Si c'est un gif, ouvrir avec gimp par exemple pour voir toutes les images de l'animation (ou script de la toolbox ou "ffmpeg -i anim.gif img%05d.png")
- [PNG] Si c'est un png, regarder s'il n'y a pas des chunks inutilisés (qui contiendraient un autre fichier). Il existe sous windows http://entropymine.com/jason/tweakpng/ pour les manipuler, sinon voir scripts de la toolbox
- Si c'est un bmp (par exemple), regarder si la taille de l'image correspond à ce qui est indiqué dans le header (x*y*nbc couleurs). Le header a p-e ete trafique pour masquer une partie de l'image. 
- [BMP] Si c'est un bmp, il y a des octets de padding à la fin des lignes qui peuvent être utilisés pour cacher de l'info. Il est possible de les extraire avec zsteg (zsteg -o All alph1-surprise.bmp -E scanline > toto.bin) ou utiliser paddingBMP.py dans la toolbox
- Si les couleurs RGB de l'image (png, gif...) sont uniquement composées de 0x00, 0xC0 ou 0xFF, l'image peut avoir été générée par un programme depuis un mot, comme par exemple le langage piet
- Retrouver sur le web (google image ou https://www.tineye.com/) l'image originale pour faire un diff
- Sur une épreuve, en convertissant une image png en bmp on a pu lire ensuite un texte dans le bmp... le mécanisme est à creuser
- Notamment sur les images paraissant pixelisées, il y a la technique du "ctrl+a" (fonctionnait directement sous ie6) qui consiste à mélanger 2 images en utilisant un damier (un pizel sur deux en décalant à chauqe ligne). Cf gridImage.py dans la toolbox

#### Image brouillée
- Autostéréogramme (utiliser l'autostereogram solver de stegsolve ou online http://magiceye.ecksdee.co.uk/)
- Générée depuis un son ? (utiliser audacity et ses différents imports raw))
- Algorithme de type catmap (cf par exemple Arnold's Cat Map mais il y en a plusieurs autres) : c'est une transformation qui semble transformer l'image en random mais si on l'applique suffisamment de fois on revient sur l'image d'origine). Cf toolbox

### Sons
- Regarder avec audacity pour séparer les canaux
- Sur le signal : crête = 1, creux = 0
- Inverser l'ordre, amplifier, ralentir le son
- Spectrogramme (avec outil sonic-visualiser par exemple) : visuellement cela peut afficher un mot
- Différence LSB entre 2 canaux
- Sous windows, il existe un (vieil) outil appelé MP3Stego

### Autres fichiers
- Il est possible de cacher de l'info dans certains fichiers. Par exemple dans des fichiers compressés (zip, rar...) ou avec des chunks (png). Il faut alors reconstruire le header (souvent un CRC à calculer), modifier le type ou certains attributs...
- S'intéresser au format du fichier (son header...) pour voir s'il n'y a pas des différences.

### Videos
- Regarder chaque frame. On peut décomposer avec ffmpeg : $ffmpeg -i %06d.jpeg -f avi qqun.avi
Il existe des options comme -s 360x288 (size) -r 5 (rate) -an -b 360k ...

### Outils
- Steghide (date de 2003) : cache/extrait pour les formats JPEG, BMP, WAV and AU files. Utilisation pour décoder :
    $steghide extract -sf image.jpg -p passphrase -xf sol.txt
- outguess : cache/extrait des textes dans des images de type PPM, PNM ou JPEG
- OpenPuff (windows... non testé)
