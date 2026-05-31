name = input("What's your name?\n")
if (
    name == "Carlisle"
):  # Notice that here we used two equal signs (=), whereas in the first line we only used one. Whenever you are SETTING the value of a variable, you use one =, but when you are comparing the value, like we are in this line of code, you use two = signs.
    print(
        "Hi, you are such an awesome person!"
    )  # Note how there are 4 spaces at the beginning of this line, that's called indenting, and it's how Python knows what is "inside" of the if statement. To add the 4 spaces, you can press the Tab key insteading of pressing the space bar 4 times.
else:
    print("Hello " + name)
