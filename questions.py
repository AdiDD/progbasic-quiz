questions = [
            [
                "Which of the following objects are unordered?",
                "\nA. Lists",
                "\nB. Strings",
                "\nC. Sets",
                "\nD. Tuples",
                "C"
            ],
            [
                "What is the difference between a list and a set?",
                "\nA. A list allows duplicate values and a set does not.",
                "\nB. A set allows duplicate values and a list does not.",
                "\nC. List allow duplicate values and are ordered whereas sets are unordered and do not allow duplicate values.",
                "\nD. There are no differences",
                "C"
            ],
            [
                "Which of the following is not a list method?",
                "\nA. add()",
                "\nB. append()",
                "\nC. clear()",
                "\nD. pop()",
                "A"
            ],
            [
                "What does the sort() method called on a set returns?",
                "\nA. Returns the sorted set",
                "\nB. Dosen't return anything because it is an in-place sort",
                "\nC. Raises AttributeError",
                "\nD. Returns the set unordered",
                "C"
            ],
            [
                "What is 'Stack Overflow'?",
                "\nA. It is a website",
                "\nB. It is exceeding the amount of memory alocated to a program",
                "\nC. It is a term used when you have over 10 stack frames in the call stack",
                "\nD. A case could be made that it is all of the above, depending on the context",
                "B"
            ],
            [
                "How do you access a specific value from a dictionary?",
                "\nA. my_dictionary['my_key']",
                "\nB. my_dictionary[my_key]",
                "\nC. my_dictionary.getvalue('my_key')",
                "\nD. Both A and C are correct",
                "A"
            ],
            [
                "What does it mean that an object is immutable in Python?",
                "\nA. It means that you can not call any methods on that object",
                "\nB. Means that the object's state can not be altered after it's been created.",
                "\nC. It means that the object is not iterable",
                "\nD. It means that the object is a string",
                "B"
            ],
            [
                "What type of elements a list can NOT contain in Python?",
                "\nA. Lists",
                "\nB. Booleans",
                "\nC. Dictionaries",
                "\nD. It can contain all of the above",
                "D"
            ],
            [
                "What does the slice operator [a:b] returns?",
                "\nA. Returns the elements between a and b (a and b not included)",
                "\nB. Returns the elements from a to b not including a",
                "\nC. Returns the elements from a up to but not including b",
                "\nD. Returns the elements from a to b, both a and b included",
                "C"
            ],
            [
                "Which of the following statements is true of Python dictionaries:",
                "\nA. Dictionaries are mutable.",
                "\nB. Items are accessed by their position in a dictionary.",
                "\nC. A dictionary can contain any object type except another dictionary.",
                "\nD. All the keys in a dictionary must be of the same type.",
                "A"
            ],
            [
                "Given the dictionary d = {'a' : 100, 'b': 200, 'c': 300}, which of the following will remove the entry in the dictionary for key 'c'?",
                "\nA. d.popitem(2)",
                "\nB. del d['c']",
                "\nC. d.remove('c')",
                "\nD. All of the above wil remove the entry 'baz' from the dictionary",
                "B"
            ],
            [
                "Given the dictionary d = {1: 100, 2: 200, 3: 300}, what is the result of d[1:3]?",
                "\nA. 200 300",
                "\nB. It raises an exception",
                "\nC. [200, 300]",
                "\nD. (200, 300)",
                "B"
            ],
            [
                "Which of the following could be a valid dictionary key:",
                "\nA. 'x'",
                "\nB. len",
                "\nC. ('1', '2')",
                "\nD. All of the above",
                "D"
            ],
            [
                "Given the dictionary d = {'a': 100, 'b': 200, 'c': 300}, what method call will delete the entry whose value is 200?",
                "\nA. del d['b']",
                "\nB. d.pop('b')",
                "\nC. d.popitem()",
                "\nD. All of the above",
                "B"
            ],
            [
                "Suppose you have a dictionary d1. Which of the following does NOT creates a variable d2 which contains a copy of d1:",
                "\nA. d2 = d1",
                "\nB. d2 = dict(d1)",
                "\nC. d2 = dict(d1.items())",
                "\nD. d2 = {} \n   d2.update(d1)",
                "A"
            ],
            [
                "The Python interpreter takes the code that you write and converts it to the language that the computer’s hardware understands.\nIs this statement true or false?",
                "\nA. True",
                "\nB. False",
                "",
                "",
                "A"
            ],
            [
                "Which one of the following if statements will NOT execute successfully?\n",
                "\nA. if(1,2): \n\tprint('True')",
                "\nB. if(1,2): print('True')",
                "\nC. if(1,2):\n\t\t print('True')",
                "\nD. All of the above will execute successfully",
                "D"
            ],
            [
                "What signifies the end of a statement block or suite in Python?",
                "\nA. A colon",
                "\nB. A line that is indented less than the previous line",
                "\nC. end",
                "\nD. }",
                "B"
            ],
            [
                "What is value of this expression:\n\n'a' + 'x' if '123'.isdigit() else 'y' + 'b'",
                "\nA. ax",
                "\nB. ab",
                "\nC. axb",
                "\nD. axyb",
                "A"
            ],
            # 19
            [
                "What would be the output of the following code snippet?\n\n\na_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}\nfor key in a_dict:\n\tprint(key)",
                "\nA. 'color'\n   'fruit'\n   'pet'" ,
                "\nB. color\n   fruit\n   pet",
                "\nC. blue\n   apple\n   dog",
                "\nD. 'blue'\n   'apple'\n   'dog'",
                "B"
            ],
            [
                "What would be the output of the following code snippet?\n\na_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}\nd_items = a_dict.items()\nprint(d_items)",
                "\nA. dict_items([('color'), ('fruit'), ('pet')])",
                "\nB. dict_items([('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')])",
                "\nC. ('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')",
                "\nD. [('color', 'blue'), ('fruit', 'apple'), ('pet', 'dog')]",
                "B"
            ],
            # 21
            [
                "Consider the following code snippet:\n\nprices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}\nfor key in prices.keys():\n\tif key == 'orange':\n\t\tdel prices[key]\n\nWhat would be the console output of this program?\n",
                "\nA. apple\n   orange\n   banana",
                "\nB. RuntimeError: dictionary changed size during iteration",
                "\nC. None",
                "\nD. There will be no output",
                "B"
            ],
            [
                "Which of the following statements are true of Python lists?",
                "\nA. ['a', 'b', 'c'] == ['c', 'a', 'b']",
                "\nB. All elements in a list must be of the same type",
                "\nC. A given object may appear in a list more than once",
                "\nD. All of the above",
                "C"
            ],
            [
                "List a is defined as follows:\n\na = [1, 2, 3, 4, 5]\n\nSelect the following statement that does NOT remove the middle element 3 from a so that it equals [1, 2, 4, 5]:\n",
                "\nA. a[2:3] = []",
                "\nB. a.remove(3)",
                "\nC. del a[2]",
                "\nD. a[2] = []",
                "D"
            ],
            [
                "List a is defined as follows:\n\na = ['a', 'b', 'c']\n\nWhich of the following statement does NOT add 'd' and 'e' to the end of a, so that it then equals ['a', 'b', 'c', 'd', 'e']:\n",
                "\nA. a.append(['d', 'e'])",
                "\nB. a += ['d', 'e']",
                "\nC. a[len(a):] = ['d', 'e']",
                "\nD. a.extend(['d', 'e'])",
                "A"
            ],
            # 25
            [
                "Suppose you have the following tuple definition:\n\nt = ('foo', 'bar', 'baz')\n\nWhich of the following statements replaces the second element ('bar') with the string 'qux':\n",
                "\nA. t[1:1] = 'qux'",
                "\nB. t[1] = 'qux'",
                "\nC. t(1) = 'qux'",
                "\nD. None of the above",
                "D"
            ],
            [
                "t = ('foo',) creates a tuple with a single element 'foo' that is assigned to variable t",
                "\nA. True",
                "\nB. False",
                "",
                "",
                "A"
            ],
            [
                "Consider this assignment statement:\n\na, b, c = (1, 2, 3, 4, 5, 6, 7, 8, 9)[1::3]\n\nFollowing execution of this statement, what is the value of b:\n",
                "\nA. 5",
                "\nB. 2",
                "\nC. 6",
                "\nD. 4",
                "A"
            ],
            [
                "Assume x and y are assigned as follows:\nx = 5\ny = -5\nWhat is the effect of this statement:\nx, y = (y, x)[::-1]\n",
                "\nA. The values of x and y are unchanged",
                "\nB. Both x and y are 5",
                "\nC. The values of x and y are swapped",
                "\nD. Both x and y are -5",
                "A"
            ],
            [
                "Which of the following is truthy:",
                "\nA. 0",
                "\nB. False",
                "\nC. 'None'",
                "\nD. None of the above",
                "C"
            ],
            [
                "Suppose the following statements are executed:\n\na = 100\nb = 200\n\nWhat is the value of the expression (a and b)?\n",
                "\nA. 100",
                "\nB. 200",
                "\nC. True",
                "\nD. False",
                "B"
            ],
            [
                "Which of the following does NOT define the set {'a', 'b', 'c'}:",
                "\nA. s = set('abc')",
                "\nB. s = set(['a', 'b', 'c'])",
                "\nC. s = {'a', 'b', 'c'}",
                "\nD. s = set('a', 'b', 'c')",
                "D"
            ],
            [
                "s = 'foo'\nt = 'bar'\nprint('barf' in 2 * (s + t))\n\nWhat is the output of the print() function call?\n",
                "\nA. True",
                "\nB. False",
                "",
                "",
                "A"
            ],
            [
                "What is the result of this statement?\n\nprint(ord('foo'))",
                "\nA. 102 111 111",
                "\nB. 102",
                "\nC. 324",
                "\nD. It raises an exception",
                "D"
            ],
            [
                "s = 'foo-bar-baz'\n\nWhich of the following expressions evaluates to a string equal to s:\n",
                "\nA. s.upper().lower()",
                "\nB. '-'.join(s.split('-'))",
                "\nC. s.strip('-')",
                "\nD. All of the above",
                "D"
            ],
            [
                "In Python, a variable must be declared before it is assigned a value:",
                "\nA. True",
                "\nB. False",
                "",
                "",
                "B"
            ],
            [
                "In Python, a variable may be assigned a value of one type, and then later assigned a value of a different type:",
                "\nA. True",
                "\nB. False",
                "",
                "",
                "A"
            ]
            ]
