<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - App</title>
</head>
[index](index.html)

## Applicatif

### Shell linux

- sudo -l  : Permet de connaître d'éventuels droits donnés spécifiquement

### Firefox

Mots de passes stockés dans .mozilla : signos.sqlite, crypté avec key3.db
Si on les récupère, il suffit de les mettre dans son propre répertoire et de faire Edition/Préférences/Sécurité - “Mots de passe enregistrés” puis “Afficher le mot de pase”.
Sinon, il existe mozilla_password_dump (linux) ou FirePassword (windows)

### VNC

Dans .vnc on récupère le fichier où est stocké les mots de passe.
Lire avec vncrack (./vncrack -C passwd_vnc) ou en ligne http://tools88.com/safe/vnc.php



