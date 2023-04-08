# Hey there I'm your boyfriend :) and I will show you some basics in python today.
#
# First off let's start with some theory and what you see on your screen:
# 
# What is python and why is it important? - Python is this fun and easy to use programing language for fun and 
# experementation you can use it to create fun little projects, like research one or a minigame or anything you want.
# The important part is that it's easy and fun to start with.
#
# How do I make a game? - For our cool games we have Unity Engine. It is a collection of helpful free tools that we 
# don't have to make our selfs. They help us make really cool looking games like the ones we played:) But we will 
# not be usinng them right now. Since for now we will just get familiar with the basics and python is perfect for
# that because of it's simplicity.
#
# Hmm files - On the left you will spot your folder called pystuff and inside you will notice a file called fun.py, 
# you can call it anything you want like even super_fun.py, though you gotta make sure that it ends
# with .py and that it doesn't have any spaces :) Inside your file you can write some fun code that the 
# computer will then execute. In here you can tell the computer to do whatever you want it to do.
#
# How do I run it? - We can run it by pressing that start icon on the top right corner and when we do it our comands
# will come to life. You can alternativly type in python and then the name of your python file where in this case it 
# is fun.py and then hit enter and whooo magic.
# 
# How do I make fun comands - Do you remember scratch, yes that fun game with the cat. In scratch you have these
# puzzle peices that you can drag and drop, and they cick nicely with each other, and you can mix and match those
# peices to make the cat do what you want. It is very simmilar in python. Here you also have puzzle peices, and
# can mix and match them in different ways to make the program do what you want it to do, shal we take a look.
#
# How do the puzzle peices work here and what are they? - Here you type out your puzzle peices and there is much
# more of them then in scratch ;) so that means you can do wayyy more. There are some built in ones that you can
# just type but there are also other ones from othe people that you can add and use.
#
# Puzzle peices basics - Lets start with our first puzzle peice. we call it a variable, though it could be called
# anything, you can call it cat, mouse, love_message or even boyfriend, (make sure not to have spaces). We can
# assign anything we want too our variable and then use it later in the program, our variable could be a number,
# a text, a song or a picture. Let's start with a text and a number

# here I'm ceating a variable I'm calling it my_cat and I'm assigning it the task (with =) of carying my number 3
my_cat = 3

# and here is another one I'm gonna call it daisy and assign it hmm... 
# maybe the text hi (nake sure to use 'and put the text inside')
daisy = 'hi how are you today?'

# TODO: here make your own below with a number or a text and you can call it anything you want and assign it anything :)

you = "you can't read"

# hmm pretty boring so far :( let's do something more exciting. So now we know how we can store basic information.
# But we can do that on a piece of paper as well. Well so let's make it come to life with something called functions.
# Functions are these building blocks that you can use to make things come to life. Let me show you how hey work;}

# so let's start by creating one, and then I will show you how to use them let's start with something simple
# maybe we could add 2 numbers together like let's say... numbers 2 and 3. So how could we do that? Well we
# could use this weird type of function called an operator.

# What is an operator? - well an operator isn't something you would really call a function, but it is some action
# that you can do in your code. I think some operators are probably already familiar to you from math like +, -, =,
# and there's more like <, !, *, /, and the list goes on. Though these operators don't necessarily have to do what
# they do in math.

# As you noticed we have already used an operator before, and that operator is =. This operator takes the value that
# you have created on your right hand side and assigns it to a variable that you have created on the left hand side
# in other programing languages you can create variables that are just empty and not assign anything to them.
# Though for now it will not be the case. So back to adding number you probably already guessed that if we write
# 2 + 3 then we create our functionality of adding those 2 numbers together, though if we just write 2 + 3 on it's
# own then it will not work. Though why? It's because we need to store the result somewhere and that's where
# variables come in. So we can do 2 + 3, and how do you think we could now store it. Yes your probably guessed it,
# we can do it by writing the following:

# In here I'm creating a variable called my_number, and I'm assigning it the result of 2 + 3
my_number = 2 + 3

# there we go, though that's not very interesting, but the difference between operators in math and in programing
# is that here they can work on other things, not just numbers things like text:
my_text = "Hi " + "Amelia"

# What do you think happens when we run the code above, what do you think my_text will be equal to?
# It's going to be 'Hi Amelia'.

# TODO: play around and try to create your own variable where you assign something cool to it you can hit run this time
# in the top left corner and see what happens



# How did it go? If you tried to be a little bit too creative like adding together a number and a text as so:
# my_variable = "Hi " + 3
# then you would probably get an error, in short errors are these helpful messages that will let you know
# if you did something wrong that couldn't be accepted by the computer. You can try removing the # from that
# my_variable example and then running it to see how errors look like and then putting the # back. If errors
# are really confusing then no worries we'll get to them later.

# Wait I know now what operators are, but what are functions? - Ahh yes functions, they are a bit different
# than operators because they allow you to create functionality that does maybe a bit more, let me show you

# So let's create our first function, I'll show you how to do it, and then you'll try to follow.
# A function in python always starts with the keyword def, the keywords stands for define.
# After we write the keyword we can give it a name, and this could be any name we want
# any name just like in variables. Though we can't create two functions with the same name
# then after we write the name we write these (), and then like a dot at the end of a sentence we write : instead.
# then after we've gone through that we can hit enter or go to the next line and hit tab, and we can start writing.
# our functionality that we want the function to do.
# Let me demonstrate:
def hi():
    nikis_number = 5
    my_number = 3 + nikis_number

# nice our first function,
# TODO: now try writing one your self below





# though if we run the code now we will not actually run the code that is inside the function we have just defined it
# to actually run it in the code we can just do the following to run the code that is inside the function
hi()

# And there we go just like that we ran our function, those variables ware created that we defined in the function

# So far functions seam pretty boring, well what if I maybe have a function but every time I run the function
# I want niki's number to be different. Well this is where these things called parameters come in
# inside these () we can actually create a variable that doesn't have anything assigned to it, and we can assign
# something to it once the function is called therefore nikis_number could be something else on every call.
# Here's a quick example of how to define a function like that:
def hi(name):
    greeting = "Hi, " + name

# now to call it we can simply do
my_name = "Niki"
hi(my_name)

# But also we could do
hi("Amelia")

# So there we go, though any variables that we create inside the function stay inside the function, how can we get
# them out, well here's another keyword that comes into play called return, return returns any a variable that
# you want it to return. In this example I create the variable greeting and I return it.
# it looks something like this:
def Hi(name):
    greeting = "Hi, " + name
    return greeting

# you can also do:
def hey(name):
    return "Hi, " + name

# then to call it and extract th variable we can simply do:
greeting = Hi("Niki")

# and greeting will now be equal to "Hi, Niki"
# TODO: As you already noticed there is a lot of room to play around so I'll give you some space to experiment:





# Hey I bet you got lot's of interesting results and discoveries. And you probably noticed that all keywords
# are colored differently, there's many more keywords that python has built in.

# Why do we need functions? - Well python has actually some really cool built-in functions and I will show
# you a few, and you can play around with them
# the first one we will take a look at is called print, it is function that displays something on your screen
# It does a lot of complicated stuff in the to make it happen but let's take a look at it. We can for example
# use it to see what are variables are equal to:

print("hi")

text = "what's up " + "Niki"
print(text)

# And another one that is really exciting is called input, it will get an input text from the user, and return it

print("What's your name?")
name = input()
print(hey(name))

# You can notice that there are just so many ways to mix and match, and I'll give you some room to play around
# to be continued...
