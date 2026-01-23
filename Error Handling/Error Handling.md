# Error Handling Review

## Common Errors in Python

### SyntaxError

The error Python raises when your code does not follow its syntax rules. For example, the code print("Hello there" will lead to a syntax error with the message, SyntaxError: '(' was never closed, because the code is missing a closing parenthesis.

### NameError

Python raises a NameError when you try to access a variable or function you have not defined. For instance, if you have the line print(username) in your code without having a username variable defined first, you will get a name error with the message NameError: name 'username' is not defined.

### TypeError

This is the error Python throws when you perform an operation on two or more incompatible data types. For example, if you try to add a string to a number, you'll get the error TypeError: can only concatenate str (not "int") to str.

### IndexError

You'll get an IndexError if you access an index that does not exist in a list or other sequences like tuple and string. For example, in a Hello world string, the index of the last character is 11. If you go ahead and access a character this way, greet = "hello world"; print(greet[12]), you'll get an error with the message IndexError: string index out of range.
AttributeError: Python raises this error when you try to use a method or property that does not exist in an object of that type. For example, calling .append() on a string like "hello".append("!") will lead to an error with the message AttributeError: 'str' object has no attribute 'append'.
