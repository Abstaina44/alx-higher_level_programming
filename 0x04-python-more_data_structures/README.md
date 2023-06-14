Squared simple mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that computes the square value of all integers of a matrix.
Prototype: def square_matrix_simple(matrix=[]): matrix is a 2 dimensional array Returns a new matrix: Same size as matrix Each value should be the square of the value of the input Initial matrix should not be modified You are not allowed to import any module You are allowed to use regular loops, map, etc.

Search and replace mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that replaces all occurrences of an element by another in a new list.
Prototype: def search_replace(my_list, search, replace): my_list is the initial list search is the element to replace in the list replace is the new element You are not allowed to import any module

Unique addition mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that adds all unique integers in a list (only once for each integer).
Prototype: def uniq_add(my_list=[]): You are not allowed to import any module

Present in both mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that returns a set of common elements in two sets.
Prototype: def common_elements(set_1, set_2): You are not allowed to import any module

Only differents mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that returns a set of all elements present in only one set.
Prototype: def only_diff_elements(set_1, set_2): You are not allowed to import any module

Number of keys mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that returns the number of keys in a dictionary.
Prototype: def number_keys(a_dictionary): You are not allowed to import any module

Print sorted dictionary mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that prints a dictionary by ordered keys.
Prototype: def print_sorted_dictionary(a_dictionary): You can assume that all keys are strings Keys should be sorted by alphabetic order Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary) Dictionary values can have any type You are not allowed to import any module

Update dictionary mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that replaces or adds key/value in a dictionary.
Prototype: def update_dictionary(a_dictionary, key, value): key argument will be always a string value argument will be any type If a key exists in the dictionary, the value will be replaced If a key doesn’t exist in the dictionary, it will be created You are not allowed to import any module

Simple delete by key mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that deletes a key in a dictionary.
Prototype: def simple_delete(a_dictionary, key=""): key argument will be always a string If a key doesn’t exist, the dictionary won’t change You are not allowed to import any module

Multiply by 2 mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that returns a new dictionary with all values multiplied by 2
Prototype: def multiply_by_2(a_dictionary): You can assume that all values are only integers Returns a new dictionary You are not allowed to import any module

Best score mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that returns a key with the biggest integer value.
Prototype: def best_score(a_dictionary): You can assume that all values are only integers If no score found, return None You can assume all students have a different score You are not allowed to import any module

Multiply by using map mandatory Score: 0.0% (Checks completed: 0.0%) Write a function that returns a list with all values multiplied by a number without using any loops.
Prototype: def multiply_list_map(my_list=[], number=0): Returns a new list: Same length as my_list Each value should be multiplied by number Initial list should not be modified You are not allowed to import any module You have to use map Your file should be max 3 lines

Roman to Integer mandatory Score: 0.0% (Checks completed: 0.0%) Technical interview preparation:
You are not allowed to google anything Whiteboard first Create a function def roman_to_int(roman_string): that converts a Roman numeral to an integer.

You can assume the number will be between 1 to 3999. def roman_to_int(roman_string) must return an integer If the roman_string is not a string or None, return 0

Weighted average! #advanced Score: 0.0% (Checks completed: 0.0%) Write a function that returns the weighted average of all integers tuple (, )
Prototype: def weight_average(my_list=[]): Returns 0 if the list is empty You are not allowed to import any module

Squared by using map #advanced Score: 0.0% (Checks completed: 0.0%) Write a function that computes the square value of all integers of a matrix using map
Prototype: def square_matrix_map(matrix=[]): matrix is a 2 dimensional array Returns a new matrix: Same size as matrix Each value should be the square of the value of the input Initial matrix should not be modified You are not allowed to import any module You have to use map You are not allowed to use for or while Your file should be max 3 lines

Delete by value #advanced Score: 0.0% (Checks completed: 0.0%) Write a function that deletes keys with a specific value in a dictionary.
Prototype: def complex_delete(a_dictionary, value): If the value doesn’t exist, the dictionary won’t change All keys having the searched value have to be deleted You are not allowed to import any module

CPython #1: PyBytesObject #advanced Score: 0.0% (Checks completed: 0.0%) Create two C functions that print some basic info about Python lists and Python bytes objects.
Python lists:

Prototype: void print_python_list(PyObject *p); Format: see example Python bytes:

Prototype: void print_python_bytes(PyObject *p); Format: see example Line “first X bytes”: print a maximum of 10 bytes If p is not a valid PyBytesObject, print an error message (see example) Read /usr/include/python3.4/bytesobject.h About:

Python version: 3.4 Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,libPython.so -o libPython.so -fPIC -I/usr/include/python3.4 103-python.c You are not allowed to use the following macros/functions: Py_SIZE Py_TYPE PyList_GetItem PyBytes_AS_STRING PyBytes_GET_SIZE
