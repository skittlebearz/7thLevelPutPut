#! /bin/sh
#
# Part of this script is stolen from:
# Bert Van Vreckem <bert.vanvreckem@gmail.com>
# 
# This script automates the installation of dependencies,
# the setup of a mysql server,
# and setup of python virtual environment for the PutPut django app
# 
#
# Tested on Ubuntu 20.04 

set -o errexit # abort on nonzero exitstatus
set -o nounset # abort on unbound variable


#{{{ Functions

usage() {
cat << _EOF_

Usage: ${0} "ROOT PASSWORD"

  with "ROOT PASSWORD" the desired password for the database root user.

Use quotes if your password contains spaces or other special characters.
_EOF_
}


#}}}
#{{{ Command line parsing

if [ "$#" -ne "1" ]; then
  echo "Expected 1 argument, got $#" >&2
  usage
  exit 2
fi


#}}}
#{{{ Variables
db_root_password="${1}"
db_django_password=`openssl rand -base64 14`
#}}}

# Script proper

# Download and install dependencies
yes y | sudo apt install python3 python3-pip python3-dev python3.8-venv default-libmysqlclient-dev build-essential
wget -c https://repo.mysql.com//mysql-apt-config_0.8.19-1_all.deb
sudo DEBIAN_FRONTEND=noninteractive dpkg -i mysql-apt-config_0.8.19-1_all.deb
yes y | sudo DEBIAN_FRONTEND=noninteractive apt install mysql-server
rm mysql-apt-config_0.8.19-1_all.deb

#Setup MySQL server
sudo su - root -c "mysql" <<_EOF_
  SET PASSWORD FOR 'root'@'localhost' = '${db_root_password}';
  DELETE FROM mysql.user WHERE User='';
  DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');
  DROP DATABASE IF EXISTS test;
  DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
  FLUSH PRIVILEGES;
  CREATE DATABASE putput CHARACTER SET utf8;
  CREATE USER 'django'@'localhost' IDENTIFIED BY '${db_django_password}';
  GRANT ALL PRIVILEGES ON putput.* to django@localhost;
_EOF_

cat << EOF > PutPutProject/mysql.cnf
[client]
database = putput
user = django 
password = ${db_django_password}
default-character-set = utf8
EOF

#Setup python environment
python3 -m venv putputvenv
. putputvenv/bin/activate
pip3 install -r requirements.txt

