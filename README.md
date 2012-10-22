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

Examples
========

    # example_cli

    usage: ./example_bin/example_cli <category> [subcommand] [--options]

      choose a category for information about available commands:
                tribbles - does things with tribbles

    # example_cli tribbles

    usage: ./example_bin/example_cli tribbles <subcommand> [--options]

      choose a subcommand:

                    list - list the tribbles

    # example_cli tribbles list --help

    Usage: example_cli tribbles list [options]

    Options:
          -h, --help            show this help message and exit
          -n NAME, --name=NAME  list tribles only with this name

    # example_cli tribbles list 

    xyork
    slorg
    rooster
    blinky
    poorboy
    willy

    # example_cli tribbles list --name=willy

    willy



License
=======

Interfacer is MIT licensed (c) rPath 2012 and is very open to contributions, but not
so much feature requests or bug reports (due to time constraints).  Since
it's so simple, just send me a pull request if you'd like to add or fix
something.

Author
======

Michael DeHaan -- michael DOT dehaan AT gmail.com
