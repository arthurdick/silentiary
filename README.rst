Warning
======================================================================

This is alpha software, and comes with no guarantees. Future development
may break existing database stores until a stable release is made.

This software uses gpg for all encryption. The security of passwords
stored with silentiary therefore depends on the security of your gpg key.

Requirements
======================================================================

Core commands require python3 and gpg2 are installed.

The type command requires xte linux program to be installed.
The copy command requires xsel linux program to be installed.

Installing
======================================================================

Install with pip::

    pip3 install silentiary

Usage
======================================================================

Commands available::

    silentiary initialize
    silentiary list [<location>] [-r]
    silentiary write [<location>] [<attribute>] [<value>] [-d] [-m]
    silentiary generate [<location>] [<attribute>] [-c CHARSET]... [-l LENGTH]
    silentiary copy [<location>] [<attribute>]
    silentiary type [<location>] [<attribute>]
    silentiary open [<location>] [<attribute>]
    silentiary read [<location>] [<attribute>]
    silentiary delete [<location>] [-r]
