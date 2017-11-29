<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[Hacking](hacking.html) 

## Generalites

### Utilisation interactive

msf> show : liste tous les modules

msf> show exploits 

msf> show auxiliary

msf> use <module> : charge un module

msf> back : quitte module

msf> search <item> : retourne tout ce qui a trait à ce sujet, ex: mysql pour les exploits sur mysql...

set/unset ou setg/unsetg pour une portée globale et non limitée au module

save : sauve le paramétrage

### Base de données

## Recherche de vulnerabilités
### Module nexpose
- > load nexpose
- > nexpose_connect
- > nexpose_scan

### Module nessus
- > load nessus
- > nessus_connect

