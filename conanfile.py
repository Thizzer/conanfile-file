#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
from six import StringIO

import os
import traceback

class LibmagicConan(ConanFile):
    name = "libmagic"
    version = "5.40"
    url = "https://www.darwinsys.com/file/"
    description = "The file command is \"a file type guesser\", that is, a command-line tool that tells you in words what kind of data a file contains."
    license = "https://github.com/file/file/blob/master/COPYING"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = 'make'
    requires = "bzip2/1.0.8", "zlib/1.2.11"
    source_url = "https://github.com/file/file"
    source_subfolder = "file"
        
    def source(self):
        self.run("git clone " + self.source_url)

        with tools.chdir(self.source_subfolder):
            version_tag = "FILE{0}".format(self.version.replace('.', '_'))
            tag_info = StringIO()
            self.run("git tag -l {0}".format(version_tag), output=tag_info)
            if len(tag_info.getvalue().strip()) != 0:
                self.run("git checkout " + version_tag)
            else:
                self.run("git checkout master")


    def build(self):
        with tools.chdir(self.source_subfolder):
            self.run("autoreconf -f -i")
            if self.options.shared:
                self.run("./configure --prefix=%s"% self.package_folder)
            else:
                self.run("./configure --enable-static --disable-shared --prefix=%s"% self.package_folder)
            self.run("make")
            self.run("make install")

    def package(self):
        self.copy(pattern="COPYING", src=self.source_subfolder)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.resdirs.append("share")
