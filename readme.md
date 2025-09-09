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
- Although I have worked with python before in my youth, and it's been years since I've used the language but I still have
a lot of experience in both writing it and reading it. 

Don't let that last point fool you! Once you master how to view patterns in programming languages, 
you can see how knowledge overlaps between languages. The truth is, you can use any language to write
any program. A developer's choice in programming language is either by design or preference, and sometimes these reasons can overlap!

You can see an example of that in this [video of a guy writing a whole webserver in bash.](https://www.youtube.com/watch?v=L967hYylZuc)

If you feel like the video is too advanced, or too long, feel free to not watch it BUT I recommend you at least read my explanation of why that video matters here:

Bash is not typically used to write such advanced software as the guy in the video was making, i.e. a webserver that can host a website, BUT he managed to not only make it work,
but eloquently wrote it all in bash, without any the use of any other languages. There are some segements where he implies that there might be module that needs an implementation in C,
but nonetheless, he omits that from his final project, and accomplished an extraordinary task that I recently didn't even know was possible until he did it and mentioned other projects
that accomplished the same thing.

The reason why I say this and mention this video at all is because this course is not designed to just teach you python, but to teach you the skills necessary to become a decent enough
programmer to create and problem solve. Great programmers like the guy in that video, Dennis Ritchie, Grace Hopper, or Steve Wozniak didn't just become magically good at programming,
they became great programmers because they practiced and learned how to solve difficult problems using **pattern based thinking.**


Needless to say, I am relatively 'advanced' in the field, but like y'all I am still learning.

### Why I made this, how you should use it, and covering past assignments.
I was inspired to make this repository because someone in class asked if I could synthesize a list of youtube videos for them 
to watch to learn how to program. On my train ride home, I thought to myself:

"Damn, I can literally write an actual study guide for the whole class if I really wanted to..."

and so I did, it's the one you're reading it now ;)

Most information will be passed along in this single readme, but I might change that. 
This repository is going to be less complicated than the textbook, and not depending on the severity more or less in depth,
on certain topics, but I will try and make it as digestible as possible. 

Since I am a full time student however, and I cannot fully invest all of my time into synthesizing 
all information properly, feel free to send a pull request or send an issue and I will look through
to publish any contributions made to this little pet project.

Additionally, I will only do what is taught already in class. That is if I hadn't already gotten ahead of myself in some sections, 
but I tried to leave some resources linked for you to read upon if you're interested.  

You should try and use this as any other study guide, or as a comprehension of the textbook. 
I also included some bonus information and some good practices for you to look at with some examples.
Inside of the example folder I also included a really easy to digest comprehensive python project that
I wrote with numerous comments to help understand what is happening, what interacts with what, and so on so forth.

With that said, I hope this guide serves you well, and you find this easy to learn!

## Miscellaneous Videos and Other Learning Resources
Here are some other resources you should check out to help study and learn, these aren't necessary, but if you
are truly interested in programming, these are some books that I had read and videos 

**LEARNING HOW TO PROGRAM IN PYTHON, AND HOW TO THINK LIKE A PROGRAMMER**
- [Fireship's wonderful video on how you should learn how to code](https://www.youtube.com/watch?v=NtfbWkxJTHw)
- [NetworkChuck's playlist on coding in python](https://www.youtube.com/watch?v=mRMmlo_Uqcs&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp)
- [Coding is easy, actually](https://www.youtube.com/watch?v=qkFYqY3vr84)
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
However, unlike most languages, it does not require them, which is will be a muscle memory issue when you learn more languages.

You can use semicolons to do something on a single line, but note that this is not really done in python, and does
reduce the readability of your code:
```py
print("This sentence was too long for me");print("so i used a semicolon for another print statement.")
```
Syntax also include indentation, missing functions, etc.

Indentation is the most important, as it dictates the control flow of functions, loops, if statements, and match/case
statements (also something we haven't covered yet, but it's like a special `if/then` statement, i'll explain later.) 

## Basic-Types
So far in class, we have covered the following data types:
- int (integers; like 1, 2, 3, 4 ...) 
- float (floating point numbers; 1.4, 4.29 3.39)
- string (line of text, but try to think of it as an **array of characters**; "hello world" -> `['h','e','l','l','o',' ','w','o','r','l','d']`)
- boolean (boolean algebra; True, False statements)

I won't go over all of the intricacies but types are **very important.**

When writing a program, knowing the types is the difference between your program succeeding, and failing
to run. In other cases, using improper types can cause undesired output, or even crashes.

Strings are the easiest and more common types we start with because it's the easiest to understand.
Also: **Arrays**, we haven't covered this *yet*, but think of arrays as a **container** of data, with indexes pointing
to different data types. In python it's called a **list**, and **arrays** are something different. So in an effort
not to confuse you:

"Arrays" in other languages are lists which look like this in python:
```py
my_list=[1,2,3,4,5,6]

```
In python, we do have specific arrays which can be invoked with:
```py
import array as arr
# we haven't learned any of this yet, so i won't say any more, but they function *similarly* to how they do in other languages.
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
will print out:
```
hello! hello! hello! hello! 

```
For some of the homework problems, you can actually use that to solve some of the problems, i.e. the rocket ships.
While I have to check with Dr.Ennaoui to see if it's ok to share answers to past homework problems, I really wish I could show
you how I solved that and retroactively add my pseudocode to explain what exactly I was thinking when I analyzed that problem.

## Functions

I will also cover variables in this section, so this is gonna be a doozy.

Functions are blocks of code in a function that either are called numerous times within your code OR added to help make your code more readable.
It is best to try to reduce the amount of code you repeatedly write when programming because this code is easier to maintain and much easier to
read overall. Here are some easy do's and don'ts when writing functions:
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
#### Proper naming
Functions and variables cannot start with certain keywords, characters, or generally numbers, this section will cover that.
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

while you can use types as function names, it is generally not recommended as it messes with the actual data type and can redefine functionality.
unless you are doing this for a very specific reason, it's best practice to not do that.

```py
def int(): # DONT DO THIS!!!
  pass # oooooh another secret keyword!
``` 

