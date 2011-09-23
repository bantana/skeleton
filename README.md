Tornado webapp skeleton
=======================

This is a webapp skeleton based on the [Tornado](https://github.com/facebook/tornado) web server and [html5bolerplate](http://html5boilerplate.com/) framework.

General goal of this package is to provide web application skeleton which can be modified to satisfy concrete needs.

Functionality provided at the moment:

- production/development mode
- UID/GID switching in production mode
- logging with log rotation
- webapp status page
- simple homepage

Usage
-----

Just clone this repository:

    git clone https://github.com/sitnin/skeleton.git

Remove .git folder:

    cd skeleton
    rm -Rf .git

Create and modify webapp.conf:

    cp etc/sample-webapp.conf etc/webapp.conf
    nano etc/webapp.conf

Run web application daemon:

    python webapp.py etc/webapp.conf

Your skeleton is a working webapp now! =)

License
-------

I'm currently searching for the proper license. Please, come back later to get informed about license type.

For sure, it will be an existing free open-source license.

Contact info
------------

- Twitter: sitnin
- Email: [sitnin@gmail.com](mailto:sitnin@gmail.com)
