Title: Emacs
Date: 2009-12-26 00:20
Author: Alexenko
Category: Software
Tags: editor, emacs, Software

So I decided to start learning [Emacs][]. Not sure it's a worthwhile
endeavor yet, but I'm hopeful at some point the time invested into
learning Emacs will save enough editing time to make learning all these
commands worthwhile. So far I haven't learned anything that isn't
available in [vi][].  

Considering there're so many Emacs gurus out there, I was really
surprised that there are so few current tutorials on the web (I got
tired after 3 pages of google results). Maybe Emacs hasn't changed
enough in the past few years to bother updating the tutorials. I started
with the [newbie guide][] from the [Emacs wiki][], but all it does is
throw all of the commands at you. After about 30 minutes of trying to
remember the commands I closed it. It turns out that Emacs comes with an
excellent tutorial (`C-h t`) that introduces the commands slowly enough
and encourages practice; finger memory takes a long time to attain, so
starting to practice right away is A++.  

I have to give it up to the Emacs community though on putting together
excellent tutorials on the Emacs wiki on how to acquire it. So many
options are available and they're all thoroughly explained. I chose to
pull the latest release from CVS and compile it on my Mac (10.5.8). For
me it was one of the most uneventful compiles ever. The wiki recommended
looking at the nightly build script. To build Emacs.app I just
copy-pasted the following into Terminal.app. Everything worked as
expected  

CFLAGS="-pipe -march=nocona" \\  

./configure --build i686-apple-darwin10.0.0 --without-dbus --with-ns  

make bootstrap -j3 && make install  
</code>  

Then just drag the Emacs.app from `./nextstep/` to `/Applications`. Set
your aliases or make symbolic links as desired.

</p>

  [Emacs]: http://www.gnu.org/software/emacs/
  [vi]: http://www.vim.org/
  [newbie guide]: http://www.gnu.org/software/emacs/tour/
  [Emacs wiki]: http://www.emacswiki.org/
