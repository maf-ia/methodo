<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Reseau</title>
</head>
[index](index.html)

## Network

### TOR
reset TOR IP address:
sudo killall -HUP tor

### IRC
Enregistrer une conversation irc:

irssi
/set nick maf-ia
/set autolog on
/connect irc.root-me.org
/join #Root-Me

### Wireshark

### tshark
> tshark -r stego.pcap -T fields -e tcp.urgent_pointer


## Wifi

### aircrack-ng 
aircrack-* : suite d'outils

### weplab
crack de trames wifi aussi, via dictionnaire ou bf:
ex bf:
$weplab -b --alnum ch10-wep.pcap
