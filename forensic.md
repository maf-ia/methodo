<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Forensic</title>
</head>
[index](index.html)

## Forensic

- testdisk : pour analyser une image disque et retrouver des fichiers perdus par exemple
- foremost : retrouve les fichiers effaces d'une image
- extundelete : specialise pour les partitions ext3 et ext4
- binwalk : recherche d'images binaires et exe intégrés
    Exemple pour extraire que les jpg : 
        $binwalk --dd='jpeg:jpg' file.bin
    Tout extraire:
        $ binwalk --dd='.*' file.bin
- autospy : existe sous windows (executable) ou linux (accessible via site web en local...). Les dernières versions sur la même image ne semble pas être analysées exactement de la même manière


### Volatility

#### Generalites

- Ajouter des plugins : $volatility --plugins=dir1,dir2 ...
- Ajouter des profiles : Dans plugins/overlays/Linux ... ou avec l'option plugins
- volatility  -f dumpfile imageinfo

#### Volatilty Windows

- volatility -f dumpfile --profile=Win7SP1x86 envars
- volatility -f dumpfile --profile=Win7SP1x86 psscan
- volatility -f dumpfile --profile=Win7SP1x86 hivelist
- volatility -f dumpfile --profile=Win7SP1x86 cmdscan
- volatility -f dumpfile --profile=Win7SP1x86 consoles
- volatility -f dumpfile --profile=Win7SP1x86 hashdump : retourne les hash ntlm et lm
- volatility -f dumpfile --profile=Win7SP1x86 netscan  : les connections réseau
- volatility -f dumpfile --profile=Win7SP1x86 filescan  : les fichiers...
- volatility -f dumpfile --profile=Win7SP1x86 dumpfiles -Q <adr filescan> -D ./ : extraire un fichier

#### Volatility Linux

- volatility -f dumpfile --profile=xxx linux_cpuinfo
- volatility -f dumpfile --profile=xxx linux_psaux
- volatility -f dumpfile --profile=xxx linux_...

### Créer une cle usb bootable

- (sudo) unetbootin 
- Choisir son iso (ou sa distrib) et suivre les instructions

### Forensic outlook
- Avec autopsy
- Avec la libpst dont readpst, convertir en mbox...
- DFF(https://github.com/arxsys/dff) - mais projet arrêté
- Encase (payant)
- PST viewer PRO (version eval...)

### Outils pdf
- www.extractpdf.com : extrait certaines données des pdf... 
- pdfextract : extrait les différents streams d'un pdf
- Les outilfs $pdfto... fonctionnent aussi


### Autres outils

- [bstrings](http://binaryforay.blogspot.fr/) (sorte de strings pour win)
- ewftools : outils pour manipuler les fichiers images (mémoire, disque...) créés par EnCase
- bmc-tools : outil pour retrouver les images du caches RDP (conection bureau à distance)
- Parfois le fichier correspond à une image corrompue. Il faut corriger (en regardant le format) ou ajouter simplement le bon header



