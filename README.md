## This guide is still a work in progress!

# Python GTK4 Tutorial

The purpose of this guide is to be a beginner friendly introduction to making desktop apps with Python using GTK4. This guide only expects you to have a *very* basic understanding of programming in Python. If you don't understand everything, that's fine! Coding can feel very overwhelming at first, it's normal.

## Step one: creating the project

First, make a folder for your project anywhere on your computer. Name it something that makes it clear what it's for. Inside the folder, create a file called main.py, this will be the main file of our app. The name of the file doesn't actually matter, but that's what I'll use in this tutorial. Open up the file in a text editor, and write this:

```
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk
```

This will simply try to import all of the libraries we will need throughout the project. Try running it by navigating in the terminal into the folder you created and running ````python3 main.py````. You will most likely get errors because you don't actually have the libraries that you are trying to import installed on your system. If that's the case, then go to step two to install the libraries, then come back and run it again to see if it works.

However, if it runs without giving you any errors, then that means you already have all the required libraries installed and can skip step two! That said, you might want to update them anyways, but that's not required.

## Step two: installing the required libraries

First of all, you will need python3. This is likely preinsalled on your system, but [here's](https://realpython.com/installing-python/) the most comprehensive guide I could find on how to install it in case it's not preinstalled.

You will of course need GTK itself, but also PyGObject, which allows you to *use* GTK in your python application. You can install these through PyPI, Python's package manager. If you are on Linux, you also have the option of installing them through your operating system's package manager instead, which I recommend. Instructions for both methods can be found on [the PyGObject website](https://pygobject.gnome.org/getting_started.html).

Now run the program we created earlier to make sure that the libraries are installed correctly. If it doesn't output any errors, proceed to step 3!

## Step 3: Make a blank application window

Ok, let's start by making a blank window. Add this to the main.py file after all of the imports:

```
class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.ExampleWeatherApp")
        GLib.set_application_name('ExampleApp')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="My First App") # The title is what name will be shown for the application in the title bar of the window. Change this to whatever you want!
        window.present()

app = MyApplication()
app.run() # You should generally make sure this line always remains at the end of your file.
```

It's okay if you don't understand everything that we just wrote! Try saving and running the program, you should see a blank window appear.

## Step 4: Add some widgets!

GTK apps are made by combining widgets. There are lots of types of widgets, such as buttons, text boxes, or containers. Containers are used for specifying where other widgets go, by placing said widgets inside a container widget. Some types of containers are grids, panes, etc. You can see a list of all possible widgets [here](https://docs.gtk.org/gtk4/visual_index.html).

The first widget you add [should always be a container widget](## "Why? You can only put one widget directly in a window. So, that one widget must be a container widget, so that you can put more widgets inside of it."), so you can put more widgets inside it. I usually start with the Box widget.

To create your box widget, right before the ```window.present()``` line in your code, add this line: ```self.main_box = Gtk.Box()```. What did we just do? We created a variable called self.main_box, and set it to equal a box widget.
Now, we've created a box, but we have to actually add it to the window. To do that, add this line right after the one we just added: ```window.set_child(self.main_box)```.

Now run the program. You should see... That the window is still blank. Remember that the Box widget is just a container, all it does is help us specify where other widgets go. So... Add some more widgets inside it! How about a button? We can create it exactly like we did with the box. Just do ```self.button = Gtk.Button()``` instead of ```self.main_box = Gtk.Box()```.
Then, to add it to the box, do ```self.main_box.append(self.button)```.

Your full code should now look something like this:

```
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk, Gdk

class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.ExampleWeatherApp")
        GLib.set_application_name('ExampleApp')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="My First App")
        self.main_box = Gtk.Box()
        self.button = Gtk.Button()
        self.main_box.append(self.button)
        window.set_child(self.main_box)
        window.present()

app = MyApplication()
app.run()
```

Run the program, you should now see a button on the left side of the window! We'll customize the button soon, but first let's add a text element, called a Label. Add it just like you added the button, but replace ```Gtk.Button()``` with ```Gtk.Label(label="Put whatever text you want here")```, and give it a different name.

If you add the label below the line where you added the button, it will appear *after* the button. If you put it above the line where you added the button, it will appear *before* the button.

Currently, widgets in the Box container are being placed horizontally. We can change the Box to be vertical by changing this line: ```self.main_box = Gtk.Box()``` to this: ```self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)```. Try it and see what happens!

## Step 5: Customize!

We've added widgets, but now I'll show you how to customize them.