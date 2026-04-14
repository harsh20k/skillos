---
creation date: 2024-12-15 14:44
modification date: Sunday 15th December 2024 14:44:55
tags:
  - slipbox/permaNotes/DalhousieInterview
description: 
source: https://docs.google.com/document/d/1f02mQTcQ7OVSi93vDUM9P65qulp_eQXixoTTYFqqKiY/edit?usp=drivesdk
dg-publish: true
---
```table-of-contents
title: 
style: nestedList # TOC style (nestedList|nestedOrderedList|inlineFirstLevel)
minLevel: 0 # Include headings from the specified level
maxLevel: 0 # Include headings up to the specified level
includeLinks: true # Make headings clickable
hideWhenEmpty: false # Hide TOC if no headings are found
debugInConsole: false # Print debug info in Obsidian console
```
# [[SOP Dalhousie|SOP]] reading projects /JAVA/ STAR Technique/ read their document

# Source
[[Dal.ca MACs]]

# Code
- [x] **Code**: [[Longest common Substring]], Find the largest common substring from array of strings,
- [x] **Code**: [[All Possible Permutations of String]], Code to find all permutations of given strings "exam" and "new"
- [x] Frequency count of words, Frequency count of a given name in the array, Frequency of character[[Frequency of Character]]
- [x] **Code**: [[Longest common Substring]] ,
- [x] Safe lock - 4-digit password unlock **code** => open a safe lock which should only open to code “4916”. Print “access denied” or “granted” accordingly
- [x] **Code**: [[Flight Booking System]] -  2 person need to get random flight (4 strings given) again after flight need to select seat randomly ( 3 strings in all flights), That 2 person also should be selected randomly
- [x] **Code**: [[Frequency of Character]],count frequency of character from given array 
- [x] **Code** for finding Number of [[Unique Characters In A String]]
- [ ] **Code** - transposition cipher
- [ ] **Code** - Longest common subsequence

---
# Pseudocode

- [x] **Pseudocode**: [[Sorting Algorithms|sorting]] (Pencil example),Best [[Sorting Algorithms]] algo ( write algo),Sort
- [x] **Pseudocode** for [[Quick Sort|quicksort]]
- [ ] **Pseudocode** -doors and windows
- [x] **Pseudocode** to reverse array of strings,Pseudo code to reverse all strings in a string array
- [x] **Pseudocode** Finding a string in array of strings, 
- [x] **Pseudocode** for Finding vowels in the list of strings

