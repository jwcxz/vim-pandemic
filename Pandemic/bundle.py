import os
import shutil
import subprocess

from Pandemic import printer
from Pandemic import shell

class BundleActioner:
    def clone(self, source, name):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def remove(self, name):
        shutil.rmtree(name)


class BundleGit(BundleActioner):
    def clone(self, source, name):
        return shell.run(["git", "clone", source, name])

    def update(self):
        return shell.run(["git", "pull", "--rebase"])


class BundleHg(BundleActioner):
    def clone(self, source, name):
        return shell.run(["hg", "clone", source, name])

    def update(self):
        return shell.run(["hg", "pull"])


class BundleLocal(BundleActioner):
    def clone(self, source, name):
        outmsg = shell.run(["cp", "-R", source, name])
        with open(f"{name}/.source", "w") as stream:
            stream.write(source)
        return outmsg

    def update(self):
        with open(".source") as stream:
            source = stream.read()
        name = os.path.split(os.getcwd())[1]
        os.chdir(os.path.split(os.getcwd())[0])
        return self.clone(source, name)


class BundleScript(BundleActioner):
    def clone(self, source, name):
        return shell.run(["cp", "-R", source, name])

    def update(self):
        return shell.run(["./.update"])


actioners = {
    "git": BundleGit,
    "hg": BundleHg,
    "local": BundleLocal,
    "script": BundleScript,
}


class Bundle:
    def __init__(self, name, source, type_, path_to_bundles):

        self.name = name
        self.path_to_bundles = os.path.expanduser(path_to_bundles)
        self.source = source
        self.type = type_

        self.bname = self.__findbundle()
        self.actioner = actioners[type_]()

    def clone(self):
        # clone from whatever repository or whatever
        self.__savecwd()
        os.chdir(self.path_to_bundles)

        if self.bname:
            # path already exists
            # best action to take is probably to just remove and clone
            # XXX: this isn't safe, though :(
            printer.warn("%s exists!" % (self.bname))
            self.remove()

        msg = self.actioner.clone(self.source, self.name)
        printer.info(msg)

        self.__restorecwd()

    def remove(self):
        # delete an existing bundle directory
        self.__savecwd()
        os.chdir(self.path_to_bundles)

        if self.bname:
            msg = self.actioner.remove(self.bname)
            printer.info(msg)
        else:
            printer.warn("%s doesn't exist!" % (self.name))

        self.__restorecwd()

    def update(self):
        # update a repository
        self.__savecwd()
        os.chdir(self.path_to_bundles)

        if self.bname:
            os.chdir(self.bname)
            msg = self.actioner.update()
            printer.info(msg)
        else:
            printer.warn("%s doesn't exist!" % (self.name))
            self.clone()

        self.__restorecwd()

    def __findbundle(self):
        orig = os.path.join(self.path_to_bundles, self.name)
        disabled = os.path.join(self.path_to_bundles, "%s~" % self.name)

        if os.path.exists(orig):
            return self.name
        elif os.path.exists(disabled):
            printer.warn("Using disabled form of %s..." % self.name)
            return "%s~" % self.name
        else:
            return None

    def __savecwd(self):
        self.__lastcwd = os.getcwd()

    def __restorecwd(self):
        os.chdir(self.__lastcwd)
