#holmes-api [![Build Status](https://secure.travis-ci.org/holmes-app/holmes-api.png?branch=master)](https://travis-ci.org/holmes-app/holmes-api)

API for holmes website validation.


## Waffle [![Stories in Ready](https://badge.waffle.io/holmes-app/holmes-api.png?label=ready)](https://waffle.io/holmes-app/holmes-api)

https://waffle.io/holmes-app/holmes-api


## Contributing


See [CONTRIBUTING.md](/CONTRIBUTING.md) if you want to contribute to holmes-api, the document also have installation instruction for development enviroments.


mkdir -p ~/vens/holmes
virtualenv ~/vens/holmes
source ~/vens/holmes/bin/activate
pip install -U pip
make setup

make drop data
http://stackoverflow.com/questions/10557507/rails-mysql-on-osx-library-not-loaded-libmysqlclient-18-dylib

.bash_profile
export MYSQL_HOME=/usr/local/mysql-5.6.24-osx10.8-x86_64
export PATH=$MYSQL_HOME/bin:$PATH
export DYLD_LIBRARY_PATH=$MYSQL_HOME/lib:$DYLD_LIBRARY_PATH

sudo ln -s $MYSQL_HOME/lib/libmysqlclient.18.dylib /usr/lib/libmysqlclient.18.dylib

brew install redis
pip uninstall setuptools
pip install 'setuptools<20.2'
make run