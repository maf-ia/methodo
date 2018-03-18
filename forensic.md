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

#### Créer un profil volatility

Le wiki de volatility l’explique plus en détails, mais il s’agit principalement de compiler pour le kernel cible un module kernel fourni par Volatility, avec les symboles de debug, puis de dumper les informations DWARF du module. Il faut donc aussi installer les headers du kernel cible, pour nous permettre de pouvoir compiler le module de Volatility. L’autre partie du profil correspond au System.map du kernel, créé à la compilation du kernel et fourni dans notre .deb de kernel Ubuntu. Au final:

$ apt-get install dwarfdump build-essential linux-headers-generic git
$ git clone https://github.com/volatilityfoundation/volatility.git
$ cd volatility/tools/linux
$ sudo make -C /lib/modules/4.4.0-57-generic/build CONFIG_DEBUG_INFO=y M=$PWD modules
$ dwarfdump -di ./module.o > module.dwarf
$ sudo zip Ubuntu1604-4.4.0-57.zip module.dwarf /boot/System.map-4.4.0-57-generic

Le zip « Ubuntu1604-4.4.0-57.zip » que nous venons de créer est donc le profil volatility correspondant à notre dump de RAM. Plaçons-le dans un répertoire « profiles » :

$ mkdir profiles
$ cp volatility/tools/linux/Ubuntu1604-4.4.0-57.zip profiles/

Reste maintenant à exploiter le dump avec volatility (nous avons au préalable récupéré la version déjà compilée de volatility pour Linux) :

$ ~/volatility_2.6_lin64_standalone --plugins=profiles/ --profile=LinuxUbuntu1604-4.4.0-57x64 -f dump.img --cache linux_pslist
...

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



