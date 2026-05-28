name = input("What's your name?\n")
if name == "Carlisle": # Notice that here we used two equal signs (=), whereas in the first line we only used one. Whenever you are SETTING the value of a variable, you use one =, but when you are comparing the value, like we are in this line of code, you use two = signs.
    print("Hi, you are such an awesome person!")
else:
    print("Hello " + name)