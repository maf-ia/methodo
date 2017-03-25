<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html) [cracking](cracking.html)

### gdb

https://betterexplained.com/articles/debugging-with-gdb/


run : lance le programme
start : commence l'exécution et s'arrête au debut du main si present 

info file : affiche les infos sur le fichier (les différents points entrée et début de section)


Pour les strip file :(gdb) file info -> donne l'entry point, il suffit de faire un breakpoin b *0x... puis run
Pas de disassemble mais x/14i $pc (pour avoir 14 lignes instructions)
Ensuite, le push qui precede call   80483ec <__libc_start_main@plt> (initialisation lib C) est le pointeur vers le vrai début


watch * 0x... ==> ajoute une watch sur ecriture memoire (sinon rwatch pour lecture et awatch pour les 2)
Si plein sigtrap : handle SIGTRAP noprint nostop


--- Afficher code à exécuter ---

x/14i $pc  => 14 prochaines instructions

Prochaine instruction 'ni'


--- Voir registres ---
info reg 

print /x $REG 	: 	affiche le contenu du registre REG en hexadécimal

print /t $REG 	: 	affiche le contenu du registre REG en binaire

print /c $REG 	: 	affiche le contenu du registre REG sous forme de caractère

print /a $REG 	: 	affiche le contenu du registre REG sous forme d'adresse


set $pc=...

#### Variables environnement

info variable environ

x/s *((char **)environ)