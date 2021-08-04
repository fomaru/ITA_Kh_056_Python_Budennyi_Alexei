groups alex
sudo adduser test_user
sudo usermod -l test_user test_user_changed
sudo userdel -r test_user
sudo passwd -l test_user
sudo passwd -u test_user
ls -l /hoome/alex/
chown test_user testFile
chmod -c 777 testFile

