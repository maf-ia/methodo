<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html)

## Forensic

testdisk : pour analyser une image disque et retrouver des fichiers perdus par exemple

foremost : retrouve les fichiers effaces d'une image

extundelete : specialise pour les partitions ext3 et ext4

binwalk : recherche d'images binaires et exe intégrés

autospy : existe sous windows (executable) ou linux (accessible via site web en local...). Les dernières versions sur la même image ne semble pas être analysées exactement de la même manière

www.extractpdf.com : extrait certaines données des pdf... Les outilfs $pdfto... fonctionnent aussi

### Forensic outlook
- Avec autopsy
- Avec la libpst dont readpst, convertir en mbox...
- DFF(https://github.com/arxsys/dff) - mais projet arrêté
- Encase (payant)
- PST viewer PRO (version eval...)

### Volatility
volatility  -f dumpfile imageinfo
volatility -f dumpfile --profile=Win7SP1x86 envars
volatility -f dumpfile --profile=Win7SP1x86 psscan
volatility -f dumpfile --profile=Win7SP1x86 hivelist
volatility -f dumpfile --profile=Win7SP1x86 cmdscan
volatility -f dumpfile --profile=Win7SP1x86 consoles
volatility -f dumpfile --profile=Win7SP1x86 hashdump : retourne les hash ntlm et lm

### Créer une cle usb bootable
(sudo) unetbootin 
Choisir son iso (ou sa distrib) et suivre les instructions

### Autres outils

- [bstrings](http://binaryforay.blogspot.fr/) (sorte de strings pour win)



