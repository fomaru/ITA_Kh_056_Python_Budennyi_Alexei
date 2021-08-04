Command line output and comments

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

