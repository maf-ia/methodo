<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
</head>
[index](index.html) [cracking](cracking.html)

## Android

### Cracker le lock pattern : 
gesture.key dans /data/system (avec adb par exemple)
Ensuite grep -i `xxd -p gesture.key` AndroidGestureSHA1.txt
(obtenu : wget 'http://www.android-forensics.com/tools/AndroidGestureSHA1.rar' puis unrar AndroidGestureSHA1.rar)
xxd : convertit en hexa et-i ignore la casse
Car en fait il s'agit d'un simple sha-1 de la combi de touche, sans salt. Du coup ce fichier donne toutes les combi possibles.

### Interpreter :

- dezipper le apk
- Obtenir le .jar : ~/Documents/hack/resources/tools/Cracking/Android/dex2jar-0.0.9.15/dex2jar.sh classes.dex
(http://code.google.com/p/dex2jar/)
- dezipper le jar
- aller dans le répertoire où se trouvent les .class et les lire avec jd-gui:
~/Documents/hack/resources/tools/Cracking/Android/jd-gui-0.3.5.linux.i686/jd-gui *.class

### Installer un apk sur l'emulateur : 

- lancer l'emulateur (par exemple depuis la version d'eclipse pour Android)
- ~/Documents/root-me/Android/adt-bundle-linux-x86/sdk/platform-tools/adb install toto.apk
- Sur l'emulateur, rafraichir la liste des apps

Si erreur "Failure [INSTALL_FAILED_UID_CHANGED]" => se connecter avec adb shell et aller dans /data/data trouver le répertoire de l'appli en question et le supprimer ainsi que son contenu (pb d'id de droit sur ce repertoire)

- Desinstaller : mettre le nom complet du package :
~/Documents/root-me/Android/adt-bundle-linux-x86/sdk/platform-tools/adb uninstall com.example.simpledisplay

### Lire les xml binaires 

- les ressources et le manifeste :
../../Android/androguard-1.9/androaxml.py -i ./AndroidManifest.xml 256374891;01 04 05 02 06 03 07 08 00;2C3422D33FB9DD9CDE87657408E48F4E635713CB
Mettre -o xxx pour un fichier de sortie...

- Autre possibilite, non encore testee :
aapt d xmltree apk_file_name res/layout/activity_main.xml
(can be found in android-sdk-dir/build-tools)
ou plus simplement :
aapt l -a toto.apk

- ClassyShark
Cet outil permet d'analyser les apk (avec GUI), et notamment les AndroidManifest.xml

### (De)assemlage smali 

- java -jar ~/Documents/root-me/Android/smali/baksmali-1.4.2.jar -o . classes.dex

- Reassemblage avec smali au lieu de backsmali ?)
Dans rép racine : java -jar ~/Documents/root-me/Android/smali/smali-1.4.2.jar -o classes.dex *.smali
Dans ./META-INF/ virer les fichiers CERT.* ...
Puis zipper en apk : zip -r ../uposax.apk ./*
Signer (cf ci-dessous)
Eventuellement retirer l'ancien package et réinstaller nouveau

- Sign apk
Si besoin de clé : keytool -genkey -v -keystore my-release-key.keystore -alias alias_name -keyalg RSA -validity 10000
Puis : jarsigner -verbose -sigalg MD5withRSA -digestalg SHA1 -keystore ./my-release-key.keystore ./uposax.apk alias_name

### Divers

* Pb Eclipse freeze at start :
Dans le répertoire du workspace : 
    cd .metadata/.plugins
    mv org.eclipse.core.resources org.eclipse.core.resources.bak
    Start eclipse. (It should show an error message or an empty workspace because no project is found.)
    Close all open editors tabs.
    Exit eclipse.
    rm -rf org.eclipse.core.resources (Delete the newly created directory.)
    mv org.eclipse.core.resources.bak/ org.eclipse.core.resources (Restore the original directory.)
    Start eclipse and start working. :-)

## Langage smali

1. Faire une log de string: 
const-string v2, "root-me-1"
const-string v3, "Dans if"
invoke-static {v2, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

2. Faire une log d'un int: 
new-instance v3, Ljava/lang/StringBuilder;
invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V
const/4 v2, 0x5
invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;
invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
move-result-object v3
const-string v2, "root-me-1"
invoke-static {v2, v3}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I