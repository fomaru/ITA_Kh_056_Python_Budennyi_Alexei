Command line output and comments

Task.Linux.1
Task1.Part1

alex@alex-Vostro-3558:~/Learning$ su
Password: 
root@alex-Vostro-3558:/home/alex/Learning#

root@alex-Vostro-3558:/home/alex/Learning# passwd
New password: 
Retype new password: 
passwd: password updated successfully

passwd command changes /etc/passwd where users data is stored. Example of a record in /et/passwd alex:x:1000:1000:alex,,,:/home/alex:/bin/bash


root@alex-Vostro-3558:/home/alex/Learning# w
 16:54:31 up  4:48,  3 users,  load average: 0,12, 0,36, 0,45
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
alex     :0       :0               12:06   ?xdm?  17:01   0.01s /usr/lib/gdm3/gdm-x-session --run-script env GNOME_SHELL_SESSION_MODE=ubuntu /usr/bin
alex     pts/1    a                15:24    1:29m  0.02s  0.02s /bin/bash
alex     pts/2    a                15:24    1.00s  0.25s 13.63s /usr/bin/python3 /usr/bin/guake


alex@alex-Vostro-3558:~/Learning$ chfn
Password: 
Changing the user information for alex
Enter the new value, or press ENTER for the default
	Full Name: alex
	Room Number [31]: 25
	Work Phone [666-666-66]: 
	Home Phone [999-999-99]:

alex@alex-Vostro-3558:~/Learning$ sudo passwd -e test_user
passwd: password expiry information changed.
alex@alex-Vostro-3558:~/Learning$ su test_user
Password: 
You are required to change your password immediately (administrator enforced)
Changing password for test_user.
Current password: 

Passwd -e allows to emmediately expire users password and he will be asked to change it on the next login.


alex@alex-Vostro-3558:~/Learning$ sudo passwd -l test_user
passwd: password expiry information changed.
alex@alex-Vostro-3558:~/Learning$ su test_user
Password: 
su: Authentication failure
alex@alex-Vostro-3558:~/Learning$ sudo passwd test_user
New password: 
Retype new password: 
passwd: password updated successfully
alex@alex-Vostro-3558:~/Learning$ su test_user
Password: 
test_user@alex-Vostro-3558:/home/alex/Learning$

passwd -l Allows locking the user's account by disabling the password. This doesn't disable the user since he can log in using other methods such as ssh key.


alex@alex-Vostro-3558:~/Learning$ more -d ~/.bash*
::::::::::::::
/home/alex/.bash_history
::::::::::::::
snap install spotify
snap install chromium
...


alex@alex-Vostro-3558:~/Learning$ less ~/.bash*

more and less are similar commands with less having more features. less also does not need to read the entire file before starting.

alex@alex-Vostro-3558:~/Learning$ vim ~/.plan
alex@alex-Vostro-3558:~/Learning$ finger alex
Login: alex           			Name: alex
Directory: /home/alex               	Shell: /bin/bash
Office: 25, 666-666-66			Home Phone: 999-999-99
On since Wed Aug  4 12:06 (EEST) on :0 from :0 (messages off)
On since Wed Aug  4 15:24 (EEST) on pts/1 from a
   2 hours 28 minutes idle
On since Wed Aug  4 15:24 (EEST) on pts/2 from a
   7 seconds idle
No mail.
Plan:
.working on labaratory work!


alex@alex-Vostro-3558:~/Learning$ ls -la ~/
total 356
drwxr-xr-x 27 alex alex   4096 сер  4 17:53 .
drwxr-xr-x  4 root root   4096 сер  4 17:07 ..
-rw-------  1 alex alex  11008 лип 23 16:13 .bash_history
-rw-r--r--  1 alex alex    220 лют 21 13:17 .bash_logout
-rw-r--r--  1 alex alex   3771 лют 21 13:17 .bashrc
-rw-r--r--  1 root root    178 кві 18 12:27 besside.log
drwx------ 25 alex alex   4096 лип 10 21:22 .cache
drwx------ 26 alex alex   4096 лип 10 21:29 .config
...

Task1.Part2

