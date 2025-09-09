# Westwardfishdme's Guide to succeeding to COMP170

## Content
non-textbook materials...
- [Introduction](#introduction)
- [Useful Misc. Youtube Videos](#miscellaneous-videos-and-other-learning-resources)

[A comprehensive guide to the class](#the-guide-for-comp170)

- [The `print()` function](#print)
- [Proper syntax](#syntax)
- [Types](#basic-types)
- [Functions](#functions)
- [Variables](#variables)


## Introduction

Welcome! My name is Jonathan. I am an open source dev, with some free time 
on my hands, so I came up with this idea to create a github repository for 
students learning Python in COMP170. Whether this is your introduction to programming,
or if you want to become a hobby developer like me, this class will be 
extremely influential in your journey as a developer, and will hopefully demystify the intricacies
of computer programming. 

I'm going to **try** to create youtube videos for each weeks topic; at the time of
writing this we are on week 3, and just covered `data types` in Python today. 
I also included someone else's playlist on [python](#miscellaneous-videos-and-other-learning-resources), 
but in my videos, granted that I get permission from Dr. Ennaoui and the other professors of the course--
cover previous homework problems from the textbook, and list them here as unlisted videos.

A little bit about me:
- I have been programming since I was about 13, I know numerous languages but have primarily worked in C, Rust, and Bash.
- I have written highly intense software projects, most you can see on [my github page](https://github.com/westwardfishdme)
although, I have kept some in private due to me not wanting to share all of my projects.
- Currently, I am learning concurrent programming in Rust, which is very important for programming software for server/client models, hats off to you if you know that.
- Although I have worked with python before in my youth, and it's been years since I've used the language, I still have
a lot of experience in both writing it and reading it statically. 

Don't let that last point fool you! Once you master how to view patterns in programming languages, 
you can see how knowledge overlaps between languages. The truth is, you can use any language to write
any program. A developer's choice in programming language is either by design or preference, and sometimes these reasons can overlap!

You can see an example of that in this [video of a guy writing a whole webserver in bash.](https://www.youtube.com/watch?v=L967hYylZuc)

If you feel like the video is too advanced, or too long, feel free to not watch it BUT I recommend you at least read my explanation of why that video matters here:

Bash is not typically used to write such advanced software as the guy in the video was making, i.e. a webserver that can host a website, BUT he managed to not only make it work,
but eloquently wrote it all in bash, without any the use of any other languages. There are some segements where he implies that there might be modules that needs an implementation in C,
but nonetheless, he omits that from his final project, and accomplished an extraordinary task that I recently didn't even know was possible until he did it and mentioned other projects
that accomplished the same thing.

The reason why I say this and mention this video at all is because this course is not designed to just teach you python, but to teach you the skills necessary to become a decent enough
programmer to create and problem solve. Great programmers like the guy in that video, Dennis Ritchie, Grace Hopper, or Steve Wozniak didn't just become magically good at programming,
they became great programmers because they practiced and learned how to solve difficult problems using **pattern based thinking.**


Needless to say, I am relatively 'advanced' in the field, but like y'all I am still learning.

### Why I made this, how you should use it, and covering past assignments.
I was inspired to make this repository because someone in class asked if I could synthesize a list of youtube videos for them 
to watch to learn how to program. On my train ride home, I thought to myself:

"Damn, I can literally write an actual guide for the whole class if I really wanted to..."

and so I did, it's the one you're reading right now ;)

Most information will be passed along in this single readme, but I might change that. 
This repository is going to be less vague than the textbook, and not depending on the how specific I get, more or less in depth and advanced. I will try my 
absolute best to make it as digestible as possible for intro programmers. 

Since I am a full time student however, and I cannot fully invest all of my time into synthesizing 
all information properly, feel free to send a pull request or send an issue and I will look through
to publish any contributions made to this little pet project.

Additionally, I will only do what is taught already in class. That is if I hadn't already gotten ahead of myself in some sections, 
but I tried to leave some resources linked for you to read upon if you're interested.  

You should try and use this as any other study guide, or as a comprehension of the textbook. 
I also included some bonus information and some good practices for you to look at with some examples.
Inside of the example folder I also included a really easy to digest comprehensive python project that
I wrote with numerous comments to help understand what is happening, what interacts with what, and so on so forth.

(I haven't finished that yet, but you'll see it here if you check back at a later date...)

As per the syllabus, I am unable to share my answers with you (bummer...) but I highly incentivize you to
try to commit yourself to doing those assignments. While they seem REALLY difficult, I promise you they do actually
teach you how to think algorithmically, and coming from a lifelong independently learning programmer who has gone to 
learn python 3 times now from schools (elementary, high school, and college now...), those exercises really do help.

With that said, I hope this guide serves you well, and you find this easy to learn!

## Miscellaneous Videos and Other Learning Resources
Here are some other resources you should check out to help study and learn, these aren't necessary, but if you
are truly interested in programming, these are some books that I had read and videos 

**LEARNING HOW TO PROGRAM IN PYTHON, AND HOW TO THINK LIKE A PROGRAMMER**
- [Fireship's wonderful video on how you should learn how to code](https://www.youtube.com/watch?v=NtfbWkxJTHw)
- [NetworkChuck's playlist on coding in python](https://www.youtube.com/watch?v=mRMmlo_Uqcs&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp)
- [Coding is easy, actually](https://www.youtube.com/watch?v=qkFYqY3vr84)
- [GeeksForGeeks Python Tutorial Module](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/) << this is how i learned python when i was young.
- [How to Read Documentation Effectively](https://www.youtube.com/watch?v=q0trIfryGvY)
- [Official Python Documentation](https://docs.python.org/3/tutorial/index.html)
- [5 Good Python Habits](https://www.youtube.com/watch?v=I72uD8ED73U)

**BOOKS UNRELATED TO THE COURSE THAT I THINK YOU SHOULD CHECK OUT**
- [The Hacker Ethic and the Spirit of the Information Age](https://archive.org/details/TheHackerEthicAndTheSpiritOfTheInformationAge)
- [Algorithms - Panos Louridas](https://www.amazon.com/Algorithms-MIT-Press-Essential-Knowledge/dp/0262539020)

You don't have to check these videos out at all, but they do help reinforce REALLY good learning habits when it comes to programming,
they were videos that I have sent out to my friends who have asked me how to learn how to program, and it's helped them in their careers.

The book on the hacker ethic isn't just necessarily pertaining to computer 'hacking' but is rather a change in mindset to how one accomplishes
their goals through their principles. This video from [14 years ago synthesizes the essence of the book pretty eloquently.](https://www.youtube.com/watch?v=l6iMdsey4uI)
 
# The Guide for COMP170
## Print 
In almost every programming language, there are ways to output messages or as we'll learn later, 
variables to the screen this is almost always called `print`, but some languages will have a slightly
different nomenclature for it, 

i.e. 
- java ->`System.out.println()` 
- javascript -> `Console.log()`
- bash/posix shell -> `echo` or `printf`
- C/C++ -> `printf`
- Rust -> `println!()`

Print will almost always be there, and it's the best way to first learn how to use a language, as you can visually
see what's going on inside of the computer, whether that is printing out variables, or the results of maths 
equations, `print()` is going to be your __best friend.__

in python we can simply call `print()` like so:

```py
print("hello world!")
# or with single quotes:
print('hello world!')
# note: in other languages, single quotes typically only designate a single character,
# which is it's own type in most other languages, but not python.

# so while it is perfectly OK to use single quotes to print out a message, it is almost
# always best practice to use double quotes (") wherever possible.
```

Slightly advanced note: 

print statements will always produce STDOUT (standard output) which is a special form of output.
This is because of how computers were originally designed to handle the 3 types of data flow:
- STDIN (Standard Input)
- STDOUT (Standard Output)
- STDERR (Standard Error)

The only other form of output is STDERR, which sends a special message to your computer to handle these messages
slightly differently to STDOUT. 

STDOUT **should** be used to output desired products of data, while data outputted by STDERR should almost always
be used to print out **debugging information**. As you grow in your journey as a developer, you will find this to be very important
when designing programs that have very robust and complicated processes, and will have to handle specific cases
where you have STDERR, and STDOUT messages occuring.

## Syntax
If you're using a fancy shmancy IDE (like me), you'll more than likely get warned about this as you write code.
Typical IDE's will underline the improper code with red underlining, or a variation of which and tell you what
exactly needs to be done to fix the error. An example of improper syntax would be:

```py
print(hello world
# notice how we're missing the quotations, and parenthesis like the proper output:
print("hello world!")
```
Python CAN use semicolons, but typically this is done either as a stylistic choice, or a on page formatting solution.
However, unlike most languages, it does not require them, which will become a muscle memory issue as you learn more languages.

You can use semicolons to do something on a single line, but note that this is not really done in python, and does
reduce the readability of your code:
```py
print("This sentence was too long for me");print("so i used a semicolon for another print statement.")
```
Syntax also includes proper indentation, fulfilling missing functions, and fulfilling missing keywords and their proper implementations.

Indentation is the most important, as it dictates the control flow of functions, loops, if statements, and match/case
statements (also something we haven't covered yet, but it's like a special `if/then` statement, i'll explain later.) 

## Basic-Types
So far in class, we have covered the following data types:
- [int](#integers) (integers; like 1, 2, 3, 4 ...)
- [float](#floats) (floating point numbers; 1.4, 4.29 3.39)
- [string](#strings) (line of text)
- [boolean](#booleans) (boolean algebra; True, False statements)

When writing a program, knowing the types is the difference between your program succeeding, and failing
to run. In other cases, using improper types can cause undesired output, or even crashes.

**Something important to note!**

You can do this really cool thing called 'typecasting' where you can turn types into other types, this is best shown with integers, floats, and strings.
Try this out in the IDLE/python shell!:
```py
>>>int(12.0) # will give you the integer '12'
12
>>>float(12)
12.0
>>>str(120)
'120'

```
Type-casting will be an important skill to learn, as you will need that when you concatenate say a string with an integer. I'll show an example of this later.

#### Integers
Integers are just as they sound, numbers. 

Integers are defined from going from -infinity to +infinity, and will be frequent in programming.

In most languages there are 2 types of integers: signed and unsigned. 
You don't need to know the complexities but it sounds exactly like how it does:

one is 'signed' with positive and negative numbers, and the other is 'unsigned', which just only positive numbers are allowed.
There is also the byte count which is how large the number can reach (8 bits, 16 bits, 32 bits, 64 bits, some languages even support 128 bits).

**However, python only has one integer type, and almost no limits on it either.**

*Python does have a partial limit of being able to print up to 4300 digits when converting integers to strings-- but that number is theoretically unlimited as you
can technically increase that limit.

#### Floats
Floats are just decimal numbers, you can do math with integers with them, or with each other.

Floats are going to be your biggest enemy and your biggest friend. They are also a total pain to deal with if they don't work as intended.

If you want an example of why I think they're a pain, try doing this simple equation in idle or the python interpreter:
```
120.1-120
answer=0.1 (super easy right?)
```
Here's what happens if you do that in python:

```py
# in the idle/python shell
>>> 120.1-120
0.09999999999999432
```
You should quickly notice that is not the right answer, and that happens because of what is described in this video [here.](https://www.youtube.com/watch?v=PZRI1IfStY0)

Floats will be very painful if not handled properly, and you have to keep track of their precision-- this is actually language agnostic as well, meaning that most 
programming languages suffer from this.


AFAIK, there is no implementation to directly solve this python without you having to write extra code to ensure that the a result from a
problem such as `120.1-120` is arithmetically correct. That isn't to say that there aren't workarounds to this issue. 

You can mitigate this with tools that python provides, but note that this is an issue that has to do with how numbers are represented within a computer.


#### Strings
Strings are the easiest to identify and use, and we've used them in every assignment, and in `print()` statements already.

I don't have much to say other than to try to think of them as an **array of characters**.

For example the string: "hello world" should translate to this:
```
"hello world" = ['h','e','l','l','o',' ','w','o','r','l','d']
```
That might look confusing, but I promise you, this is how you should think of strings, because that is what strings are.

We haven't covered this *yet*, but think of arrays as a **container** of data, with indexes pointing
to different data types. In python it's called a **list**, and **arrays** are something different. So in an effort
not to confuse you:

"Arrays" in other languages are lists which look like this in python:
```py
my_list=[1,2,3,4,5,6]

```
In python, we do have specific arrays which can be invoked with:
```py
import array as arr # WHAT IS THIS?????? (we'll cover these later too...)

# we haven't learned any of this yet, so i won't say any more, but they function *similarly* to lists, but are slightly more advanced.
my_array=arr.array("hi!",1)
```
If you want to read more on this check out this page from [GeeksForGeeks](https://www.geeksforgeeks.org/python/python-arrays/) I also used their example here to show you how an array is initialized.

Strings are considered an 'array of characters' in almost all languages, meaning that you can do special things with strings,
and when we get to that point in class, I'll update this document to help assist in understanding how arrays work.

#### String concatenation and special characters
As we have already discussed in class, we can print out and use `print()` in special ways to format our
code in different ways. We already learned about `'\n'` and `'\t'` (newline and tab respectively).

We also learned that we can concatenate within a string with `+` and `,` within the print statements.

For example, we can use a one liner to print out:
```
I am a programmer,
I love to write code!
```
with: 
```py
print("I am a programmer,"+'\n'+"I love to write code!")
```
instead of 
```py
print("I am a programmer,")
print("I love to write code!")

```
It's important to note that `,` will produce a space while `+` will not, as Dr. Ennaoui also mentioned.

You can also multiply strings into one another, for example:
```py
string="hello! "
cool_string=4*string
print(cool_string)
```
This code will print out:
```
hello! hello! hello! hello! 
```
For some of the homework problems, you can actually use that to solve some of the problems, i.e. for my rocket ships
I used a parameter to multiply the strings to allow the user to print more than two rockets if they wanted.

The limit was up to their imagination...

#### Booleans
Easiest one: True or False statements.

Python also supports the usage of expressions to represent boolean values, for example:

```py
print(1>2) # Output is false.

```
Boolean expressions are fundamentally the most important part of any programming language.
They determine what is called "control flow", and I'll also write about this as we do cover this later in class.

Basically, all you need to know right now is that boolean means True or False, thats it, they can only be those 2 values.

If you're interested in the theory, it follows the logic of electric circuits. 1 being on, 0 being off.
See this [crash course video](https://www.youtube.com/watch?v=gI-qXk7XojA) to understand the depths of booleans,
although you should just keep note from the 3 minute point onwards.

## Functions

Functions are blocks of code in a function that either are called numerous times within your code OR added to help make your code more readable.
It is best to try to reduce the amount of code you repeatedly write when programming because this code is easier to maintain and much easier to
read overall. 

When it comes to programming, it is always best to make your code as *modular* as possible. What do I mean by that? I mean that when writing code, you 
should always opt to make it so that if you need to reuse a portion of your code again in another section, or if you want to be able to reuse code, you
should always try and plan ahead to determine what each function and part of your code does as to not cause yourself too much hassle in maintenance.

This will be **EXTREMELY** important when we get to later chapters where we cover imports as well. If you are on the path to becoming a developer, you need to 
learn how to write your code as compartmentalized and as readable as possible. You'll come to understand why that is extremely important in collaborative projects 
if you ever get to that point in your career.

I still struggle with this in my current projects, but understand that good code comes with a lot of practice and learning how to break problems up 
properly will help you do that.

Here are some easy do's and don'ts when writing functions:
#### Do's
- Compartmentalize your code; use functions to break your code into modular pieces that can be called individually.
- Use functions as a way to reduce repeated patterns of code.
- Name your functions and parameters accurately, avoid vague naming schemas.
- If possible, give your functions a return type, being able to pass variables into functions and printing out the result of a function is a very
useful skill and tool that will be important in your journey. In my example program, I show how this is done to eloquently print out a user's name
and greet them with using only a function. 

#### Don'ts
- Write functions that aren't used in your program; this is called 'dead code' and is considered a waste of resources.
- Nest functions within functions, it sounds really weird, but yes you can define a function within a function. You don't want to do this because it makes
your code less readable.
- Give your functions or parameters very vague names, unless you are purposefully obfuscating code it just makes your program harder to maintain and less
readable.

### Parameters
Functions come with this thing called parameters. They're essentially inputted variables for your function to work with. The little parentheses like those in `main->()<-`
always dictate the inputted parameters of a function. It is important that when writing functions to always include those parentheses when defining because a 
function is something that always will have parameters even if there is none (like `main()`)

You can have an infinite amount of parameters, however I usually limit it to 4 at max, at which point, I would write other functions to perform different things.
For example:
```py
def addition(num1, num2, num3, num4): # nums{} are my parameters
  return num1+num2+num3+num4

def multiply(num1,num2): #lets multiply some numbers too, their parameters are named num1 amd num2.
  return num1*num2

def main():

  # see the section on variables.

  result1=addition(10,20,30,40) #adds all these numbers together... (result1=100)
  final_result=second_round_add(result1, 30) # multiplies result1 by 30... (100*30)

  print("Result:",str(final_result))#print out the result of 3000, notice I how I typecasted to print out the result.

main()
```
This looks complicated now, but hopefully the sections below clears some of this up for you.

### Returns
In all programming languages a function can do more than just do a specific task, it can be attributed a type as a return value.
Say I had a function `add()` which took two parameters `num1` and `num2`, which can be either a float or an integer, but I only
want it to give me my result as an integer.

When I write the function `add()`, it might look something like this:

```py
def add(num1, num2):
  return int(num1+num2) # i can just cast the whole equation as an int, and this will always return type int.
```
Thinking of functions like this will help you out with soooooo many programming problems. Not only because it makes your job a lot simpler,
but because you have to will be able to pre-plan what functions will do inside of your program, allowing you to delegate responsibilities
to certain functions.

However, returns can also be used to give signals:
```py
# i haven't talked about if statements yet in depth, but they just check boolean values...
def some_function(some_string):
  if some_string=="hi":
    return 2
  elif some_string=="goodbye":
    return 1
  else:
    return 0

# you can also write this as a match/case statement.
# you should do this if there are more than one possibility so
# you don't have a million if elif statements.

def some_function_using_match(some_string):
  match some_string:
    case "hi":
      return 2
    case "goodbye":
      return 1
    case _:
      return 0
```
These will return either the values {0,1,2} respectively should the conditions of `some_string` are "hi", "goodbye", or anything else.
It is also probably important to note that it's not setting some_string is lowercase, so if you were to have `some_string` be something
like "Hi", "hI" or "gOodbYe" it will always return 0.

This is called input formatting, which I'll likely cover at a later date.

## Variables
Variables are the primary method of storage in any programming language. In almost all programming languages you must specify the type, however what makes
python super easy and special is that types are inferred by your definition.

Here are some examples of how python performs automatic type inference:
```py
my_integer=12 # this will be inferred as an integer

my_other_integer=0x15 #we haven't covered this yet, but this is 21 in hexadecimal (base 16) and it counts as an integer!
# hexadecimal is super important in the field of computing, hopefully we'll see why later.

my_string="wowzas!" # will always be inferred as a string

my_float=12.0 # any number with a '.' to separate decimal values are always inferred as a floating point integer.

my_bool=True # is inferred as boolean, but also see my example below:

my_other_bool=(my_float > my_integer) # this is also inferred as a boolean type!

```
Something that will reduce future headaches is to immediately define a variable with a predefined type.
You don't have to, but it will seriously help reduce headaches in much more complex and complicated programs.

You would do that like this:
```py
my_int:int = 12

```
With something like this, it helps to read your code and keep track of variables, especially when you start having complex things happen to them, like throwing them through functions as parameters.

#### Proper naming
Functions and variables cannot start with certain keywords, characters, or generally numbers, this section will cover that.

This guide from [Geeks4Geeks should also help](https://www.geeksforgeeks.org/python/what-are-the-allowed-characters-in-python-function-names/)

Generally speaking, you should always try to name your functions as to what they specifically are as much as possible.
A good example of this would be:

```py

# in this program, we do some basic returns to show us how we can use functions and variables properly to understand what
# our program is doing.

def addition(num1, num2):
    return int(num1+num2)


def greetUser(username):
    return "Hello "+username+" long time no see!"


def userFriend(friend_name):
    return "It's me your best friend "+friend_name+"!"


def main():
    # my friend Tyler is telling me hello!
    greetings = greetUser("John")
    friend_greeting = userFriend("Tyler")

    # we also can do some addition
    sum = addition(4, 5)  # should give a sum of 9

    # you can use a comma, but sometimes its best to learn practice proper string concatenation...
    print(greetings+" "+friend_greeting)
    # you don't have to, but you should always type cast integers as strings, as it helps build good practice. Should print out our result of 9.
    print(str(sum))


main()

```
##### Improper names!
Python is a very finnicky language, and as such you have to name functions and variables properly.

- A function or variable cannot start with a number.
- Best to avoid weird characters like "@", ")" or "*" for example...
- No spaces!

see this [blogpost](https://itoolkit.co/blog/2023/08/what-variable-names-are-illegal-in-python/) for more information.

##### Special Keywords
Special keywords include any key word that the python interpreter will not accept as a variable OR function name:
- `if` is an example...
- `not` is one as well...
- `for` is another keyword...
- `def` is also another keyword...
- so, so many more. see this list [here]()

You may have noticed I didn't say any 'types'
While you can use types as function names, it is generally not recommended as it messes with the actual data type and can redefine functionality.
unless you are doing this for a very specific reason, it's best practice to not do that.

```py
def int(): # DONT DO THIS!!!
  pass # oooooh another secret keyword!
``` 

