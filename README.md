Interfacer
==========

Interfacer is a multi-level command line support library, heavily inspired
by Cobbler's command line structure, only a lot cleaner.

To use it, just write an example script like the one in 'example_bin'
and some modules like the ones in 'example_modules'.

Interfacer is also a thin abstraction around optparse at the lowest
level, which simplifies how easy it is to write new command line
tools.

Explore the source in 'lib' to understand how it works.

List Categories
===============

example_cli

See What Commands Are In A Category
===================================

example_cli category   

Run A Command
=============

example_cli category subcommand [--help]

License
=======

Interfacer is MIT licensed and is very open to contributions, but not
so much feature requests or bug reports (due to time constraints).  Since
it's so simple, just send me a pull request if you'd like to add or fix
something.

Author
======

Michael DeHaan -- michael DOT dehaan AT gmail.com
