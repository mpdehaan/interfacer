#
# Copyright (c) rPath, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


# Michael DeHaan

import interfacer.base_module as base_module
import sys


def register():
    return TribblesModule()


class ListCommand(base_module.SubCommand):
    ''' example_cli tribbles list [--name] '''

    def name(self):
        return 'list'

    def description(self):
        return 'list the tribbles'

    def options(self):

        return [
           ["-n", "--name",
            dict(dest="name", help="list tribles only with this name")]
        ]

    def run(self, options, args):
        tribbles = ['xyork', 'slorg', 'rooster', 'blinky', 'poorboy', 'willy']

        found = False
        for x in tribbles:
            if options.name is not None:
                if options.name.lower() in x:
                    found = True
                    print x
            else:
                print x

        if not found and options.name is not None:
            # TODO: make this an exception subclass
            sys.stderr.write("error: tribble (%s) not found" % options['name'])
            return 1
        return 0


class TribblesModule(base_module.BaseModule):
    ''' example_cli tribbles [...] '''

    def name(self):
        return 'tribbles'

    def description(self):
        return 'does things with tribbles'

    def sub_commands(self):
        return [
            ListCommand(self)
        ]
