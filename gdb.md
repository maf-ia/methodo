<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - GDB</title>
</head>
[index](index.html) [cracking](cracking.html)

# gdb

## Intro

https://betterexplained.com/articles/debugging-with-gdb/

run : lance le programme
start : commence l'exécution et s'arrête au debut du main si present 

info file : affiche les infos sur le fichier (les différents points entrée et début de section)

Pour les strip file :(gdb) file info -> donne l'entry point, il suffit de faire un breakpoin b *0x... puis run
Pas de disassemble mais x/14i $pc (pour avoir 14 lignes instructions)
Ensuite, le push qui precede call   80483ec <__libc_start_main@plt> (initialisation lib C) est le pointeur vers le vrai début


watch * 0x... ==> ajoute une watch sur ecriture memoire (sinon rwatch pour lecture et awatch pour les 2)
Si plein sigtrap : handle SIGTRAP noprint nostop


## Suivi de l'exécution

On peut la stopper avec ctrl-c

Si on a les infos, on peut utiliser : (gdb) list pour afficher le code

Sinon (gdb) x/14i $pc  => 14 prochaines instructions

Modifier l'exécution : (gdb) set $pc=...

Pour afficher une chaine : (gdb) x/3s 0x... => Les 3 prochaines chaînes à partir de l'adresse...

Prochaine instruction 'ni', prochaine step 'si', modification avec : (gdb) set x = ...

Appeler une fonction existante : (gdb) call toto()

Retour à l'appelant : (gdb) finish

Pile d'exécution : (gdb) backtrace, changer de stack sur cette pile : (gdb) frame 2

Examiner la stack frame courante : (gdb) info frame / (gdb) info locals / (gdb) info args

## Voir la mémoire...

On peut utiliser print ou x

(gdb) x/x 0x... 	: en hexadécimal

(gdb) x/t 0x... 	: en binaire

(gdb) x/c 0x... 	: sous forme de caractère

(gdb) x/a 0x... 	: sous forme d'adresse

(gdb) x/s 0x... 	: sous forme de chaine (arrêt au \0 suivant)

On peut rajouter un chiffre pour en afficher plusieurs /4c : 4 caractères /2s : 2 strings...

## Variables environnement et registres

(gdb) info variable environ

(gdb) x/s *((char **)environ)

(gdb) info reg 

## Breakpoints

Poser un breakpoint : (gdb) b * 0x8048674

Lister les breakpoints : (gdb) info break / (gdb) i b

Supprimer un break point : (gdb) d break 2 (mettre le numero du breakpoint)

On peut mettre un breakpoint directement sur une fonction ou une méthode : (gdb) break func1 / (gdb) break TestClass::testFunc(int)

Si au lieu de break on utilise tbreak, cela met un breakpoint temporaire (s'arrêtera une fois et sera supprimé)

Il est possible de désactiver un breakpoint : (gdb) disable 2 

Il est possible d'ignorer un breakpoint un certain nombre de fois : (gdb) ignore 2 5

## Watchpoints

Comme des breakpoint, mais sur des variables : watch (écriture), rwatch (lecture) et awatch (lecture/écriture)

## Coredump

Relancer le program avec gdb : >gdb toto.bin puis (gdb) core core