alex@alex-Vostro-3558:~/Learning$ tree -L 2 ~/
/home/alex/
├── besside.log
├── Desktop
│   ├── 2021-05-07-raspios-buster-armhf-lite.img
│   ├── P1533688.JPG
│   ├── photo_2020-10-22_15-11-09.jpg
│   └── Photos
...

alex@alex-Vostro-3558:~/Learning$ tree -L 2 ~/*c*
/home/alex/Documents
/home/alex/Jackett
├── AngleSharp.dll
├── Autofac.dll
├── Autofac.Extensions.DependencyInjection.dll
├── AutoMapper.dll
├── BencodeNET.dll
├── CommandLine.dll

alex@alex-Vostro-3558:~/Learning$ file README.md 
README.md: ASCII text

alex@alex-Vostro-3558:~/Learning$ cd ~
alex@alex-Vostro-3558:~$ 

alex@alex-Vostro-3558:~$ ls -d */
Desktop/  Documents/  Downloads/  Jackett/  Learning/ 

alex@alex-Vostro-3558:~$ ls -la
total 356
drwxr-xr-x 27 alex alex   4096 сер  4 17:53 .
drwxr-xr-x  4 root root   4096 сер  4 17:07 ..
-rw-------  1 alex alex  11008 лип 23 16:13 .bash_history
-rw-r--r--  1 alex alex    220 лют 21 13:17 .bash_logout
-rw-r--r--  1 alex alex   3771 лют 21 13:17 .bashrc
...

ls -l displays files and directories in a more readable format with
some additional information about permissions, creation date, and so
on. ls -a display hidden files sch as .ssh directory etc.

alex@alex-Vostro-3558:~$ mkdir testDir
alex@alex-Vostro-3558:~$ touch testDir/testFile
alex@alex-Vostro-3558:~$ ls -la /r
root/ run/  
alex@alex-Vostro-3558:~$ ls -la /root/ > testDir/testFile 
ls: cannot open directory '/root/': Permission denied
alex@alex-Vostro-3558:~$ sudo ls -la /root/ > testDir/testFile 
alex@alex-Vostro-3558:~$ vim testDir/testFile 
alex@alex-Vostro-3558:~$ cp testDir/testFile /home/alex/
alex@alex-Vostro-3558:~$ ls -l test*
-rw-rw-r-- 1 alex alex  602 сер  4 18:18 testFile

testDir:
total 4
-rw-rw-r-- 1 alex alex 602 сер  4 18:17 testFile
alex@alex-Vostro-3558:~$ rm -dr test
testDir/  testFile  
alex@alex-Vostro-3558:~$ rm -dr testDir/
alex@alex-Vostro-3558:~$ rm testFile

mkdir test
cp .bash_history test/labwork2
ln -s /home/alex/test/labwork2  /home/alex/test/labwork2_soft_link
ls -l test/
ln /home/alex/test/labwork2  /home/alex/test/labwork2_hard_link
vim test/labwork2_soft_link 
mv test/labwork2_hard_link hard_lnk_labwork2
mv test/labwork2_soft_link symb_lnk_labwork2
rm test/labwork2 

after the original file is deleted symb link would work but the hard
link still can be used to edit file data. You can say that the hard
link became the file when the original one was deleted.



alex@alex-Vostro-3558:~$ man locate 
alex@alex-Vostro-3558:~$ locate *squid*
/usr/share/vim/vim81/syntax/squid.vim
alex@alex-Vostro-3558:~$ locate *traceroute*
/etc/alternatives/traceroute6
/etc/alternatives/traceroute6.8.gz
/usr/bin/traceroute6
/usr/bin/traceroute6.iputils
/usr/lib/modules/5.8.0-53-generic/kernel/drivers/tty/n_tracerouter.ko
/usr/lib/modules/5.8.0-59-generic/kernel/drivers/tty/n_tracerouter.ko
/usr/share/man/man8/traceroute6.8.gz
/usr/share/man/man8/traceroute6.iputils.8.gz
/usr/share/nmap/scripts/http-traceroute.nse
/usr/share/nmap/scripts/targets-traceroute.nse
/usr/share/nmap/scripts/traceroute-geolocation.nse
/usr/src/linux-hwe-5.8-headers-5.8.0-53/tools/testing/selftests/net/traceroute.sh
/usr/src/linux-hwe-5.8-headers-5.8.0-59/tools/testing/selftests/net/traceroute.sh
/var/lib/dpkg/alternatives/traceroute6

