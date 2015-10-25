# Schocken
Schocken Würfelspiel Simulation


# Packages
sudo apt-get install python-pip
sudo pip install --upgrade pip
sudo pip install peewee

sudo apt-get install python-dev
sudo apt-get install postgresql-contrib
sudo apt-get install postgresql-server-dev-all

su postgres
psql template1 -c 'create extension hstore;'
psql schock_db -c 'create extension hstore;'