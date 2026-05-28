## This guide is still a work in progress!

This is the second guide in a series. If you haven't already gone through the first guide, do it now [here](regular_python_guide.html).

# Python GTK4 Tutorial

The purpose of this guide is to be a beginner friendly introduction to making desktop apps with Python using GTK4. GTK is a cross platform library that allows you to make apps! When talking about coding, libraries are basically add-ons to the programming language you are using; They give you access to more functionality!

This guide only expects you to have a *very* basic understanding of programming in Python. If you don't understand everything in this guide, that's fine! Coding can feel very overwhelming at first, it's normal.

## Step one: creating the project

First, make a folder for your project anywhere on your computer. Name it something that makes it clear what it's for. Inside the folder, create a file called main.py, this will be the main file of our app. The name of the file doesn't actually matter, but that's what I'll use in this tutorial. Open up the file in a text editor, and write this:

```python
import gi  

gi.require_version("Gtk", "4.0")  
from gi.repository import GLib, Gtk, Gdk
```

This will simply try to import all of the libraries we will need throughout the project. Try running it by navigating in the terminal into the folder you created and running `python3 main.py`. You will most likely get errors because you don't actually have the libraries that you are trying to import installed on your system. If that's the case, then go to step two to install the libraries, then come back and run it again to see if it works.

However, if it runs without giving you any errors, then that means you already have all the required libraries installed and can skip step two! That said, you might want to update them anyways, but that's not required.

## Step two: installing the required libraries

First of all, you will need python3. This is likely pre-insalled on your system, but [here's](https://realpython.com/installing-python/) the most comprehensive guide I could find on how to install it in case it's not pre-installed.

You will of course need GTK itself, but also PyGObject, which allows you to *use* GTK in your python application. You can install these through PyPI, Python's package manager. If you are on Linux, you also have the option of installing them through your operating system's package manager instead, which I recommend. Instructions for both methods can be found on [the PyGObject website](https://pygobject.gnome.org/getting_started.html).

Now run the program we created earlier to make sure that the libraries are installed correctly. If it doesn't output any errors, proceed to step 3!

## Step 3: Make a blank application window

Ok, let's start by making a blank window. Add this to the main.py file after all of the imports:

```python
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

The first widget you add should always be a container widgetⓘ, so you can put more widgets inside it. I usually start with the Box widget.

To create your box widget, right before the `window.present()` line in your code, add this line: `self.main_box = Gtk.Box()`. What did we just do? We created a variable named self.main_box, and set it to equal a box widget.  
Now, we've created a box, but we have to actually add it to the window. To do that, add this line right after the one we just added: `window.set_child(self.main_box)`.

Now run the program. You should see... That the window is still blank. Remember that the Box widget is just a container, all it does is help us specify where other widgets go. So... Add some more widgets inside it! How about a button? We can create it exactly like we did with the box. Just do `self.button = Gtk.Button()` instead of `self.main_box = Gtk.Box()`.  
Then, to add it to the box, do `self.main_box.append(self.button)`.

Your full code should now look something like this:

```python
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

Run the program, you should now see a button on the left side of the window! We'll customize the button soon, but first let's add a text element, called a Label. Add it just like you added the button, but replace `Gtk.Button()` with `Gtk.Label(label="Put whatever text you want here")`, and give it a different name.

If you add the label below the line where you added the button, it will appear *after* the button. If you put it above the line where you added the button, it will appear *before* the button.

Currently, widgets in the Box container are being placed horizontally. We can change the Box to be vertical by changing this line: `self.main_box = Gtk.Box()` to this: `self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)`. Try it and see what happens!

## Step 5: Customize!

We've added widgets, but now I'll show you how to customize them.

Let's start with the button. Try adding some text to it! You can do that by updating this line: `self.button = Gtk.Button()` to this: `self.button = Gtk.Button(label="Put whatever you want it to say!")`

Both the text label and the button are touching each other, along with the sides of the window, with no gap. Generally it's nice to have a bit of spacing between elements. We can add that spacing through CSS (Cascading Style Sheets), which is the language that we use for changing the visual appearance of things in our app!

Create a new file called style.css. This is where we will put the css code. In this new file, try writing:

```css
button {  
    margin: 30px;  
}
```

That will put 30 pixels of space on each side of the button. If you just wanted to put space on just one side of the button, you could do `margin-left` or `margin-top` etc for whichever side you want.

In order for it to actually work, you need to tell the app to use the css file. Near the top of the main.py file, right after the imports, add this:

```python
css_provider = Gtk.CssProvider()  
css_provider.load_from_path('style.css')  
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
```

Remember to save both the files, and see if it worked.

We can also change the colors! Within the button section of the css file, add a new line and type this: `background-color: green;`, you can replace the color with whatever. If you need a more specific color, you can use a hex or rgb color code([here is](https://htmlcolorcodes.com/) a color picker for hex and rgb).

You can also change the color of the *text* like this: `color: red;`

## Step 6: Adding functionality

Let's make the button actually do something! We'll start by making it print something to the terminal when you click the button.

Add this line after the part where you created the button widget: `self.button.connect('clicked', self.button_clicked)`

What does that do? It makes it so that whenever the button is clicked, it will trigger the function called `self.button_clicked`. But of course, we haven't created a function called `self.button_clicked` yet, so let's make it! I want you to create the function inside of the `MyApplication` class, but outside of the `do_activate` function. Create the function like this `def button_clicked(self, widget):`, then put a print statement in the function to inform us of whether the function is actually run when we press the button.

In case all that wasn't clear, your code should now look something like this:

```python
class MyApplication(Gtk.Application):  
    def __init__(self):  
        super().__init__(application_id="com.example.ExampleWeatherApp")  
        GLib.set_application_name('ExampleApp')  

    def do_activate(self):  
        window = Gtk.ApplicationWindow(application=self, title="My First App")  
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)  
        self.button = Gtk.Button(label="Put whatever you want it to say!")  
        self.button.connect('clicked', self.button_clicked)  
        self.label = Gtk.Label(label="Put whatever text you want here")  
        self.main_box.append(self.label)  
        self.main_box.append(self.button)  
        window.set_child(self.main_box)  
        window.present()  

    def button_clicked(self, widget):  
        print("Button clicked")
```

Let's try making a counter, where it adds 1 every time you press the button, and have it show the number in the app instead of printing it to the terminal.

First, we need to store the number of times we've clicked the button in a variable. In the `MyApplication` class, we made a function called `__init__`. The `__init__` function is run immediately when the class is created. In very simple terms, `__init__` is where you setup the classes attributes. Create the variable inside of the `__init__` function, like this: `self.times_pressed = 0`

To make the number go up each time you press the button, you *could* (inside of the `button_clicked` function) do `self.times_pressed = self.times_pressed + 1`, but there is a better way. Doing `self.times_pressed += 1` does the exact same thing, but is written more concisely.

Now, to actually make it display the number, let's make it update the text on the label widget to show the number. Right after the part where you add 1 to the variable: `self.label.set_text(str(self.times_pressed))`
