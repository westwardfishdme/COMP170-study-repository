# Westwardfishdme's Guide to succeeding to COMP141

Welcome! My name is Jonathan. I am an open source dev, with a lot of free time 
on my hands so I came up with this idea to create a github repository for 
students learning Python. Whether this is your introduction to programming,
or if you want to become a hobby developer like me, this class will be 
extremely influential in your journey as a developer, and will hopefully bring concepts
to light. I'm going to try and also create videos for each weeks topic; At the time of
writing this we are on week 3, and just covered `data types` in Python today.

Most information will be passed along in this readme, but I will try and include some examples
of the code inside of the examples folder. This repository is going to be less complicated than
the textbook, and ergo less in depth, but I will try and make it as digestible as possible. 

Since I am a full time student however, and I cannot fully invest all of my time into synthesizing 
all information properly, feel free to send a pull request or send an issue and I will look through
to publish any contributions made to this little pet project.

With that said, I hope this guide serves you well, and you find this easy to learn!

## Content
- [The `print()` function](#print)
- [Proper syntax](#syntax)
- [Types](#basic-types)
- [Functions](#functions)

### Print 
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

### Syntax
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

### Basic-Types
So far in class, we have covered the following data types:
- int (integers; like 1, 2, 3, 4 ...) 
- float (floating point numbers; 1.4, 4.29 3.39)
- string (line of text, but try to think of it as an **array of characters**; "hello world" -> `['h','e','l','l','o',' ','w','o','r','l','d']`)
- boolean (boolean algebra; True, False statements)

I won't go over all of the intricacies but types are **very important.**

When writing a program, knowing the types is the difference between your program succeeding, and failing
to run. In other cases, using improper types can cause undesired output, or even crashes.

Strings are the easiest and more common types we start with because it's the easiest to understand.
Also: Arrays, we haven't covered this yet, but think of arrays as a **container** of data, with indexes pointing
to different data types. 

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

### Functions 

#### Proper naming
Functions and variables cannot start with certain keywords, characters, or generally numbers, this section will cover that.
##### Improper names!
Python is a very 
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


