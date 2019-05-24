vim-pandemic
============

Manage remote [pathogen] bundles from multiple source types.

I've been looking for a way to maintain a `~/.vim{,rc}` repository.  The natural
solution is to just have a Git repo containing my `~/.vimrc` and contents of
`~/.vim`.  Sure, that's no problem.

Since I use [pathogen], I have a variety of bundles that are repositories of
various types: Git, Mercurial, etc.  I strongly believe in the philosophy that
version control should not be tied into the operation of the thing it is
tracking.  For that reason, using Git submodules as part of my vim
configuration repository just seems stupid.  This was not the problem that
submodules tries to solve and it leads to a lot of problems and configuration
difficulties.  My adherence to this philosophy also means that I don't want to
use systems like [Vundle], though I appreciate the author's work in developing
this sort of workflow.

So I decided to build a way to easily manage remote repositories outside of
vim, without requiring the use of a specific repository.  The result is
[vim-pandemic].

## Installation

Clone this repo, and then run:

```
sudo python setup.py install
```

This places the [pandemic] executable onto your path (probably at
`/usr/local/bin/pandemic`), and installs its dependencies to your
`site-packages` folder.

## Getting Started

By default, [pandemic] manages bundles in `~/.vim/bundle.remote`.  So, in your `~/.vimrc`,
you're going to want:

```vim
execute pathogen#infect('bundle.remote/{}')
```

In addition to having calls to `pathogen#infect()` for your local bundles.


## Managing Bundles

Using [pandemic] is easy!  Like, really, it actually is easy.


### Adding a bundle

Using the `add BUNDLE TYPE SOURCE` command, we can easily add new bundles.
`BUNDLE` can be any name you want to give the bundle you're storing, `TYPE` is
one of the source types (run `pandemic --types` to find out supported types),
and `SOURCE` is the remote source.  For example:

```
$ pandemic add nerdtree git https://github.com/scrooloose/nerdtree.git
```

will add NERD Tree to our bundle list.  It's being developed in a Git repo on Github.

What if we wanted something from Mercurial because the developer is some kind of hipster?  Easy:

```
$ pandemic add l9 hg https://bitbucket.org/ns9tks/vim-l9
```

[pandemic] also supports things that aren't version-controlled.  For example,
you might have a directory that you simply want to copy over to your bundle
directory.  For that, you can just use the `local` type.  Or, you might have a
directory that contains its own update script called `.update`; for that, you
can use the type `script`.

Adding new types is as easy as modifying `bundle.py` to have more
`BundleActioners`.


### Removing a bundle

Simply:

```
$ pandemic remove nerdtree
```

If you stick `keep` at the end, it will not delete the data from the bundle
directory.  I highly don't recommend that.


### Updating a bundle

To update all bundles, just run:

```
$ pandemic update
```

Or, to update specific ones:

```
$ pandemic update nerdtree tagbar
```


### Listing Bundles

Try:

```
$ pandemic list | column -t
```


### Synchronization

Let's say you removed some entries from [pandemic]'s database file but left the
physical bundle files in the bundle directory.  You can use:

```
$ pandemic list-dead
```

to find which bundles are still in the directory but not in the database file
and vice-versa.  You can then run `pandemic update` to get missing bundles or
delete extra bundles yourself.


## But what about disabled bundles?

[pathogen] allows you to append `~` at the end of a bundle name to disable it
from being used at runtime.  [pandemic] does a decent job of detecting this
when you are trying to perform operations.  Simply keep using the original name
in your tasks.  For example, let's say you installed NERD Tree, but then you
disabled it and now you want to remove it.  That's okay!

```
$ pandemic add nerdtree git https://github.com/scrooloose/nerdtree.git
$ mv ~/.bundle.remote/nerdtree ~/.bundle.remote/nerdtree~
$ pandemic remove nerdtree
```

[pandemic] knows what to do.  Please, just don't try to simultaneously have
`~/.vim/bundle.remote/nerdtree` and `~/.vim/bundle.remote/nerdtree~` exist at
the same time.  [pandemic] doesn't detect every form of idiocy.


## What's up for the future?

I'm deciding whether I want to allow the user to enable or disable bundles from
[pandemic].  Part of me thinks that this is a bad idea and is missing the point
of the program.


## This is dumb.

Yeah, probably.  But it's suitable for my workflow, which is what I care about.
When I was trying to think up names for this program, I accidentally ran across
[vim-epidemic], which does just about the same thing, only in Ruby, and also
only with Git repositories.



[pathogen]:https://github.com/tpope/vim-pathogen
[vim-pandemic]:http://github.com/jalanb/vim-pandemic
