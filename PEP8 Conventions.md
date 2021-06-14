##### Table of Contents  
[Naming](#Namings)  

### Namings
```
Class name : All Upercase with No seperator e.g MyModel
Constants: All UperCase with _seperator e.g MY_CONSTANT
functions, variables, Methods, Module : lowercase with _seperator e.g my_function()
packages: lowercase with no sepeartor e.g mypackage
```

### spaces
```
Vertical spaces : 2 blank line between different classes and functions
                  1 blank line when you want to seperate different parts of codes to show clear steps
                  1 blank line : Method defintion inside classes
Horizontal: Maximum line length: 79 charachter

Indentation: Use 4 spaces , prefare spaces over tabs
```

### extended lines
```sh
1. withouth equal sign:
def function(a,b
             c,d):
    return a+b+c+d
    
2. with equal sign:
var = function(
              a,b,
              c,d)
    
3. Closing Brace
list_of_students = [
                 1,2,3,
                 4,5,6,
                 7,8,9
                 ]
```
            
### comments
```sh
DocString (PEP257)
1. one line: ''' solve problem of ... '''
2. more han one line: ''' solve problem of ...
                      when there is a ...
                      '''
```
### data hiding
```
single underscore :  _hiddenvariable, it is a conventioon and does not stop external code from accessing them
doucle underscore: __private_method or variable, it can be accessed externally only with _ClassName__private_method
```