---
# Debugging
- **Debugging**: allEvenIntegers, Even odd program for debug, Even debugging,Odd/even debug
- **Debugging**: Factorial debugging, The last one was factorial debugging
- **Debugging**: Odd numbers from Array of Integer, Debug: Even numbers from Array of Integer, Debug: Odd-Even numbers,  Even number debugging, Even debugging,odd even debug, Debugging: if int array  contains all odd integers return true else false
- **Debugging**: Fibonacci
- **Debugging**: gcd of 2 numbers 13, 78
- **Debugging**: of Factorial Program, Debugging-factorial, Factorial program debugging
- **Debugging**: program to output only odd numbers, Debugging: finding only even integers
- **Debugging**: for fibonacci
- **Debugging**: GCD of 2 numbers, Debug: GCD of 2 numbers
- **Debugging**: Odd numbers from Array of Integer
- **Debugging**: Even numbers from Array of Integer
- **Debugging**: Odd-Even numbers
- **Debugging**: Fibonacci,Fibonacci for debugging
- **Debugging**: the code for finding the factorial of an inputted number
---
### Questions
- What is [[Inheritance|inheritance]], and other [[OOPS]] concepts
- [[Inheritance#Types of Inheritance|Types of inheritance]]
- [[Normalisation]]

- Introduction, Introduce Yourself, Tell me abt yurself
- [[Compiler vs Interpreter|Compiler vs. Interpreter]] 
- Is java compiler or interpreter based

	ANS - Interpreter translates just one statement of the program at a time into machine code which makes it overall slower in terms of execution speed compared to a compiler which…
	Compiler scans the entire program and translates the whole of it into machine code at once


- [[Pointer - address of location in memory]]
- [[Sliding Window Protocol|sliding window protocol]](used in TCP),
- What is [[Low Level Language]]?
- [[New keyword in Java|Usage of "new" keyword]]
- Difference between [[Final vs Finally in Java|final and finally]]
- ***Why [[Why strings are immutable|strings are immutable?]]***
- [[Threads#**Threads - Different Ways to Use It in Java**|Thread - Different ways to use it]]
- [[Call by Reference vs Call by Variable]], 
- What is [[Wrapper Class|wrapper class]], 
- What happens if there is no main method in the code?

- What are some popular DBMS? What is [[SQL]]?
- mysql
- postgresql
- mongodb
- oracle
- ms sql server

- Command to display a particular row of a table in [[SQL]].
- Use of where or like statement to filter out

- Dynamic allocation of the memory returning a reference variable to it.
- [[Compiler vs Interpreter|Compiler vs Interpreter]],
	- Compiler = converts the highlevel code into machine level code

- [[Final vs Finally in Java]], Final vs Finally in Java
	Final - variables cannot be modified - remain constant. If we initialize a variable with the final keyword, then we cannot modify its value. If we declare a method as final, then it cannot be overridden by any subclasses.
	Finally defines a block of code we use along with the try keyword. It defines code that's always run after the try and any catch block, before the method is completed. The finally block executes regardless of whether an exception is thrown or caught.

- [[Why strings are immutable]] 
	- safety concerns - database connections (hacker can easily manipulate) 

- What is [[Web socket]]
	It is bidirectional and a stateful protocol, which means the connection between client and server will keep alive until it is terminated by either party (client or server). After closing the connection by either of the client and server, the connection is terminated from both ends. 

- What is [[Inheritance]] in java
	Subclass can use the public methods from the base class, it can inherit the qualities of the parent class. 
	- Types = Single, hybrid, multilevel, multiple

- What are [[Threads]] and [[Type of Threads|types of it ]]

	- Basic unit of cpu utilization 
	
	- User level [[Threads]] + kernel level [[Threads]]
	they are not created using the system calls. Thread switching does not need to call OS and to cause interrupt to Kernel. Kernel doesn’t know about the user level thread and manages them as if they were single-threaded processes.
	Kernel knows and manages the [[Threads]]. Instead of thread table in each process, the kernel itself has thread table (a master one) that keeps track of all the [[Threads]] in the system. In addition kernel also maintains the traditional process table to keep track of the processes

- Explain [[Safe Lock in java]]

- What is [[Low Level Language]]
	Low-level languages are languages that sit close to the computer's instruction set . An instruction set is the set of instructions that the processor understands. Two types of low-level language are: machine code. assembly language

- What are the [[Advantages of Constructor]]?
	Automatic initialization of objects at the time of their declaration.
	Multiple ways to initialize objects according to the number of arguments passes while declaration.
	The objects of child class can be initialized by the constructors of base class.


- What are the [[Protected Keywords in JAVA]]?
	- Inside the same class in which it is declared.
	- From other classes which are also in the same package as the declared class.
	- Classes inherited from the declared one, irrespective of their package.

- What is a [[Wrapper Class]]? 
	- converts primitive data type to objects

- What is a [[Singleton Class]]? - allows only single object for the class

- [[Race Conditions|Race condition]]
- [[Deadlock]] in dbms
- [[Database Deadlock]]

- [[Cloud computing#Disadvantages of Cloud Computing|Disadvantage of cloud computing]],Cloud computing,

- [[Normalisation]] 1NF 2NF 3NF,
- [[Polymorphism]],
- [[Operator overloading]],

- Explain your views towards cyber Security

- Is Having more RAM always an efficient scenario??

- What is [[Database Deadlock]]?

- Explain “[[New keyword in Java|New” keyword in java]]?

