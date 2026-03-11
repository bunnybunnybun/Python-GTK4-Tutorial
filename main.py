import gi
import requests
import json
from threading import Thread

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk