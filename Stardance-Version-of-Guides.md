##Welcome!
These guides will introduce you to Python, a popular starter programming language.

You do not need any coding experience to get started! By the end, you'll (hopefully) have the knowledge needed to make your very own app!

This series of guides is not yet done, and will be updated over time. But for now, enjoy :D

Make sure you have Hackatime setup before starting! Hackatime is what you use to keep track of how much time you spend coding, and we require you use it as part of how we verify you actually made something! Learn how to setup Hackatime [here](https://hackatime.hackclub.com/).

##Setting up Git and Github
:::callout type="info"
If you have already setup your Github repository, you can skip this section.
:::

First of all, what _is_ Git, and why do we need it? To start, Git and Github are two different things. Git is a tool for managing your code projects. You store each of your projects in a repository, and whenever you make an update to your project, you can "commit" the changes to the repository. Git will keep a history of every change you have made, so that in case your update accidentaly broke something, you can easily undo your changes! Now, Git*hub* is a free service that allows you to host your Git repository -- which has all of your code -- in the cloud, which makes it easy to access your code from anywhere. It also makes sharing and collaborating on projects much easier, and serves as a backup in case your computer breaks and you lose all of your code (This has happened to me 😞... **back up your stuff!**) Git is used all the time by programmers, and using it is an essential skill to learn.

First up... Make an account! Go to github.com and sign up for an account (it's free, don't worry).

Now, create a new repository, like so:

![Image](https://raw.githubusercontent.com/bunnybunnybun/Python-GTK4-Tutorial/refs/heads/main/images/new-repository(small).png)

Choose a name for your repository, and a short description. You can change these later. Set visibility to public and add README to on. For the "Add .gitignore" option, set it to Python. It's okay if you don't know what .gitignore is! It's not very important right now. And lastly, you can optionally set a license. You can use any license you want, or none at all, but do know that if you don't set a license, then nobody is allowed to use and improve upon your code in their own projects. I personally like to use an open source license, such as the [MIT License](https://choosealicense.com/licenses/mit/), which allows others to use my code in their projects if they wish.

![Image showing the create repository page](https://github.com/bunnybunnybun/Python-GTK4-Tutorial/blob/main/images/create-repository.png?raw=true)

Now copy the URL of your repository, you will need this soon!

![Image showing where to copy repository URL.](https://github.com/bunnybunnybun/Python-GTK4-Tutorial/blob/main/images/copy-repostiory-url.png?raw=true)

So you have a repository on Github, but you also need to have Git installed on your computer. To install it, follow the instructions on the Git website [here](https://git-scm.com/install/). The installer might have a ton of settings to change. It should be fine to leave the settings on the default values.

After you've installed Git, you need to clone the repository onto your computer. This will let you do the coding in the local repository (the copy on your computer), and then synchronize your code onto the repository on Github (this action is referred to as "pushing" your code to Github) whenever you make a significant change to your code!
 To clone the repository, we will use the newly installed Git. Git is used through the terminal. To launch the terminal, follow the instructions for whichever operating system you use:
:::collapse summary="Windows"
On Windows, instead of opening your regular terminal, you open Git's custom terminal app, called "Git Bash".
1. Press the ::kbd[⊞ Win] key.
2. Type ```Git Bash```.
3. Press ::kbd[Enter ↩].
:::
:::collapse summary="MacOS"
1. Press the ::kbd[⌘ Cmd] + ::kbd[Space] keys.
2. Type ```Terminal```.
3. Press ::kbd[Enter ↩].
:::
:::collapse summary="Linux"
The process can vary on Linux, but it's usually:
1. Press the ::kbd[⌘ Super] key (That's the same as the ::kbd[⊞ Win] key).
2. Type ```Terminal```.
3. Press ::kbd[Enter ↩].
:::

Now that you have your terminal open, you may be thinking, "What is this? It's just text, what do I do?". The terminal is a little confusing at first, because everything is done through typing commands. The terminal is used for many different tasks, such as creating, moving, and editing files, monitoring system resources, and using programs like Git (which is what we will be doing now).

In your terminal, type `git clone <URL of Github repository>`. Obviously, replace `<URL of Github repository>` with the URL of your repository, which you copied earlier. Press ::kbd[Enter ↩], and Git will clone the repository onto your computer.

:::callout type="tip"
💡Tip: Having trouble pasting the URL? Try doing ::kbd[Control+Shift+V] instead of ::kbd[Control+V].
:::

##Intro to Python
This is gonna be a little boring unfortunately, as we have to start out with learning the very basics of Python first, but in the next section you will start making an actual proper app!

First of all, you will need python3. This is might installed on your system already, but if it's not, [here's](https://realpython.com/installing-python/) the most comprehensive guide I could find on how to install it.

Open your file browser and find the folder of your project (it probably has the same name as the repository you created). Create a new file inside of that folder, and name it `main.py`. Open the file in a text editor (or a code editor/IDE if you wanna be fancy), it's time to start coding!

Let's start with the classic "Hello world" program!

In the main.py file, write this:

```python
print("Hello world!")
```

This is one of the simplest scripts you can make. It simply prints out the sentence "Hello world!"

To run the program you just wrote, open up the terminal, and type in this command: `cd <name of folder>`, but replace `<name of folder>` with the name of your project/repository. That will put you into the folder, just like when you open a folder in your file manager. Then run this command: `ls`. That tells you what files are inside of the folder you are in. You should see the file you made called `main.py`. Now run the command `python3 main.py` to execute the program!

If it ran successfully, you should see "Hello world!" printed to the terminal. Congrats, you've made your first program!

Try updating your code to this:

```python
name = input("What's your name?\n") # the \n tells it to start a new line
print("Hello " + name)
```

What's that do? The first line will ask for user input, and then set the value of the variable called `name` to whatever the user entered. Everything after the hashtag symbol (#) is considered a comment, which doesn't do anything. You can write anything there, it is just meant for leaving a note for yourself, to help you understand the code.

The second line prints out the text "Hello " plus the value of the `name` variable. Try running the new script by typing `python3 main.py` in the terminal again! It should ask you "What's your name". Just type something and press enter, and it will say hello to you.

I want the script to compliment me, but not other people, as a way to boost my ego. I can do this by using an if statement to check whether the name that the user entered is my name, and if it is, it will compliment them, and if not, it will say "Hello" like before.

Try it! Replace the print statement with this (but keep the first line):

```python
if name == "Carlisle": # Notice that here we used two equal signs (=), whereas in the first line we only used one. Whenever you are SETTING the value of a variable, you use one =, but when you are comparing the value, like we are in this line of code, you use two = signs.
    print("Hi, you are such an awesome person!") # Note how there are 4 spaces at the beginning of this line, that's called indenting, and it's how Python knows what is "inside" of the if statement. To add the 4 spaces, you can press the Tab key insteading of pressing the space bar 4 times.
else:
    print("Hello " + name)
```

### Making a clock

Let's try something new.

##What is GTK?
In the last section we learned the basics of how Python works, but now we want to make an actual app. In order to do this, we will use GTK. GTK is a library that allows you to make a window for your application, instead of just printing text to the terminal! When talking about coding, libraries are basically add-ons to the programming language you are using; They give you access to more functionality!

Remember, if you don't understand everything that's coming up in this guide, that's fine! Coding can be very difficult when you are starting out. 
If at any point you feel overwhelmed, my biggest recommendation is to take a break and come back later.
If something doesn't make sense and you want help, feel free to ask in the [#python-stardance-mission](https://hackclub.enterprise.slack.com/archives/C0B726SAPV4) channel on Slack!

##Installing the required libraries
Time to install the libraries!

You will of course need GTK itself, but also PyGObject, which allows you to *use* GTK in Python. Instructions for how to install them can be found on [the PyGObject website](https://pygobject.gnome.org/getting_started.html).

To check if the libraries are installed correctly, open up the main.py file in your text editor, and replace the current code with this:

```python
import gi  

gi.require_version("Gtk", "4.0")  
from gi.repository import GLib, Gtk, Gdk
```
That will try to import the libraries. Run the program. If it gives an error, check to see that you installed everything correctly. Otherwise, continue onward!

##Make a blank application window
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

It's okay if you don't understand everything that we just wrote. Try saving and running the program, you should see a blank window appear! In the next section, I'll show you how to make it, well, not empty!

##Add some widgets!
GTK apps are made by combining widgets. There are lots of types of widgets, such as buttons, text boxes, or containers. Containers are used for specifying where other widgets go, by placing said widgets inside a container widget. Some types of containers are grids, panes, etc. You can see a list of all possible widgets [here](https://docs.gtk.org/gtk4/visual_index.html).

The first widget you add should always be a container widget, so you can put more widgets inside it. I usually start with the Box widget.

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

##Customize!
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

##Adding functionality
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
