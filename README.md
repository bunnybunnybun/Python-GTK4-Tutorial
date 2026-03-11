# Python GTK4 Tutorial
The purpose of this guide is to be a beginner friendly introduction to making desktop apps using Python and GTK4 by teaching you how to make a basic weather app. The full code of the final app is available in this repository in the main.py file.

## Step one: creating the project
First, make a folder for your project anywhere on your computer. Name it something that makes it clear what it's for. Inside the folder, create a file called main.py, this will be the main file of our app. The name of the file doesn't actually matter, but that's what I'll use in this tutorial. Open up the file in a text editor, and write this:
```
import gi
import requests
import json
from threading import Thread

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk
```
This will simply try to import all of the libraries we will need throughout the project. Try running it by navigating in the terminal into the folder you created and running ````python3 main.py````. You will most likely get errors because you don't actually have the libraries that you are trying to import installed on your system. If that's the case, then go to step two to install the libraries, then come back and run it again to see if it works.

However, if it runs without giving you any errors, then that means you already have all the required libraries installed and can skip step two! That being said, you might want to update them anyways, but that's not required.

## Step two: installing the required libraries
First of all, you will need python3. This is likely preinsalled on your system, but [here's the most comprehensive guide I could find on how to install it](https://realpython.com/installing-python/) in case it's not preinstalled.

You will of course need GTK itself, but also PyGObject, which allows you to *use* GTK in your python application. You can install these using either your operating system's package manager or PyPI, Python's package manager. I recommend using your OS's package manager if you can, but PyPI works fine too. Instructions can be found on [the PyGObject website](https://pygobject.gnome.org/getting_started.html).

Finaly, the last needed library is [Requests](https://requests.readthedocs.io/en/latest/). This will allow us to very easily call the Open-Meteo API to get the weather forecast. You can install it from PyPI by running the command ````python -m pip install requests```` in the terminal, or, if you are on Linux, I recommend using your package manager instead. To install it with your package manager, if you are on Debian or a derivative such as Ubuntu or Linux Mint, use this command ````sudo apt install python3-requests````, or if you are on Arch Linux or a derivative, use ````sudo pacman -Sy python-requests````, and on Fedora or a derivative, do ````sudo dnf install python3-requests````.

Now run the program we created earlier to make sure that the libraries are installed correctly.