# Python

## Installation

### python
- Download and install the latest Python for your OS: https://www.python.org/downloads/
- pip install https://pip.pypa.io/en/stable/installation/

You can verify the successful installation (new or existing) by running the following commands either on Terminal, or Git Bash.
```terminal
python --version
pip --version

or 

python3 --version
pip3 --version
```

## String Methods
![image](images/string_methods.png)

## Split

1. A basic split method:
>```Python
> new_str = "The cow jumped over the moon."
> new_str.split()```
> 
> Output is: ['The', 'cow', 'jumped', 'over', 'the', 'moon.']
>```

2. Here  the separator is space, and the maxsplit argument is set to 3.
>```Python
> new_str.split(' ', 3) ```
> 
> Output is: ['The', 'cow', 'jumped', 'over the moon.']
>```

3. Using '.' or period as a separator.
>```Python
> new_str.split('.')```
> 
> Output is: ['The cow jumped over the moon', '']
>```

4. Using no separators but having a maxsplit argument of 3.
>```Python
> new_str.split(None, 3)```
> 
> Output is: ['The', 'cow', 'jumped', 'over the moon.']
>```

## Data Structure

- Mutable data types can be changed after they are created. e.g. list, dict, set
    + are passed into functions as a pointer to the original object.
    + changes that happen to this pointer within the function change the original object.
- Immutable data types can't be changed after they are created. e.g. bool, int, float, tuple, str
    + are passed into functions as a copy of the original object
    + changes that happen to this copy within the function don't affect the original object

>```python
> Data Structure    |   Ordered    |    Mutable |   Constructor     |   Example
> ------------------+--------------+------------+-------------------+-----------------------
>  List             |   Yes        |    YES     |   [ ] or list()   |   [5.7, 4, 'yes', 5.7]
>  Tuple            |   Yes        |    NO      |   ( ) or tuple()  |   (5.7, 4, 'yes', 5.7)
>  Set              |   NO         |    YES     |   {}* or set()    |   {5.7, 4, 'yes'}
>  Dictionary       |   NO         |    NO**    |   { } or dict()   |   {'Jun': 75, 'Jul': 89}
>```


### Lists and Membership Operators
>```Python
> months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
> print(months[0]) # January
> print(months[1]) # February
> print(months[7]) # August
> print(months[-1]) # December```
> print(months[25]) # IndexError: list index out of range
> 
> q3 = months[6:9]
> print(q3) # [ 'July', 'August', 'September']
> 
> first_half = months[:6]
> print(first_half) # ['January', 'February', 'March', 'April', 'May', 'June']
> 
> second_half = months[6:]
> print(second_half) # ['July', 'August', 'September', 'October', 'November', 'December']
> 
>```

### Are you `in` OR `not in`?
>```Python
> >>> 'this' in 'this is a string'
> True
> >>> 'in' in 'this is a string'
> True
> >>> 'isa' in 'this is a string'
> False
> >> 5 not in [1, 2, 3, 4, 6]
> True
> >>> 5 in [1, 2, 3, 4, 6]
> False
>```


### Tuples
A tuple is another useful container. It's a data type for immutable ordered sequences of elements. They are often used to store related pieces of information. Consider this example involving latitude and longitude:

>```Python
> location = (13.4125, 103.866667)
> print("Latitude:", location[0])
> print("Longitude:", location[1])
>```

Tuples are similar to lists in that they store an ordered collection of objects which can be accessed by their indices. Unlike lists, however, tuples are immutable - you can't add and remove items from tuples, or sort them in place.

Tuples can also be used to assign multiple variables in a compact way.
>```Python
> dimensions = 52, 40, 100
> length, width, height = dimensions
> print("The dimensions are {} x {} x {}".format(length, width, height))
>```

### Sets
A set is a data type for mutable unordered collections of unique elements. One application of a set is to quickly remove duplicates from a list.

>```Python
> numbers = [1, 2, 6, 3, 1, 1, 6]
> unique_nums = set(numbers)
> print(unique_nums)
> This would output: {1, 2, 3, 6}
> 
> fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
> print("watermelon" in fruit)  # False -- check for element 
> 
> fruit.add("watermelon")  # add an element
> print(fruit) # {'grapefruit', 'orange', 'watermelon', 'banana', 'apple'}
> 
> print(fruit.pop())  # grapefruit -- remove a random element
> print(fruit) # {'orange', 'watermelon', 'banana', 'apple'}
>```

### Dictionaries and Identity Operators
>```Python
> elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
> print("carbon" in elements)
> print(elements.get("dilithium"))
>```

## Lambda Expressions
You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

With a lambda expression, this function:

>```Python
> def multiply(x, y):
>     return x * y
> # can be reduced to:
> multiply = lambda x, y: x * y
>```

## Documentation
Documentation is used to make your code easier to understand and use. Functions are especially readable because they often use documentation strings, or docstrings. Docstrings are a type of comment used to explain the purpose of a function, and how it should be used. Here's a function for population density with a docstring.

>```Python
> def population_density(population, land_area):
>     """Calculate the population density of an area.
> 
>     INPUT:
>     population: int. The population of that area
>  
>     OUTPUT: 
>     population_density: population / land_area. The population density of a particular area.
>     """
>     return population / land_area
>```

## Reading and Writing Files

>```Python
> f = open('my_path/my_file.txt', 'r')
> file_data = f.read()
> f.close()
> 
> with open('my_path/my_file.txt', 'r') as f:
>     file_data = f.read()
> 
>
> def create_cast_list(filename):
>    cast_list = []
>    with open(filename) as f:
>        for line in f:
>            name = line.split(",")[0]
>            cast_list.append(name)
>
>    return cast_list
>
> cast_list = create_cast_list('flying_circus_cast.txt')
> 
> for actor in cast_list:
>    print(actor)
>
>```

## The Standard Library
https://pymotw.com/3/

## IPython
There is actually an awesome alternative to the default Python interactive interpreter, IPython, which comes with many additional features.

- tab completion
- ? for details about an object
- ! to execute system shell commands
- syntax highlighting!
and a lot more you can find here! https://ipython.org/ipython-doc/3/interactive/tutorial.html

## Inheritance

```python
class Clothing:
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

