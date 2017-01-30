# XORcist crackme

* URL - https://github.com/XORcists/crackme.git

## 0x00

running the program first

``` bash
[root:~/crackme]# ./0x00
Enter password: password
Noob! Shame on you!
```

### Solution

opening the binary in radare2, seeking to main and printing the disassembly shows the following

```
[0x004005b0]> s main
[0x0040069d]> pdf
            ;-- main:
	    / (fcn) sym.main 130
	    |   sym.main ();
	    |           ; var int local_20h @ rbp-0x20
	    |           ; var int local_8h @ rbp-0x8
	    |           ; DATA XREF from 0x004005cd (entry0)
	    |           0x0040069d      55             push rbp
	    |           0x0040069e      4889e5         mov rbp, rsp
	    |           0x004006a1      4883ec20       sub rsp, 0x20
	    |           0x004006a5      64488b042528.  mov rax, qword fs:[0x28]    ; [0x28:8]=0x11c0 ; '('
	    |           0x004006ae      488945f8       mov qword [rbp - local_8h], rax
	    |           0x004006b2      31c0           xor eax, eax
	    |           0x004006b4      bfc4074000     mov edi, str.Enter_password: ; "Enter password: " @ 0x4007c4
	    |           0x004006b9      b800000000     mov eax, 0
	    |           0x004006be      e89dfeffff     call sym.imp.printf        ; int printf(const char *format);
	    |           0x004006c3      488d45e0       lea rax, qword [rbp - local_20h]
	    |           0x004006c7      4889c6         mov rsi, rax
	    |           0x004006ca      bfd5074000     mov edi, 0x4007d5           ; "%s"
	    |           0x004006cf      b800000000     mov eax, 0
	    |           0x004006d4      e8c7feffff     call sym.imp.__isoc99_scanf; int scanf(const char *format);
	    |           0x004006d9      488d45e0       lea rax, qword [rbp - local_20h]
	    |           0x004006dd      bed8074000     mov esi, str.secret         ; "secret" @ 0x4007d8
```

intresting that location `0x004006dd` has a string of `"secret"`

trying this as the password works

``` bash
[root:~/crackme]# ./0x00
Enter password: secret
Yay! You cracked the code!
```

to improve this i can change the secret using radare2 like so

```
[0x004007d8]> pd
	      ;-- str.secret:
	      ; DATA XREF from 0x004006dd (sym.main)
0x004007d8     .string "secret" ; len=7
	       ;-- str.Yay__You_cracked_the_code_:

..snip..

[0x004007d8]> w foobar
[0x004007d8]> q

[root:~/crackme]# ./0x00
Enter password: secret
Noob! Shame on you!

[root:~/crackme]# ./0x00
Enter password: foobar
Yay! You cracked the code!
```

## 0x01

running this program for the first time shows the following

``` bash
[root:~/crackme]# ./0x01
XORcists crackm3 lvl-2
Enter password:password
Password incorrect!
```

### Solution

again opening it up in radare2 and see where the password is evaluated

```
|           0x00400626      e8c5feffff     call sym.imp.__isoc99_scanf; int scanf(const char *format);
|           0x0040062b      8b45f8         mov eax, dword [rbp - local_8h]
|           0x0040062e      3945fc         cmp dword [rbp - local_4h], eax ; [0x13:4]=256
|       ,=< 0x00400631      750c           jne 0x40063f
|       |   0x00400633      bf1f074000     mov edi, str.Password_correct_ ; "Password correct! " @ 0x40071f
|       |   0x00400638      e873feffff     call sym.imp.puts           ; loc.imp.__gmon_start__-0x30
|      ,==< 0x0040063d      eb0a           jmp 0x400649
|      ||   ; JMP XREF from 0x00400631 (sym.main)
|      |`-> 0x0040063f      bf32074000     mov edi, str.Password_incorrect_ ; "Password incorrect! " @ 0x400732
|      |    0x00400644      e867feffff     call sym.imp.puts           ; loc.imp.__gmon_start__-0x30
|      |    ; JMP XREF from 0x0040063d (sym.main)
|      `--> 0x00400649      b800000000     mov eax, 0
```

the `jne 0x40063f` will always result in the password being incorrect, to try and bypass this i can write `nop's` so that the next operation is executed resulting in the password always being correct

```
[0x004005ed]> s 0x00400631
[0x00400631]> wao nop
[0x00400631]> q

[root:~/crackme]# ./0x01
XORcists crackm3 lvl-2
Enter password:password
Password correct!

[root:~/crackme]# ./0x01
XORcists crackm3 lvl-2
Enter password:anything
Password correct!
```
