Tornado webapp skeleton
=======================

This is a webapp skeleton based on the [Tornado](https://github.com/facebook/tornado) web server and [html5boilerplate](http://html5boilerplate.com/) framework.

General goal of this package is to provide web application skeleton which can be modified to simplify starting new dvelopment.

At the moment this skeleton provides:

- logging with log rotation (from tornado)
- production/development mode logging
- sample homepage

Dependecies
-----------

- Tornado 2.0+

Tested with the Python 2.6.5 & 2.7.1

Usage
-----

Download and unpack current stable version:

    wget -O skeleton.tar.gz https://github.com/sitnin/skeleton/tarball/master
    tar zxf skeleton.tar.gz

Create and modify webapp.conf:

    cp etc/sample-webapp.conf etc/webapp.conf
    nano etc/webapp.conf

Run web application daemon:

    python webapp.py etc/webapp.conf

Your skeleton is a working webapp now! =)

License
-------

Skeleton is free software package: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Skeleton is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

To receive a copy of the GNU General Public License
see [GNU GPL](http://www.gnu.org/licenses/) website.

Contact info
------------

- Twitter: [sitnin](http://twitter.com/sitnin)
- Email: [sitnin@gmail.com](mailto:sitnin@gmail.com)