class Shirt(Clothing):
    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2*self.price

class Pants(Clothing):
    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)
```


# Anaconda/ Miniconda/ Pip
## What is Anaconda Distribution?
- Anaconda is a program to manage (install, upgrade, or uninstall) packages and environments to use with Python. It's simple to install packages with Anaconda and create virtual environments to work on multiple projects conveniently.

- Even if you already have Python installed, it will be beneficial to use Anaconda/Miniconda because:
    + Anaconda comes with a bunch of data science packages; you'll be all set to start working with data.
    + Using conda to manage your packages and environments will reduce future issues dealing with the various libraries you'll be using.
- `conda install PACKAGENAME`
- The `conda` and `pip` both are the Python package managers. Package managers are used to installing libraries and other software on your computer. pip is the default package manager for Python libraries, whereas conda focuses only on the packages that are available from the Anaconda distribution.

## Why do you need a Virtual Environment?
- Each virtual environment remains isolated from other virtual environments, and the default “system” environment. Environments allow you to separate and isolate the packages you are using for different projects. Often you’ll be working with code that depends on different versions of some library. For example, you could have code that uses new features in Numpy, or code that uses old features that have been removed. It’s practically impossible to have two versions of Numpy installed at once. Instead, you should make an environment for each version of Numpy then work in the appropriate environment for the project.

- This issue also happens a lot when dealing with Python 2 and Python 3. You might be working with old code that doesn’t run in Python 3 and new code that doesn’t run in Python 2. Having both installed can lead to a lot of confusion and bugs. It’s much better to have separate environments.

- You can also export the list of packages in an environment to a file, then include that file with your code. This allows other people to easily load all the dependencies for your code. Pip has similar functionality with `pip freeze > requirements.txt`

## Installing Anaconda
Anaconda is available for Windows, Mac OS X, and Linux. Follow the links below to get started:

- Download the installer from https://www.anaconda.com/download/. Choose the Python 3.6 or higher version, and the appropriate 64/32-bit installer. If you already have Python installed on your computer, this won't break anything. Instead, the default Python used by your scripts and programs will be the one that comes with Anaconda.
- Refer the installation instructions [here](https://docs.anaconda.com/free/anaconda/install/)
- Verify the installation [here](https://docs.anaconda.com/free/anaconda/install/verify-install/) for your respective OS

After installation, you’re automatically in the default conda environment with all packages installed which you can see below. You can check out your own install by entering the following command into your terminal.

`conda list`

## List of Applications Installed with Anaconda
As we read on the previous page, the following packages will get installed with Anaconda:

- **Anaconda Navigator** - a GUI for managing your environments and packages
- `conda` - a command-line utility
- **Python** - The latest version of Python gets installed as an individual package.
- **Anaconda Prompt** - [Only for Windows] a terminal where you can use the command-line interface to manage your environments and packages
- A bunch of applications, such as **Spyder**. It is an IDE geared toward scientific development. In total, over 160 scientific packages and their dependencies are also installed.
To avoid errors later, it's best to update all the packages in the default environment. Open the Terminal/ Anaconda Prompt application. In the prompt, run the following commands:

```Terminal
conda upgrade conda
conda upgrade --all
```

# References
- document: document: https://peps.python.org/pep-0008/

# Useful Third-Party Packages
- Being able to install and import third party libraries is useful, but to be an effective programmer you also need to know what libraries are available for you to use. People typically learn about useful new libraries from online recommendations or from colleagues. If you're a new Python programmer you may not have many colleagues, so to get you started here's a list of packages that are popular with engineers at Udacity.

- IPython - A better interactive Python interpreter https://ipython.org
- requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
- Flask - a lightweight framework for making web applications and APIs.
- Django - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
- Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping. https://www.crummy.com/software/BeautifulSoup/
- pytest - extends Python's builtin assertions and unittest module. https://docs.pytest.org/en/7.4.x/
- PyYAML - For reading and writing YAML files. https://pyyaml.org/wiki/PyYAML
- NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities. https://numpy.org
- pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes! https://pandas.pydata.org
- Matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments. https://matplotlib.org
- ggplot - Another 2D plotting library, based on R's ggplot2 library. https://pypi.org/project/ggplot/
- Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter. https://python-pillow.org
- pyglet - A cross-platform application framework intended for game development.  https://pyglet.org
- Pygame - A set of Python modules designed for writing games. https://www.pygame.org/news
- pytz - World Timezone Definitions for Python - https://pytz.sourceforge.net


