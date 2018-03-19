<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Cracking</title>
</head>
[index](index.html)

## Cracking

### Exploit

- pscan : permet d'analyser statiquement du code source pour déceler des failles de sécurité comme les "format strings"
- flawfinder : analyse statique du code pour la sécurité
- rats : analyse statique du code pour la sécurité

- ROPgadget pour contruire des ROP (script python) : https://github.com/JonathanSalwan/ROPgadget

### Symbolic execution

Permet d'explorer les chemins d'exécution possibles d'un programme informatique à partir des symboles contenus dans son code source. Elle diffère de l’exécution concrète qui ne suit qu'un seul des chemins possibles. Alors que l’exécution concrète met directement à jour les variables en mémoire, l’exécution symbolique enregistre les formules logiques liant les variables entre elles. Le but est d'analyser statiquement un programme pour trouver des bugs ou prouver certaines propriétés du programme. Il s'agit d'une interprétation abstraite d'un programme. 
Le framework Z3 de microsoft research semble a la pointe. Il y a un outil manticore qui semble l'utiliser (https://github.com/trailofbits/manticore) :
./manticore --proc 2 ./my_binary

D'autres outils, ciblant différentes target, sont cités sur https://en.wikipedia.org/wiki/Symbolic_execution

### Assembleur
Référentiel des opcodes (notamment x86) : [www.sandpile.org/x86/](http://www.sandpile.org/x86/)

- Commande call 0x...
push eip (next inst pour le retour)
eip = 0x...

- test   %eax,%eax : compare si vaut 0

- Commande pop :
Lit à l'adresse esp puis increment esp

- Commande "leave":
mov esp,ebp  (copie ebp dans esp)
pop ebp

- Commande ret:
pop eip

### Cracking de binaires 

#### Applications Linux

##### Analyse statique

- file Affiche différentes informations sur le fichier ELF

- readelf : Permet d'afficher différents informations concernant un fichier ELF

- dumpelf : Dump toutes les informations sur la structure d'un fichier ELF en équivalent d'une structure en C

- lddtree : Montre l’arbre des dépendances d'un fichier ELF

- checksec : script bash permettant d'afficher les protections (ou pas) d'un binaire : RELRO (relocation read-only, NX (non executable segment), Canary, PIE (position independent executable)...

- objdump

- scanelf

- edb

- IDA

##### Outils
- gdb xxx. [Utilisation de gdb](gdb.html)
- ltrace xxx : Trace library calls of a given program.
- strace xxx : trace system calls and signals
- LD_PRELOAD :

Compiler une lib shared : gcc -shared -fPIC -o fake.so fake.c
LD_PRELOAD à l'execution permet de preloader de fausse shared lib en remplacement
Exemple:  strace -E LD_PRELOAD=./fake.so ./program

- objdump - display information from object files.

objdump -D ./hackme > out.asm
utiliser -d pour une version abregee, sans les data notamment
Option -M intel ou -M att selon la préférence d'affichage (intel ou AT&T)

- decompiler: 

http://boomerang.sourceforge.net ou http://www.backerstreet.com/rec/rec.htm ??

https://retdec.com

- Utiliser readelf pour decouvrir les segments
ex: readelf -a <myprog> | grep strcpy

hte -> Navigateur de ELF (installé) - Parfois appelé ht

elfsh, ndisasm et elfgrep ??


Connaitre l'adresse printf dans GOT :
> objdump -R ./binary9 | grep printf
08049760 R_386_JUMP_SLOT   printf


env -i EGG=`python -c "print '0x....




Il existe d'autres disassembler, notamment à inclure dans du code python : capstone ou encore distorm3
keystone peut etre utilise pour assembler
    
#### Applications Windows

##### .Net

Il est possible d'utiliser ILSpy ou dotPeek (chez JetBrains) ou .NetReflector (devenu payant, il faut retrouver une vieille version mais du coup n'a pas évolué)
    
#### [Shellcode](shellcode.html)
 
#### Applications Mac

Il existe Hopper Disassembler, une version de démo (limitée à 30 minutes consécutives) disponible sous windows et linux.
Sinon il y a les otools, assez proche des binutils (objdump...) de linux.

    
### Exploit d'application

####- Format string :
- %08X : affiche la stack par 4 octets
- %s : affiche la valeur pointée par l'adresse en mémoire, on peut alterner des %x et %s car si ce que pointe %s est hors zone, ca crashe
- %n : écrit le nombre de caractères déjà affichés, à l'adresse pointée
Generalement si on met suffisamment de %x on arrive à pointer le début de la chaîne qu'on vient d'entrer et donc si on a bien choisi les valeurs, cela permet de pointer où on veut.
- Si on ne veut pas mettre les premiers %x, on peut utiliser pour le %n : %5$n (saute à la 5ème valeur pointée)
- %XXXXd. Cela génère un entier de taille XXXX (mais on ne peut pas mettre de valeurs trop grandes)
- %hn : comme %n mais écrit des valeurs de 2 octets (on doit donc écraser une adresse en 2 fois (en décalage de 2))


### [Cracking d'appli Android](android.html)

### Cracking Excel
J'ai trouvé xlcrack qui a fonctionné

### Cracking Documents
Il y a une macro OpenOffice qui fait une attaque par dictionnaire : OOoPasswordCracker

### Cracking PDF
Il existe pdfcrack (par exemple attaque par dictionaire)

### Cracking Flash
J'utilise ffdec qui permet d'afficher les ressources et codes

### Cracking Java
Il existe des decompilers comme jad : "jad xx.class" => genere un fichier contenant le code source ou jd-gui (fourni une interface graphique, fonctionne aussi avec les .jar).
A noter qu'il existe des outils en ligne performants comme "http://www.javadecompilers.com"
Sous linux on peut lancer en local un applet avec "appletviewer" (creer un html avec une balise <applet code="xx.class" />)

### Cracking SAM (mots de passe windows)
Sous linux on peut examiner ces fichier avec reglookup ou de manière plus fine avec chntpw (permet de naviguer). Ex 'chntpw SAM -i' (mode interactif)
Le plus simple pour les mots de passe est ophcrack qui donne les comptes avec leur LM hash et/ou NT hash (à noter qu’en LM on n’a pas la casse. Pour connaitre la casse il faut en fait attacker avec le NT Hash). Il existe aussi des sites online pour ça.

### Cracking ARM
Install :
qemu-system-arm -m 256 -M versatilepb  -kernel ./vmlinuz-2.6.32-5-versatile -initrd ./initrd-2.6.32-5.gz -hda ./armdisk.img -append "root=/dev/sda1"

qemu-system-arm -m 256 -M versatilepb          -kernel ./vmlinuz-3.2.0-4-versatile          -initrd ./initrd.gz          -hda ./armdisk.img -append "root=/dev/ram"

=> Accès au fs arm...
sudo mount -o loop,offset=$[2048*512] ./armdisk.img  ./mount 

Lancer:
qemu-system-arm -m 256 -M versatilepb -kernel vmlinuz-2.6.32-5-versatile -initrd initrd.img-2.6.32-5-versatile -hda armdisk.img -append "root=/dev/sda1" 
-net user ?
-netdev user,id=mynet0,net=192.168.76.0/24,dhcpstart=192.168.76.9 ?

