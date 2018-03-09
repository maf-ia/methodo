<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - John the ripper</title>
</head>
[Crypto](crypto.html)

## Exemple de base
./john htaccess_pwd.txt --wordlist=rockyou.txt

## Documentation John

(a simplifier)

These examples are to give you some tips on what John's features can be
used for. Some of them may not be obvious, I'm sorry if others are, but
anyway, I just got tired of answering questions.

 Command Line
--------------

1. First, you need to get a copy of your password file. If you got shadow
passwords, then (as root):

	unshadow /etc/passwd /etc/shadow > passwd.1

or similar should do (replace the filenames as needed, and make sure that
your combined password file isn't readable by others). Otherwise, just:

	cp /etc/passwd passwd.1

If you're going to crack AFS or NT passwords, then use 'unafs' or Jeremy
Allison's PWDump (ftp://samba.anu.edu.au/pub/samba/pwdump/), respectively.

2. Assume you just got a password file, 'passwd.1', and want to crack it.
The simplest way is to use the default order of cracking modes:

	john passwd.1

This will try "single crack" mode first, then use a wordlist with rules,
and finally go for incremental mode. Read doc/MODES for more information
on these modes.

It is highly recommended that you obtain a larger wordlist, and edit the
'Wordfile =' line in ~/john.ini before running John.

3. Now, you got some passwords cracked, they are saved in ~/john.pot. You
want to retrieve them:

	john -show passwd.1

If the account list gets large and doesn't fit on the screen, you can, of
course, use output redirection. (There's intentionally no example here, a
few people have asked for one, but they shouldn't be using John anyway.)

Now, you may notice that many accounts have a disabled shell, you can make
John ignore these (assume that shell is called '/etc/expired'):

	john -show -shells:-/etc/expired passwd.1

or, shorter, but will also match '/any/path/expired':

	john -show -shells:-expired passwd.1

or, if you also want to ignore some other shell, say '/etc/newuser':

	john -show -shells:-expired,newuser passwd.1

(Note: the above syntax has changed since version 1.4 so that it's more
logical and shorter to type.)

To check if any root (uid 0) accounts got cracked:

	john -show -users:0 passwd.1

or, to check for cracked root (uid 0) accounts in all the files:

	john -show -users:0 passwd.*

To display the root (login 'root') account only:

	john -show -users:root passwd.1

And finally, to check for privileged groups:

	john -show -groups:0,1 passwd.1

4. You might prefer to manage the cracking modes manually instead. It is
wise to start with "single crack" mode:

	john -single passwd.1

or, since options can be abbreviated (however, I'll be using full names
for most options in these examples):

	john -si passwd.1

If you have more files to crack, better to load them at the same time:

	john -single passwd.1 passwd.2

or even:

	john -single passwd.*

5. To catch more complicated (but still weak) passwords, you can use more
powerful cracking modes. First, try a wordlist:

	john -w:words.lst passwd.1

or, you might prefer to use the GNU-style long options syntax, say, to use
file name completion in bash:

	john --wordfile=words.lst passwd.1

or, shorter to type:

	john -w=words.lst passwd.1

or, with rules enabled (slower, but more powerful; this is what you should
use if you're trying to locate almost all the weak passwords):

	john -w:words.lst -rules passwd.1

or, if you got a lot of spare disk space to trade for performance:

	john -w:words.lst -rules -stdout:8 | unique huge.lst
	john -w:huge.lst passwd.1

This is going to take some time, so you will probably want to continue
cracking in the background. You can simply disconnect, or close your
xterm: John will ignore the SIGHUP and continue running. Alternatively,
you might prefer to start it like this, and then logout:

	nice -n 20 john -w:words.lst -rules passwd.1 &

Finally, to make John have even less impact on other processes, you might
want to set the 'Idle =' option in ~/john.ini.

To only crack accounts with a good shell (in general, the shell, user and
group filters described above work for all the cracking modes also):

	john -w:words.lst -rules -shells:sh,csh,tcsh,bash passwd.1

Like with all the other cracking modes, faster to crack all the files you
need cracked simultaneously:

	john -w:words.lst -rules passwd.*

You can crack some passwords only. This will try cracking all root (uid 0)
accounts in all the password files:

	john -w:words.lst -rules -users:0 passwd.*

Alternatively, you may wish not to waste the time cracking your very own
passwords, if you're sure they're uncrackable:

	john -w:words.lst -rules -users:-root,solar passwd.*

Sometimes it is useful to split your password files into two parts which
you crack separately, like:

	john -w:words.lst -rules -salts:2 passwd.*
	john -w:words.lst -rules -salts:-2 passwd.*

This will make John try salts with two or more passwords faster, and then
try the rest. Total cracking time will be about the same, but you will get
some passwords cracked earlier, and may not need the rest. Also, you might
want to try all the accounts with a small wordlist, and only those that
you can try faster (with '-salts:2') with a larger one. Often it is better
to use a larger value than 2 for '-salts' (sometimes even as high as 1000
will do, indicating a problem with your password changing program though),
adjust it for your particular case.

Note that the default wordlist rules include ':' (which means "try words
as they are in the list") as the first line. If you already ran through a
wordlist without using rules, and then decided to try the same wordlist
with rules also, you'd better comment this line out.

6. The most powerful cracking mode in John is called "incremental" (not a
proper name, but kept for historical reasons). You can simply run:

	john -i passwd.1

This will use the default incremental mode parameters, which are defined
in ~/john.ini's [Incremental:All] section. In the configuration file
supplied with John these parameters are to use the full 95 character set,
and to try all possible password lengths, from 0 to 8. (By zero password
length I mean a hashed empty string, this sometimes happens.) Don't expect
this to terminate in a reasonable time (unless all the passwords were weak
and got cracked), read doc/MODES for an explanation.

In some cases it is faster to use some other pre-defined incremental mode
parameters and only crack simpler passwords, from a limited charset. The
following command will try 26 different characters only, passwords from
'a' to 'zzzzzzzz':

	john -i:alpha passwd.1

Again, you can crack root accounts only and use some other John's features
with the incremental mode. This command will try cracking all root (uid 0)
accounts in all the password files, and only those of them that produce
matching salts, so you get at least twice the performance -- if you have a
lot of password files (like 100+ of them, named '*.pwd'), otherwise there
will probably be no roots with matching salts:

	john -i -users:0 -salts:2 *.pwd

7. If you got a password file and already have a lot of passwords cracked
or sniffed, and the passwords are unusual, then you might want to generate
a new charset file, based on characters from that password file only:

	john -makechars:custom.chr passwd.1

Then use that new file for the incremental mode.

If you got many password files from your country, your university, etc,
it might be useful to use all of them for the charset file that you then
use to crack more passwords in these files, or some other files from the
same place:

	john -makechars:custom.chr passwd.1 passwd.2
	[ Add your custom incremental mode to ~/john.ini now. See below. ]
	john -i:custom passwd.3

You can use some pre-defined or custom word filters when generating the
charset file, to make it only try some simpler words:

	john -makechars:my_alpha.chr -external:filter_alpha passwd.1

If your ~/john.pot file got large enough (or if you don't have any charset
files at all), you might want to use it for new main charset files:

	john -makechars:all.chr
	john -makechars:alpha.chr -external:filter_alpha
	john -makechars:digits.chr -external:filter_digits
	john -makechars:lanman.chr -external:filter_lanman

In the example above, John will overwrite the charset files with new ones
that are based on your entire ~/john.pot (John uses the entire file if you
don't specify any password files). Note that the word filters used here
are pre-defined in ~/john.ini supplied with John, for your convenience.

8. Finally, you might want to mail all the users who got weak passwords,
to tell them to change the passwords. It's not always a good idea though
(unfortunately, lots of people seem to ignore such mail, it can be used
as a hint for crackers, etc), but anyway, I'll assume you know what you're
doing. Edit the 'mailer' script supplied with John: the message it sends,
and possibly the mail command (especially if the password file is from a
different box than you got John running on). Then run:

	mailer passwd.1

 Configuration File
--------------------

1. Assume you notice that in some password file a lot of users have their
passwords set to login names with '?!' appended. Then you just make a new
"single crack" mode rule (see doc/RULES for information on the syntax),
and place it somewhere near the beginning:

	[List.Rules:Single]
	$?$!

Hint: if you want to temporarily comment out all the default rules, you
can simply rename the section to something John doesn't use, and define
a new one with the section's old name, but be sure to leave the 'list.'
part of the name, so that you don't get a parse error.

All the same applies to the wordlist rules also.

2. If you generate a custom charset file (described above) you will also
need to define a ~/john.ini section with the incremental mode parameters.
In the simplest case it will be like this (where 'Custom' can be replaced
with any name you like):

	[Incremental:Custom]
	File = custom.chr

This will make John use characters that were in passwords used to generate
the charset file only. To make John try some more characters, add:

	Extra = !@#$%

These extra characters will then be added, but still considered the least
probable. If you want to make sure that, with your extra characters, John
will try all the 95 characters, you can add:

	CharCount = 95

This will make John print a warning if it only has less than 95 characters
in its charset.

You can also use CharCount to limit the number of different characters
that John tries, even if the charset file has more:

	CharCount = 25

If you didn't use any filters when generating the charset file, setting
CharCount that low will most likely disable some rare characters, and make
John try complicated long passwords earlier. However, the default length
switching is usually smart enough so that you shouldn't need such a trick.

To make John try passwords of some lengths only, use the following lines:

	MinLen = 6
	MaxLen = 8

Setting 'MinLen' high, as in the example above, is reasonable if shorter
passwords weren't allowed to set on the machine you got the password file
from (however, note that root can usually set any password for any user).

On the contrary, you might want to set 'MaxLen' low if you think there's
a lot of short passwords.

3. Another example: a lot of users at some site use short duplicated words
as their passwords, such as "fredfred". As the number of such potential
passwords is fairly low, it makes sense to code a new external cracking
mode that tries them all, up to some length.

You can find the actual implementation of such a cracking mode with lots
of comments in the default ~/john.ini supplied with John. See doc/EXTERNAL
for information on the language used.
