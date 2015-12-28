PyDbg - Capstone
================

This is a fork of Pedram Amini's [PyDbg](http://pedramamini.com/PaiMei/docs/) ([archived copy at OpenRCE](https://github.com/OpenRCE/pydbg)) that replaces libdasm/pydasm with the more up-to-date and maintained Capstone Engine. There are many projects still relying on this library but I got tired of setting up pydasm, this is the result. 

In the current state this branch probably works for those software that I personally use, but there certainly are some incompatibilities. If you find any, please use the Issue Tracker!

If you need a good introduction to PyDbg you should check out the book [Gray Hat Python](https://www.nostarch.com/ghpython.htm)!

Installation
------------

There is a small setup script provided, `setup.py install` should just work _as long as the repo is cloned to a directory called pydbg!_

The installer script of PaiMei checks requirement by trying to import the corresponding modules, so you should be good to go with that if you install pydbg first.

License
-------

The PyDbg project is licensed under GNU/GPL.

