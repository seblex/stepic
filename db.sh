#sudo /etc/init.d/mysql restart
sudo service mysql restart
sudo mysql -uroot -e "CREATE DATABASE qa CHARACTER SET utf8 COLLATE utf8_general_ci;"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON qa.* TO 'stepic'@'%' IDENTIFIED BY 'stepic';"