---
marp: true
theme: default
class: default
size: 16:9
paginate: true
header: 國立陽明交通大學 電子與光子學士學位學程
headingDivider: 1
style: |
  section::after {
    content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .small-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .small-grid img {
    width: 50%;
  }
  .middle-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .middle-grid img {
    width: 75%;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
  }
  .grid img {
    width: 100%;
  }
  .red-text {
    color: red;
  }
  
  .blue-text {
    color: LightSkyBlue;  
  }

  .small-text {
    font-size: 0.75rem;
  }
---
# What is a Array
- Array is a data structure consisting of a collection of elements, of same memory size, each identified by an index. 
- Memory address of an element can be computed by 
  [array_start_address] + ([size] * [index])
- Static Arrays, Sorted Arrays, Dynamic Arrays

![bg right:40% w:500 array memory](../Lecture-Data-Structure/files/image/array_memory_address.png)

# Arrays
- Key characteristics
  - It stores a collection of data
  - Its elements can be accessed by index
  - Elements don’t have to be accessed sequentially
- Implementing arrays as a core language feature
  - Arrays are allocated in memory with sequential locations.
  - Arrays are restricted to storing data of the same type.
  - <span class="blue-text">Static Arrays: </span> The size of arrays (# of elements) must be decided when the array is created, and that size can’t be changed.

# Arrays in Python

Class          |Fixed Size|Fixed Type|Implementation
---------------|----------|-----------------|--------------
**list**       |NO    |NO               |not exactly an array
**array.array**|NO    |YES              |dynamic array
**Numpy.array**|YES   |YES              |static array

[Code: array-like in Python](../Lecture-Data-Structure/code/ch02a_python_array_like.py)

# Implement Arrays as a Core Language Feature
  - allocated in continuous memory
  - restricted to storing data of the same type
  - size of arrays must be decided when the array is created

# The core array class will have the following methods:
  - Initialize: create an array with a given size and type
  - Get the value at a given index
  - Get the number of elements in the array
  - Display the array

[Code: core array](../Lecture-Data-Structure/code/ch02b_core_array.py)

# Magic Method
![bg right:70% w:60%](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff69d1d4d-91ac-409a-baa2-ccd4c4aaab13_1700x2087.png)

# \_\_str\_\_() vs \_\_repr\_\_()
Method | Purpose | When Used?
-------|---------|-----------
\_\_str\_\_()|Readable, user-friendly representation|print(obj), str(obj)
\_\_repr\_\_()|Developer-friendly, unambiguous representation (often used for debugging)| repr(obj), or print(obj) if \_\_str\_\_() is missing


# Lab
(1) Create a package structure
my_package/
|---- \_\_init\_\_.py
|---- arrays/
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---- \_\_init\_\_.py
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---- core.py
|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|---- sorted_array.py
|---- queues/

(2) Write a main program to import core.py and use class Array to create an array object (codetype = l, size = 5), then store 4 integers
