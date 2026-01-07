
# Westwardfishdme's Guide to succeeding to COMP170

## Content
non-textbook materials...
- [Introduction](#introduction)
- [Useful Misc. Youtube Videos](#miscellaneous-videos-and-other-learning-resources)

Completed sections:

[A comprehensive guide to the class](#the-guide-for-comp170)

[Python Basics](#python-basics)
- [The `print()` function](#print)
- [Proper syntax](#syntax)
- [Types](#basic-types)
- [Functions](#functions)
- [Variables](#variables)
- [Expressions](#mathematical-expressions)

[User Input](#input)
- [How to handle user input properly](#handling-user-input)

[Control Flow](#control-flow)
- [Logic in Python](#logic)
- [If-Elif Statements](#if-elif-statements)
- [Match/Case Statements](#match-case-statements)
- [Pass Statements](#pass-and-break-statements)

[Iterators, and Recursion](#iterators-and-recursion)
- [For loops](#for-loops)
- [While loops](#while-loops)
- [Recursion](#recursion)


[Error Handling](#error-handling)
- [Exit and Errors](#exit-and-errors)
- [Try/Except statements](#try-except-and-finally-statements)

The following sections are unfinished and will be appended to at a later date:

[Imports and using libraries]
- [Using python's built-in libraries]
- [Using self-defined libraries]
- [Using pip to install libraries]

[Methods, and Classes](#methods-and-classes)
- [What is a method?]
- [Python classes]
- [Class Attributes]
- [Writing custom objects]


[Advanced Python]
- [Asynchronous python]
- [Input Sanitization]


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

### LEARNING HOW TO PROGRAM IN PYTHON, AND HOW TO THINK LIKE A PROGRAMMER

This specific section is dedicated in providing resources to help learn how to think like a programmer, and build foundational
principles for learning. You might notice that some content creators kinda sh*t on academia, but
that's because for the most part, programming is a skill that most really great programmers learn how to do on their own time.

It does breed this toxic culture, but I'm neither here nor there on how someone learns concepts. I think that academia provides
people with a great framework to learn these concepts, but to really solidify knowledge, I would take a listen to what people
say who learned how to program independently, as they *typically* have better inputs, but that is not always the case.

- [Fireship's wonderful video on how you should learn how to code](https://www.youtube.com/watch?v=NtfbWkxJTHw)

This video does a wonderful job in introducing programming concepts, and I think helps build some concepts in your journey as a programmer.
- [Crin's wonderful video on how to learn how to programming](https://www.youtube.com/watch?v=kNareBFFWtQ)

Same as the video above, but from another content creator's perspective :3
- [NetworkChuck's playlist on coding in python](https://www.youtube.com/watch?v=mRMmlo_Uqcs&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp)

I would use this playlist as a way to help solidify what we learn in the course. 
- [Coding is easy, actually](https://www.youtube.com/watch?v=qkFYqY3vr84)

Same as the first 2 videos.
- [GeeksForGeeks Python Tutorial Module](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/) << this is how i learned python when i was young.

G4G is the programmers best friend, I'm not joking Geeks4Geeks will carry you in learning any concept. It's user guided, and explains concepts with details.
- [How to Read Documentation Effectively](https://www.youtube.com/watch?v=q0trIfryGvY)

I would use this video once you get more advanced in python, but this is a language agnostic concept
that I think serves the purpose of learning very well.
- [Official Python Documentation](https://docs.python.org/3/tutorial/index.html)

This is the official Python documentation. I know for beginners you will look at this and think "WTF is this?" but I promise you 
official documentation of any language will be necessary in not only understanding what is happening under the hood, but better
conceptualize what certain functions and modules do.
- [5 Good Python Habits](https://www.youtube.com/watch?v=I72uD8ED73U)

Use this video to help organize your code better. I'm not even kidding the #1 career-killer in programming is
having extremely disorganized, vague, and error-prone code. 

### Topics/Wiki articles you should study to help you succeed in programming

These articles aren't Python Specific, but I highly recommend you read them.

- [The Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy)
- [KISS Principle (Keep It Simple, Stupid!)](https://en.wikipedia.org/wiki/KISS_principle)
- [DRY Principle (Don't Repeat Yourself)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [Modular Programming](https://en.wikipedia.org/wiki/Modular_programming)
- [What is Pattern-Based Thinking?](https://www.knapsack.cloud/blog/pattern-based-thinking)


### BOOKS UNRELATED TO THE COURSE THAT I THINK YOU SHOULD CHECK OUT

I love reading, but I understand that reading is not for everyone, if you are heavily invested into computers, computer science in general,
or want to build better programming skills, I would check out some of these books

- [The Hacker Ethic and the Spirit of the Information Age](https://archive.org/details/TheHackerEthicAndTheSpiritOfTheInformationAge)

The book on the Hacker Ethic isn't just necessarily pertaining to computer 'hacking' but is rather a change in mindset to how one accomplishes
their goals through their principles. This video from [14 years ago synthesizes the essence of the book pretty eloquently.](https://www.youtube.com/watch?v=l6iMdsey4uI)

- [Algorithms - Panos Louridas](https://www.amazon.com/Algorithms-MIT-Press-Essential-Knowledge/dp/0262539020)

I read this book a few years back, but to summarize it-- the matter of algorithmically thinking is such an important skill
in today's world. It kind of just gives the reader some basic ideas of what algorithms are, and how someone with an algorithmically-thinking 
brain will tackle such problems.
- [The C Programming Language](https://www.cs.sfu.ca/~ashriram/Courses/CS295/assets/books/C_Book_2nd.pdf)

So the C programming language itself is not something that we cover in this course specifically, but C is such a fundamental language in
computing, that NOT reading it or knowing about it will be extremely detrimental in your career as a programmer as most languages are either
based or written in C (such as python, which uses C in it's backend)

If you don't want to read a whole other book, which I totally understand, you can either check out the wikipedia article [here](https://en.wikipedia.org/wiki/C_(programming_language))
or this video of why C is so important [from computerphile here.](https://www.youtube.com/watch?v=ci1PJexnfNE)

### In summary...
You don't have to check these videos or articles out at all, but they do help reinforce REALLY good learning habits when it comes to programming,
they were videos that I have sent out to my friends who have asked me how to learn how to program, and it's helped them in their careers.

# The Guide for COMP170

# Python Basics
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

print statements will always produce STDOUT (standard output) which is a special form of output, unless
given as an argument inside of the print statement to print to another file otherwise.

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

To print to STDERR, you can do so like so:
```py
import sys
print("hello world", file=sys.stderr) # prints to stderr
```

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

Indentation is the most important, as it dictates the control flow of functions, loops, if statements, and [match/case](#match-case-statements)
statements (also something we haven't covered yet, but it's like a special [if/then](#if-elif-statements) statement, i'll explain later.) 

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


AFAIK, there is no implementation to directly solve this in python without you having to write extra code to ensure that the a result from a
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
useful skill and tool that will be important in your journey. In my [example program](rock_paper_scissors_example/), I show how this is done to store the result of the computer randomly
choosing an index to return a string. 

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
  final_result=multiply(result1, 30) # multiplies result1 by 30... (100*30)

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
- Best to avoid weird characters like "@", ")" or "*" for example, as these are specially assigned characters read by the interpreter.
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
## Mathematical Expressions
In python you can use math. The general rule of PEMDAS is typically followed, but occasionally, 
there are some weird exceptions to how math is performed in python.

Generally speaking, your operators are the following:
- `({exp})` for parenthesis based values.
- `**`      for exponents.
- `%`       for modulation.
- `/`       for division.
- `//`      for floored division.
- `*`       for multiplication.
- `+`       for addition.
- `-`       for subtraction.

In addition the only two types of variables that can perform math is `int` and `float` respectively.
Generally speaking, you can use them interchangeable, however it is to be noted that expressions 
that use `float` variables will always return `float` answers.

For example:
```py
>>> 1+2.0
3.0
```

You can specifically cast the types if you wish to retain a specific type, for example:
```py
>>> int(1+2.0) # will always return an integer.
3
```
There are also specific operations that will always return a specific answer. These operators are:
- `/` will try and attempt to divide into an accurate float
- `//` will always divide and return the floor value, e.g 
```py
>>> 4.4//2
2.0
```

### Modulus (% operator)
In this guide, I have to include a section on modulo because it is something that people aren't used to seeing be done as an operation,
but nonetheless a **VERY** important operator. The best and easiest way to remember what modulo (`%`) does is that it returns the remainder.
Think of it like a clock:

```py
>>> 13%5
3
# When I say think of it like a clock, it's because in a case like x%5=y,
# y can only be in the range of (0,1,2,3,4)
```
So when you see something like `13%5`, try to see it like this:

1. let our expression be `13%5`
2. let us perform whole number division, and find the remainder.
3. `13/5=2` with a remainder of `3`,
4. Therefore `13%5` = `3`

Another way you can visualize it is: how far away from the lowest possible result that isn't a float value be?

1. let our expression be `265%100`
2. our lowest possible correct result that would not be a `float` is `200`,
3. we are `65` points away from `200`.
4. Therefore `265%100` = `65`

IMPORTANT TO NOTE:

Modulation is similar to subtracting, but is NOT subtraction itself! You use modulation in a very different way in comparison.
For example, a good example of this is like writing a clock function:
```py

def clock_from_secs(seconds_from_start):
  if seconds_from_start > 3600:
    # get the human readable time from something like 6534 seconds
    seconds = seconds_from_start % 60 # gives us the seconds,
    minutes = (seconds_from_start % 3600) / 60 # gives us the minutes.

  print(str(minutes),"minutes",str(seconds),"seconds")
```
I have a few programs that utilize this algorithm in other languages, but this is python edition :3

### Advanced mathematic expressions.
for more advanced calculations, and math principles, we would have to use the [math module](#using-pythons-built-in-libraries) (not complete yet!)

# Input
Python actually makes reading user input really easy. You can do this a numerous amount of ways,
but for most beginners it's best interpretted by using the `input()` function. You can invoke
`input()` by writing the following code:
```py
def ask_question():
  my_answer=input(str("What is your favorite color?: "))
  print("Your favorite color is:", my_answer)

def main(): 
  ask_question()

main()
```
notice how I specified the type inside of the `input()` function:
```py
my_answer=input(str("What is your favorite color?: "))
```
This is normally how you will see people dictate the expected input of what the user inputs,
and you can check the validity of user inputs with boolean logic, which I will cover in the next
section on control flow.

## Handling User Input

In your journey as a programmer, you will begin to learn why programmers hate user input.
This section is kind of designed in a manner to explain how to handle some simple ways and
thinking processes to better handle external inputs to your program.

I say you will hate user input, because it is the most tedious, and most annoying thing a programmer
has to deal with.

The best way I can describe why it's such a pain is because of the following reasons:

1. A user can input whatever the hell they want.
2. Because a user can put in whatever the hell they want, they can easily crash the program, or introduce bugs you will have to go back and fix.
3. This process usually involves hours upon hours of rewriting numerous lines of code, or hours of variable tracking to figure out exactly where 
these bugs occur. Thus inducing so many migraines in the process.

Generally speaking, you want to treat user input with as little trust as possible, and install the most amount of safeguards possible. Especially in a
language like python because of how variable types are handled with very little pre-emptive definition. What does that mean?

```py
# say we ask a user for a number.
user_num=int(input("give me a number!: "))
# they put in 'three...'
```
Now the whole program goes kaput!

Now there are mitigations, and once we get to [try/except statements](#try/except-statements) we will cover how we can leverage `try/except` statements to better
handle user inputs.

Specifically this gives a ValueError where the type String cannot be parsed into an integer, which we'll cover in the section titled [Exit and Errors](#exit-and-errors)
which is incomplete at this moment...

Also, it is best to use `case` modifiers for strings such as `.lower()` or `.upper()` to better handle user input, regardless of what the user inputs.

For example, in some snippets of code you might see me do something like:
```py
my_string="westwardfishdme"
some_string="I LOVE ICE CREAM"

# make my_string all upper case
print(my_string.upper())
# make some_string all lower case
print(some_string.lower())

```

Using case modifiers makes handling boolean values all that much easier, because you don't have to worry if your user puts in some funky text, because your
program will automatically set it to either all `lowercase` or all `uppercase`.

# Control Flow
This section informs you on the control flow of python. Control flow is the process of handling
logic within functions to procedurally handle conditions where you wish to produce certain output
under certain conditions. It also dictates how your code is handled, and processed by your computer.

## Logic
Logic is the intricate details of booleans. Logic on computers is handled the same way you'll see on
most electronics and electric circuits. We can handle if statements using logic and booleans to build
our skills on control flow. 

### Logic gates
In python there are numerous keywords and special characters that you can use to 
handle logic within your code to replicate the logic gates seen within electrical
diagrams. 

If you have played Minecraft for any amount of time, and have used redstone to
build contraptions, it follows the same laws. Or if you have played around
with electrical circuit diagrams, you would also know these by heart.

These are the following boolean operators that perform logic gates and rules, 
I have also pointed out which one's you really need to know.
- `and` << 
- `or` << 
- `xor` <<
- `xnor`
- `not` << **this is also a keyword in python, but there is a special way we notate this. 
- `nand` 
- `nor`

## If-Elif Statements
If and Elif Statements are your bread and butter in mastering control flow.
These statements can **ONLY ACCEPT** boolean operations and expressions. 

Say you have a program that asks a user what is their favorite color, and
you have to design it such that your program checks whether or not they inputted
a specific value. Here would be an acceptable use for an `if/elif` statement:

For example, you might write code that looks like this:
```py
def check_color(color):
  # in the case, where I like blue but not as much as I do red...
  if color == "red":
    print("That's my favorite color too!")
  elif color == "blue":
    print("I guess thats an ok color, its not my favorite but I like it!")
  else:
    print("I guess we can have different opinions, but I don't like that color.")

def main():
  color=str(input("what is your favorite color?: "))
  # note that i add the .lower() to make sure the user's input is set to lowercase.
  check_color(color.lower()) 

main()
```
Sometimes, you want the output of that inner function to be something similar or performed
the exact same way. This is when we use **boolean operators.**

```py
# We don't want something like this:

def check_color(color):
  # say i like blue as much as red...
  if color == "red"
    print("I love the color red too!")
  elif color == "blue":
    print("I love the color blue too!")
  else:
    print("I guess we can have different opinions, but I don't like that color.")

def main():
  color=str(input("what is your favorite color?: "))
  check_color(color.lower()) 

main()
```
Another acceptable, and honestly a much more readable rewrite might look like this:
```py
def check_color(color):
  # say i like blue as much as red...
  if color == "red" or color == "blue":
    print(f"I love the color {color} too!")
  else:
    print("I guess we can have different opinions, but I don't like that color.")

def main():
  color=str(input("what is your favorite color?: "))
  check_color(color.lower()) 

main()
```
**Note:**

For statements where you use the keywords `or`, `and`, `is`, and `not` YOU
MUST format it such that you are comparing two or more separate complete
boolean expressions.

For example, you want to generally format it such that it looks like this:
```py
# WRITE IT LIKE THIS:
# you don't need to add the parentheses, but
# I included them because it makes it slightly
# more readable.

if (m==1) or (m==2):
  # do something...


# DO NOT WRITE EXPRESSIONS LIKE THIS, THIS WILL BE A LOGICAL BUG.
# Meaning that it will run, but "2" is a literal,
# meaning that it will always return true...

if m==1 or 2:
  #this will always run, regardless of the value of m.
```
## Match-Case Statements
Match-case statements are a more comprehensive form of If-Elif statements that does exactly as it sounds.
Sometimes when we are programming, we have to actually write code that takes an input and we have to
build based around the context of the user. Say you had to work on a project where there a ton of conditions
that need to be met for the variable `name` and you had to check if their name was either `jonathan, kyle, or miranda`.

Would you rather parse code that looks like this:
```py
if name=="jonathan":
  print(f"hello {name}, cool name!")
elif name=="kyle":
  print(f"hello {name}, do you drink monster energy by chance?")
elif name=="miranda":
  print(f"hello {name}, you share the same name as the iCarly actor!")
else:
  print(f"Oh, {name}. I don't know you!")
```
or code that looks like this:
```py
match name:
  case "jonathan":
    print(f"hello {name}, cool name!")
  case "kyle":
    print(f"hello {name}, do you drink monster energy by chance?")
  case "miranda": 
    print(f"hello {name}, you share the same name as the iCarly actor!")
  case _: # this is like our else statement,
    print(f"Oh, {name}. I don't know you!")
```
Typically in a software development environment, it is preferred to write logic based on match/case statements rather
than if/else statements **IF POSSIBLE.**

You won't always have the opportunity to use match/case statements, but if you HAVE to use an if statement,
try to use them as minimally of them as you possibly can.

# Iterators and Recursion
## For loops
If `if/elif` statements are your bread and butter for control flow, them `for` loops is your Swiss Army Knife in control flow operations. You can use them to do
repetitive tasks where you need to complete a specific **iteration**, or better yet, as I like to describe it: "a pattern of operations".

For example, say we need to write a function that tells us specifically to create a pattern of 10 hello's, but on the 7th hello, we print out a special message.

```py
# here specifically, i use the range modifier with a single argument/parameter 10.
for i in range(10):
  print("hello!")
  if i == 7:
    print("hello from iteration:",str(i))
```
This is a very basic form of a for loop, but essentially anything within the indentation of the for loop gets repeated procedurally.
Note: When you inevitably learn O notation ("Big O notation" as it's colloquially called) you'll learn when iterators are both detrimental,
necessary, and acceptable cases. Typically, you don't want to nest for loops as seen below:
```py
for i in range(30):
  for j in range(30):
    #do complex code things
    pass

```
For something like this it is best advised to consult all other possible ways to solve this as it can get very slow and messy fast--
This particular algorithm runs in `O(n^2)`. Thats because as you can guess we are calling the inner for loop `for j in range(30)`
every time we iterate through the outer loop `for i in range(30)` so as you can imagine this not only would hog up resources in its complex
calculations, but also be extremely inefficient. However, it is not always the case that we can escape something like this, but there are alternatives.

I can't list any specific examples at the moment, but you can find some on [leetcode](https://leetcode.com) if you want some more practice on O notation.
## While loops
Honestly, these are the same as for loops, but will iterate until the statement provided is false. For example:
```py
def main():
  i=30
  j=0
  while (i >= j):
    print(i+j) #would count from 30 to 60
```
you can use while loops the same as for loops, but you can never use a for loop the same as a while loop. It's like that square can be a rectangle 
argument "a square can be a rectangle, but a rectangle never a square".

Typically, when you're developing some software, you either declare initially what conditions will `break` the loop inside of the parameters.
```py
# for example:
while(x>y): 
  #do something...
  pass 
```
If you have multiple conditions that can break your loop, it is best practice to do a `while(True)` loop and then use either an `if/elif` statement
or better yet, use a `match/case` statement, for example:
```py

def main():
  while(True):
    print("If these conditions aren't met, I will run forever!")
    condition=str(input("What is your favorite pizza topping?: "))

    if condition == "": # if blank break the loop return to main()
      break

    match condition.lower:
      case "pepperoni":
        print("Love that topping!")
      case "cheese":
        print("That's pretty meh, but ok.")
      case _:
        print(f"Sorry, im not a big fan of {condition.lower()}")

  print("in main")

```

## Pass and Break Statements
Breaks and Pass statements are essentially just special keyword statements that allow you to do nothing in a control flow statement, or break out of a loop;

Breaks (`break`) are useful for breaking out of a `for` or `while` loop once a specific condition is met. `pass` statements literally do nothing, but just because
they do nothing, it is unwise to doubt the power of a `pass` statement.

Pass statements are **ESPECIALLY** useful when handling **errors**, or catching faulty logic. For example:

```py
def countfrom(x:int, y:int):
  return int(x+y) 
  # in normal python, there would just be a string concatenation, 
  # but since we specify that we are casting a string to an int,
  # this program will give a TypeError error, and crash out.

def main():
  try: # check out try/except statements, will be posted later.
    print("we sucessfully performed the function countfrom()")
    print(countfrom("we", 2))
  except TypeError:
    print("we hit an error: TypeError")
    pass 
    # the pass statement will just pretend like nothing happened.
    # and the program will continue. Had we not inserted this here, 
    # the program would just fail and crash.

  print("Main has completed.") #<< this line is now reachable.

main()
```

We can use `break` in a similar fashion, but we usually use in programming to
stop a loop when certain logical conditions are met. 

Generally speaking, use `pass` and `break` as liberally as possible, but use
them as tools specific to their best use application.

Ideally in situations where we want to break out of a function all together if something fails, we can also just call
`return`.

## Recursion
Now that you kind of understand how to use pass and break functions, you can use them in recursive functions.
Now the thing about recursive functions it is rather complicated, and honestly not that much different from iteratable
functions, but they are very different in terms of efficiency and performance. Generally speaking, recursive functions
can be useful in certain scenarios or for code reading, but keep in mind that you are calling a function numerous times
which causes an increase in memory use each time-- so be wary!

What is a recursive function? Pretty much a function that calls itself:

```py
# this is an example from wikipedia, which i suggest you check out.
def factorial(x):
  if x > 0:
    return n * factorial(x - 1)
  else:
    return 1
```
see how in the definition of the function, it calls itself? That's what recursion is.

Check out more from the wikipedia article [here](https://en.wikipedia.org/wiki/Recursion#In_computer_science)

To see more about recursive vs. iterative, [read this](https://edward-huang.com/2021/02/17/is-recursion-really-slower-than-iteration/)


# Error Handling

## Exit and Errors
As a new developer, you probably have already run into these. Reading errors is rather quite scary, BUT you can actually levy 
errors to your advantage. Take this example program as an example:

```py
def cause_error():
    this = "this"
    will = "will"
    fail = 3
    print(this, will+fail)


def main():
    print("hello world!")
    cause_error()



if __name__ == "__main__":
    main()
```
This will cause a `TypeError` error, as we are trying to concatenate the string `will` with the integer `fail`.

```
Traceback (most recent call last):
  File "/home/withoutdishonor/programming/high/python/141/COMP170-study-repository/fail.py", line 14, in <module>
    main()
    ~~~~^^
  File "/home/withoutdishonor/programming/high/python/141/COMP170-study-repository/fail.py", line 10, in main
    cause_error()
    ~~~~~~~~~~~^^
  File "/home/withoutdishonor/programming/high/python/141/COMP170-study-repository/fail.py", line 5, in cause_error
    print(this, will+fail)
                ~~~~^~~~~
>>TypeError: can only concatenate str (not "int") to str << # THIS IS WHAT WE NEED.
```
While this looks scary to an untrained eye, it's really not that all scary.
The format of python's errors, are rather easier to read in comparison to other languages, 
as the language is interpreted, it gives you a very accurate traceback of where our error occured.

Lets first breakdown the issue to this:

```
main(): line 14 had an error
|
|--->cause_error(): line 10 inside of main() is where the error occurs.
    | 
    |----------->print(this, will+fail): line _5_ experienced an error.
                                 ^
                                 |---- we tried to concatenate an integer with a string
                                       and because these are 2 different data types, we
                                       will experience an error because data types were
                                       not typecasted. (we fix this with str(fail))
```

Because this datatype error occurs, we actually get the error code from the interpreter:
`TypeError: can only concatenate str (not "int") to str` 

## Try, Except, and Finally statements

Now that we know how to read errors, we can actually write robust code called Try/Except statements.
In other languages, this might be called try/catch, or you might not have these at all. Most Object
Oriented Programming languages do, but you might have to search up how to mimic this functionality.

In C, you would have to manually catch these errors before compiling, and in Rust you could use the Result<T,E> return type, but
in python, they actually make error handling extremely simple with `try/except`

what does a `try/except` function do exactly? Well, lets use our code from earlier with `cause_error()`:

```py
def cause_error():
    this = "this"
    will = "will"
    fail = 3
    print(this, will+fail)


def main():
    print("hello world!")
    # let's use a try/except control block.
    try:
      cause_error()
    except TypeError:
      print("We had an error!: TypeError")
    finally:
      print("We got through our try/except block!")


if __name__ == "__main__":
    main()
```
To breakdown what's going on when we run our code:

1. Our program will `try` to run the function, `cause_error()`
when it does, it will faile because of the `TypeError` exception
that we saw occur.
2. We will then go to our `except` block, and then inform the user of the error.
3. No matter if `cause_error()` runs successfully, or if an exception is raised,
we will `finally` inform the user that we got through our try/except block.

We can actually make the `except` block more general and print out any type of error with:
```py
try:
  cause_error()
except Exception as error_code:
  print(f"We had an error!: {type(error_code).__name__}")
```
This will actually print out the error without us having to define the error in the `except` statement,
this way if we were to encounter any other error in our code, we will actually catch that error, and
print out what happened to the user. This way, if we were to fix our original error and came into contact
another error, we actually know what occurs.

If we want to get the exact line where it goes wrong, we would have to use `traceback` library:
```py
import traceback

try:
  cause_error()
except Exception as error_code:
  print(traceback.format_exc())
```
This will actually print out the same thing we see inside of the error without terminating our program.

It is very good to write your code like this, as if when you write code for future projects,
you want to make it as robust and fool-proof as possible. It's always best to apply Murphy's law
when making programs:

> "Anything that can go wrong, will go wrong."

# Classes
Python uses an extreme



# Imports and using libraries
Sometimes, you when writing code, you may want to break your code up into 
## Using python's built-in libraries
You can import any built-in libraries using their name respectively.
for example:
```py
import math;

```
this imports the math library, which is built into python.
To see a full list, see: 
[The Official Documentation for Python](https://docs.python.org/3/library/index.html)

## Using self-defined libraries
You can use seperate files or libraries that you made yourself by making an it a file, or in a seperate folder/directory.
For example, you may want to write code into modules that each holds functions that are related to a specific task or feature.

### Code Examples

In our first example, let's look at the following directory tree:
```
src/
|-[main.py]
|-[foo.py]
```
Inside our root directory, we have our `main.py` and `foo.py`, of which we can directly import `foo.py` 
```py

```

```py
# main.py
import foo
def main():
  foo.func()

```


#### Writing from other directories.
When writing it as a seperate directory, it acts as a seperate class, therefore you can do something like this:

```
src/
|-[main.py]
|-[my_lib]
     |----[__init__.py]
     |----[otherfile.py]
```

In the tree above, we have `main.py` in the main directory, and `my_lib` as a seperate directory. 

It is important to note that `__init__.py` inside of `my_lib` can ONLY see what is inside of the directory, and when importing files from within `my_lib`, you must declare that
the root directory is within `my_lib`. To do this, you use the `from . import x` when working in a subdirectory of your main project:
#### inside of my_lib/otherfile.py
```py
# inside mylib/otherfile
def bar():
  print("bar")

```
#### inside of my_lib/__init__.py

```py
# inside of my_lib/__init__.py
from . import otherfile

def foo():
  print("foo")

def foobar():
  foo()
  otherfile.bar()

```

#### main file:
```py
# inside main.py
import my_lib
def main():
  my_lib.foobar()
```

#### Output when running main.py:
```
foo
bar
```
## Example 2
In addition, we can call functions independently from inner files, for example:

```py
# inside main.py
import my_lib

def main():
  my_lib.foo()
  my_lib.foobar()
  my_lib.otherfile.bar()

```
### Output when running main.py:
```
foo
foo
bar
bar
```

## Using PIP and external python libraries.
If there is code outside of your project that you would like to use-- you can easily import them into your
project using python's package manager `pip`. You can install packages using the command-line with:

```
$ pip install somepackage
```

Note: this may work differently depending on which operating system you're on. Some python setups may be running on an externally managed environment,
which means that you have to install packages using an `env` based directory. To see more: [read the official documentation](https://packaging.python.org/en/latest/specifications/externally-managed-environments/)