alex@alex-Vostro-3558:~$ mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
udev on /dev type devtmpfs (rw,nosuid,noexec,relatime,size=4000184k,nr_inodes=1000046,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=000)


alex@alex-Vostro-3558:~$ mount > mounted_devices
alex@alex-Vostro-3558:~$ grep 'cg' mounted_devices | wc -l 
14

alex@alex-Vostro-3558:~$ find /etc/*host*
/etc/ghostscript
/etc/ghostscript/cidfmap.d
/etc/ghostscript/cidfmap.d/90gs-cjk-resource-korea1.conf
/etc/ghostscript/cidfmap.d/90gs-cjk-resource-cns1.conf
/etc/ghostscript/cidfmap.d/90gs-cjk-resource-gb1.conf
...

alex@alex-Vostro-3558:~$ find /etc/*ss*
...
alex@alex-Vostro-3558:~$ ls /etc/ | grep ss
gss
insserv.conf.d
issue


alex@alex-Vostro-3558:~$ ls -l /dev/
total 0
crw-r--r--  1 root root     10, 235 сер  4 12:06 autofs
crw-------  1 root root     10, 234 сер  4 12:06 btrfs-control

There are two types of devices, block devices, and character devices. ls -l outputs types of the device(first character in the line b or c) as well as  major number and minor number which tells what driver is responsible for this device and minor number allows the driver to run multiple devices. In this example, autofs is a character devies with major number 10 and minor 235.

alex@alex-Vostro-3558:~$ file testFile 
testFile: ASCII text
alex@alex-Vostro-3558:~$ ls -l testFile 
-rw-rw-r-- 1 alex alex 3 сер  4 20:50 testFile

File types:
	- : regular file
	d : directory
	c : character device file
	b : block device file
	s : local socket file
	p : named pipe
	l : symbolic link
	
alex@alex-Vostro-3558:~$ sudo find /etc/ -type f -amin $recently

Task.Linux.2

1. etc/passswd file contains users information structured in such form alex:x:1000:1000:alex,25,666-666-66,999-999-99:/home/alex:/bin/bash. its consists of users name, password, user id and group id. as well as additional information and path to the home directory. etc/group structured in a similar way and stores group name, password, GID, Group List.

2. UDI is used to identify users. it's stored in the third value of the line in /etc/passwd. Users with user id between 1 and 999 can be called system users since they used to run different services etc. From 1000 to 65533  can be considered normal users. There are also two special user root(UID 0) and nobody(UID 65534). root with full access to the system and nobody with no permissions to the system at all. 

3. GID is group identifyier. GID ranges similar to the UID ranges.

4. alex@alex-Vostro-3558:~/Learning$ groups alex
alex : alex adm cdrom sudo dip plugdev lpadmin lxd sambashare

5. alex@alex-Vostro-3558:~$ sudo adduser test_user
Adding user `test_user' ...
Adding new group `test_user' (1001) ...
Adding new user `test_user' (1001) with group `test_user' ...
Creating home directory `/home/test_user' ...
Copying files from `/etc/skel' ...
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for test_user
Enter the new value, or press ENTER for the default
	Full Name []: 
	Room Number []: 
	Work Phone []: 
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] y

Basic parameters are username and password everything else is optional.

6. alex@alex-Vostro-3558:~$ sudo usermod -l test_user test_user_changed

7. /etc/skell is a director that is used as a skeleton when creating user's home directory.

8. alex@alex-Vostro-3558:~$ sudo userdel -r test_user
userdel: test_user mail spool (/var/mail/test_user) not found

9. alex@alex-Vostro-3558:~$ sudo passwd -l test_user
passwd: password expiry information changed.
alex@alex-Vostro-3558:~$ sudo passwd -u test_user
passwd: password expiry information changed.

11. alex@alex-Vostro-3558:~$ ls -l /home/alex/
total 276
-rw-r--r--  1 root root    178 Apr 18 12:27 besside.log
drwxr-xr-x  3 alex alex   4096 Jul 27 13:02 Desktop
drwxr-xr-x  2 alex alex   4096 Feb 21 13:37 Documents
...

12. Access rights to a file or a directory set by the owner, group, and everyone. Rights include read, write and execute operations(r, w, x).

13. When a file is created its owner is set as the user who created it and group this user's primary group. 

14. alex@alex-Vostro-3558:~$ touch testFile 
alex@alex-Vostro-3558:~$ ls -l testFile 
-rw-rw-r-- 1 alex alex 3 Aug  4 22:41 testFile
alex@alex-Vostro-3558:~$ chown test_user testFile 
chown: changing ownership of 'testFile': Operation not permitted
alex@alex-Vostro-3558:~$ sudo chown test_user testFile 
[sudo] password for alex: 
alex@alex-Vostro-3558:~$ ls -l testFile 
-rw-rw-r-- 1 test_user alex 3 Aug  4 22:41 testFile
alex@alex-Vostro-3558:~$ sudo chmod -c 777 testFile 
mode of 'testFile' changed from 0664 (rw-rw-r--) to 0777 (rwxrwxrwx)

15. Access right of reading(4) writing(2) and executing(1)
represented with a single-digit. For example file with a 666 access
octal is allowed to be read and written by its owner group and
everyone else. Default access right octal is 666 but it can be
changed by umask command.

16. Sticky bit can be set with chmod -t FileName and will prevent from altering ...

17. Execution needs to be allowed for a script to run.  


Task.Linux.3
Part1

1. Process can be in 5 differend states:
	Running (R)
	Sleeaping (S)
	Uninterruptable sleep (D)
	Stopped (S)
	Zombie (Z)
	
2. -h option is used to highlight  the  current  process and its ancestors. 
![](https://i.imgur.com/QDlntqw.png)

3. Proc file is a virtual file system that's created on a start-up and removed on shutdown. It contains information about the processes that are currently running. It is used as a control center for the kernel. 

4. ps -Flww -p PID
![](https://i.imgur.com/OwrBgzh.png)

5. ![](https://i.imgur.com/ZqNPkoj.png)

6. Kernel processes are part of the Linux kernel and cannot be managed or killed by the user. User processes are ones initiated by the user. 

7. ![](https://i.imgur.com/HprEWgB.png) 
Processes can be in 5 different states. For example, r (running) means that task is currently being executed, d (uninterruptable sleep) most of the time process waiting for IO, z (zombie) means that the process stopped responding and could be closed by its parent process.

8. ![](https://i.imgur.com/ISW0YcT.png)

9. Some of the commands mentioned in ps man page: pgrep, pstree, top, proc.

10. top displays information about most active processes (PID, process priority, state etc) and provides utilities for managing processes. 

11. ![](https://i.imgur.com/Df3QkAG.png)

12. Sort by most memory usage - Shift M or by CPU usage Shift P
	Change the priority of the process or kill sending different signals to it K. 
	
13. ![](https://i.imgur.com/tPWna7r.png)

14. nice and renice. Nice used when the process is started and renice to change the process priority. 

15. Using Shift P command.

16. kill send different signals to the process like SIGTERM(15) or SIKILL(9) and process will respond accordingly to them.

17. Commands can be executed in the background of the shell. A job is a process that the shell manages. jobs command used to list all of the jobs.
For example 
![](https://i.imgur.com/twy4Bi1.png)

 
Part2

1. On windows ssh command and ssh-keygen behave the same way as on Linux system. With ssh user@host we can connect to the machine remotely and by ssh-keygen generate a public and private key for authentication. 

![](https://i.imgur.com/hwHhvBt.jpg)

2. Disable root login, disable password-based login, and restrict ssh access using iptables.
![](https://i.imgur.com/tABK7bf.png)
![](https://i.imgur.com/VOwiyjk.png)

3. By using ssh-keygen -t we can specify the key type and choose from the following RSA
ECDSA, ed25519. If no value is specified RSA key will be generated.

![](https://i.imgur.com/ry0DEyM.png)










