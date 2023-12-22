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

## Managing Environments
As you saw on the previous page, conda can be used to create environments to isolate your projects. To create an environment, use the following command in your Terminal/Anaconda Prompt.

`conda create -n env_name [python=X.X] [LIST_OF_PACKAGES]`
Here `-n env_name` sets the name of your environment (-n for name) and LIST_OF_PACKAGES is the list of packages you want to be installed in the environment. If you wish to install a specific version of Python to be installed, say 3.7, use python=3.7. For example, to create an environment named my_env with `Python 3.7`, and install NumPy and Keras in it, use the command below.

`conda create -n my_env python=3.7 numpy Keras`

## Entering (Activate)/ Deactivate an environment
Once you have an environment created, you can enter into it by using:

```Terminal
# For  conda 4.6 and later versions on Linux/macOS/Windows, use
conda activate my_env
#For conda versions prior to 4.6 on Linux/macOS, use 
source activate my_env
#For conda versions prior to 4.6 on Windows, use 
activate my_env

# For  conda 4.6 and later versions on Linux/macOS/Windows, use
conda deactivate
#For conda versions prior to 4.6 on Linux/macOS, use 
source deactivate
#For conda versions prior to 4.6 on Windows, use 
deactivate

```

When you're in the environment, you'll see the environment name in the terminal prompt. Something like `(my_env) ~ $`

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
conda install numpy scipy pandas
conda install numpy=1.10
conda remove PACKAGE_NAME
conda update package_name
```

- If you want to update all packages in an environment, which is often useful, use `conda update --all`. And finally, to list installed packages, it's `conda list` which you've seen before.

- Search a Package to Install
    + If you don't know the exact name of the package you're looking for, you can try searching with `conda search *SEARCH_TERM*`. For example, I know I want to install Beautiful Soup, but I'm not sure of the exact package name. So, I try conda search *beautifulsoup*. Note that your shell might expand the wildcard * before running the conda command. To fix this, wrap the search string in single or double quotes like `conda search '*beautifulsoup*'`.



## How to Install pip Package Manager
If you have successfully installed Anaconda/Miniconda, possibly you will have conda (and pip) automatically installed on your system. If pip is not there, we recommend you install the pip as well because you will be able to run pip commands only after installing it.

```Terminal 
# Check if pip is already installed, by running this command on Terminal/Anaconda Prompt
pip --version

# Once you have conda installed, run the command below on Terminal/Anaconda Prompt
conda install pip
```

**Update Note**

In newer version of Anaconda/Miniconda, both pip and conda package managers are included by default, so you do not need to install them separately.

## Additional Resources
- [Managing virtual environments and packages with pip](https://docs.python.org/3/tutorial/venv.html)
- [Managing virtual environments with conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#managing-environments)
- [A comprehensive cheat sheet of Conda 4.6 commands](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
- [A comprehensive cheat sheet of Conda version prior to 4.6 commands](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)


## Saving and loading environments
A really useful feature is sharing environments so others can install all the packages used in your code, with the correct versions. Let's see all the package-names, including the Python version present in the current environment, using the command:

### Export Env
- `conda env export`
- `conda env export > environment.yaml`
- `pip freeze > requirements.txt`

### To create an environment from an environment file, use the following command: 
- `conda env create -f environment.yaml`
- `pip install -r requirements.txt`

## Removing an environment
If there are environments you don't use anymore, use the command below to remove the specified environment (here, named env_name).

- `conda env remove -n env_name`



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



PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=Ipmwpb70FRKgPzAdeVXuiZPC] [wp-includes/rest-api/class-wp-rest-server.php:1193 

Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 

WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:424 

WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:324 rest_api_loaded(), 

wp-includes/class-wp-hook.php:348 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:418 do_action_ref_array(), wp-includes/class-wp.php:813 WP->parse_request(), wp-includes/functions.php:1336 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

03:22:13 PM



PHP message: Deprecated: Constant FILTER_SANITIZE_STRING is deprecated in /var/www/wp-content/plugins/wpseo-news/classes/meta-box.php on line 59 [kbb2023-develop.go-vip.net/sm/f07d8d7b2652873f485707eab4f3d300bf1f6f3b42912e189c8933b1b9b3dfde.map] [wp-content/plugins/wpseo-news/classes/wpseo-news.php:48 WPSEO_News_Meta_Box->register_hooks(), wp-content/plugins/wpseo-news/wpseo-news.php:61 WPSEO_News->__construct(), wp-includes/class-wp-hook.php:324 __wpseo_news_main(), wp-includes/class-wp-hook.php:348 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-settings.php:506 do_action('plugins_loaded'), wp-config.php:53 require_once('wp-settings.php'), wp-load.php:50 require_once('wp-config.php'), wp-blog-header.php:13 require_once('wp-load.php'), index.php:17 require('wp-blog-header.php')]

04:58:29 PM	
PHP message: Deprecated: Constant FILTER_SANITIZE_STRING is deprecated in /var/www/wp-content/plugins/wpseo-news/classes/meta-box.php on line 59 [kbb2023-develop.go-vip.net/wp-admin/admin-ajax.php] [wp-content/plugins/wpseo-news/classes/wpseo-news.php:48 WPSEO_News_Meta_Box->register_hooks(), wp-content/plugins/wpseo-news/wpseo-news.php:61 WPSEO_News->__construct(), wp-includes/class-wp-hook.php:324 __wpseo_news_main(), wp-includes/class-wp-hook.php:348 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-settings.php:506 do_action('plugins_loaded'), wp-config.php:53 require_once('wp-settings.php'), wp-load.php:50 require_once('wp-config.php'), wp-admin/admin-ajax.php:22 require_once('wp-load.php')]

04:58:29 PM	
PHP message: Deprecated: Constant WP_Stream\FILTER_SANITIZE_STRING is deprecated in /var/www/wp-content/plugins/stream/classes/class-filter-input.php on line 100 [kbb2023-develop.go-vip.net/wp-admin/admin-ajax.php] [wp-content/plugins/stream/classes/class-filter-input.php:80 WP_Stream\Filter_Input::filter(), wp-content/plugins/stream/includes/functions.php:22 WP_Stream\Filter_Input::super(), wp-content/plugins/stream/classes/class-log.php:46 wp_stream_filter_input(), wp-content/plugins/stream/classes/class-plugin.php:139 WP_Stream\Log->__construct(), wp-content/plugins/stream/stream.php:40 WP_Stream\Plugin->__construct(), wp-content/mu-plugins/vip-helpers/vip-utils.php:1400 include_once('wp-content/plugins/stream/stream.php'), wp-content/mu-plugins/vip-helpers/vip-utils.php:1232 _wpcom_vip_include_plugin(), wp-content/client-mu-plugins/plugin-loader.php:15 wpcom_vip_load_plugin(), wp-content/mu-plugins/z-client-mu-plugins.php:123 include_once('wp-content/client-mu-plugins/plugin-loader.php'), wp-settings.php:398 include_once('wp-content/mu-plugins/z-client-mu-plugins.php'), wp-config.php:53 require_once('wp-settings.php'), wp-load.php:50 require_once('wp-config.php'), wp-admin/admin-ajax.php:22 require_once('wp-load.php')]

04:58:29 PM	
PHP message: Deprecated: DateTime::__construct(): Passing null to parameter #1 ($datetime) of type string is deprecated in /var/www/wp-content/plugins/kbb-foundation/acf/class-kbb-foundation-acf-vehicle.php on line 641 [kbb2023-develop.go-vip.net/sm/f07d8d7b2652873f485707eab4f3d300bf1f6f3b42912e189c8933b1b9b3dfde.map] [wp-content/plugins/kbb-foundation/acf/class-kbb-foundation-acf-vehicle.php:641 DateTime->__construct(), wp-includes/class-wp-hook.php:324 KBB_Foundation_ACF_Vehicle->get_datalayer_object_from_post(), wp-includes/class-wp-hook.php:348 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:830 do_action_ref_array(), wp-includes/functions.php:1336 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

04:58:29 PM	
PHP message: Deprecated: str_replace(): Passing null to parameter #2 ($replace) of type array|string is deprecated in /var/www/wp-content/plugins/kbb-foundation/omniture/class-kbb-foundation-omniture.php on line 116 [kbb2023-develop.go-vip.net/sm/f07d8d7b2652873f485707eab4f3d300bf1f6f3b42912e189c8933b1b9b3dfde.map] [wp-content/plugins/kbb-foundation/omniture/class-kbb-foundation-omniture.php:116 str_replace(), wp-includes/class-wp-hook.php:324 KBB_Foundation_Omniture->set_omniture_spec(), wp-includes/class-wp-hook.php:348 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:830 do_action_ref_array(), wp-includes/functions.php:1336 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]


-------------------


PHP message: Warning: Attempt to read property "post_content" on null in /var/www/wp-content/plugins/kbb-foundation/public/class-kbb-foundation-public.php on line 354 [www.kbb.com/error/?requestedurl=https://www.kbb.com/pixall/v2/event?p=DealerDotCom&d=kbbcox&w=KBB&v=mvxZC3vAJIFDhLSEh4BeHOWc&bv=y2pcGvYrl45ONx0J8gpkIN2M&ii=994631819796174952&pt=vlp&ab=&x=boost%3D0&l=classlistnew&pi=classlistnew&smi=75000&cm=eyJteUNvbnN1bWVySWQiOiIwMUhETUNLS0M0WUY3TTlIRkVSU1FaS0JWQyIsImVtYWlsIjoibWlhZ3JhbnQ0NTRAZ21haWwuY29tIn0%3D&zip=77065&et=ajaxPageView&pm=%7B%22wrapperName%22%3A%22kbb%22%2C%22jsVersionId%22%3A%221.41.34%22%7D&u=https%3A%2F%2Fwww.kbb.com%2Fcars-for-sale%2Fall%3FisNewSearch%3Dtrue%26keywordPhrases%3Dveloster%26maxMileage%3D75000&rn=52311916144&Reference=18.8d17dd17.1699463182.249d54d] [wp-includes/class-wp-hook.php:310 KBB_Foundation_Public->change_theme_scripts(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/general-template.php:3053 do_action('wp_head'), wp-content/themes/cox-kbb/header.php:17 wp_head(), wp-includes/template.php:785 require_once('wp-content/themes/cox-kbb/header.php'), wp-includes/template.php:720 load_template(), wp-includes/general-template.php:48 locate_template(), wp-content/themes/cox-kbb/404.php:8 get_header(), wp-includes/template-loader.php:106 include('wp-content/themes/cox-kbb/404.php'), wp-blog-header.php:19 require_once('wp-includes/template-loader.php'), index.php:17 require('wp-blog-header.php')]

05:06:23 PM	
PHP message: Warning: Attempt to read property "post_content" on null in /var/www/wp-content/plugins/kbb-foundation/public/class-kbb-foundation-public.php on line 233 [www.kbb.com/error/?requestedurl=https://www.kbb.com/pixall/v2/event?p=DealerDotCom&d=kbbcox&w=KBB&v=mvxZC3vAJIFDhLSEh4BeHOWc&bv=y2pcGvYrl45ONx0J8gpkIN2M&ii=994631819796174952&pt=vlp&ab=&x=boost%3D0&l=classlistnew&pi=classlistnew&smi=75000&cm=eyJteUNvbnN1bWVySWQiOiIwMUhETUNLS0M0WUY3TTlIRkVSU1FaS0JWQyIsImVtYWlsIjoibWlhZ3JhbnQ0NTRAZ21haWwuY29tIn0%3D&zip=77065&et=ajaxPageView&pm=%7B%22wrapperName%22%3A%22kbb%22%2C%22jsVersionId%22%3A%221.41.34%22%7D&u=https%3A%2F%2Fwww.kbb.com%2Fcars-for-sale%2Fall%3FisNewSearch%3Dtrue%26keywordPhrases%3Dveloster%26maxMileage%3D75000&rn=52311916144&Reference=18.8d17dd17.1699463182.249d54d] [wp-content/plugins/kbb-foundation/public/class-kbb-foundation-public.php:282 KBB_Foundation_Public->pre_load_lcp_img_for_landing_page(), wp-includes/class-wp-hook.php:310 KBB_Foundation_Public->add_mobile_resource_hints(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/general-template.php:3053 do_action('wp_head'), wp-content/themes/cox-kbb/header.php:17 wp_head(), wp-includes/template.php:785 require_once('wp-content/themes/cox-kbb/header.php'), wp-includes/template.php:720 load_template(), wp-includes/general-template.php:48 locate_template(), wp-content/themes/cox-kbb/404.php:8 get_header(), wp-includes/template-loader.php:106 include('wp-content/themes/cox-kbb/404.php'), wp-blog-header.php:19 require_once('wp-includes/template-loader.php'), index.php:17 require('wp-blog-header.php')]

05:06:25 PM	
ort::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analytics_for_iframe_video(), wp-includes/plugin.php:205 WP_Hook->apply_filters(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1268 apply_filters('the_content'), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:1071 Wpil_Report::process_content(), wp-content/plugins/link-whisper-premium/core/Wpil/Report.php:2055 Wpil_Report::getContentLinks(), wp-content/plugins/link-whisper-premium/core/Wpil/Post.php:1523 Wpil_Report::stored_link_content_changed(), wp-includes/class-wp-hook.php:312 Wpil_Post::updateStatMark(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/post.php:4753 do_action('save_post'), wp-content/plugins/wp-large-options-master/wp-large-options.php:55 wp_insert_post(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:237 wlo_add_option(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:223 GeneralHelper::cache_common_data(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:253 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/datalayer-utils.php:169 Datalayer_Utils::get_newcar_years_data(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:368 Datalayer_Utils::get_datalayer_info(), wp-content/plugins/cox-auto/analytics/class-cox-auto-datalayer.php:67 GeneralHelper::get_datalayer_object_from_api(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:427 DataLayer->__construct(), wp-content/plugins/cox-auto/analytics/class-cox-auto-analytics.php:444 Cox_Auto_Analytics::get_video_vehicle_data(), wp-includes/class-wp-hook.php:310 Cox_Auto_Analytics->youtube_analyti...

05:06:26 PM	
PHP message: Warning: vip_safe_wp_remote_request: Blog ID 1: Requesting https://psp-service.prod.duvh.dealer.com/kbb/triggers/v1/NTWLQSmYLnfJWNDqMbCH2QJX with method GET and a timeout of 3 failed. Result: O:8:'WP_Error':3:{s:6:'errors';a:1:{s:19:'http_request_failed';a:1:{i:0;s:70:'cURL error 6: Could not resolve host: psp-service.prod.duvh.dealer.com';}}s:10:'error_data';a:0:{}s:18:' in /var/www/wp-content/mu-plugins/vip-helpers/vip-utils.php on line 901 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=NTWLQSmYLnfJWNDqMbCH2QJX] [wp-content/mu-plugins/vip-helpers/vip-utils.php:901 trigger_error(), wp-content/mu-plugins/vip-helpers/vip-utils.php:925 vip_safe_wp_remote_request(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:211 vip_safe_wp_remote_get(), wp-content/plugins/kbb-foundation/helpers/researchable-helper.php:69 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php:81 Researchable_Helper::get_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=NTWLQSmYLnfJWNDqMbCH2QJX] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=NTWLQSmYLnfJWNDqMbCH2QJX] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Attempt to read property "body" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=NTWLQSmYLnfJWNDqMbCH2QJX] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 84 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=NTWLQSmYLnfJWNDqMbCH2QJX] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 84 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=NTWLQSmYLnfJWNDqMbCH2QJX] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Undefined property: stdClass::$subCounty in /var/www/wp-content/plugins/kbb-foundation/helpers/location-helper.php on line 51 [www.kbb.com/wp-json/location/api/v1/byzipcode/?zipcode=50003] [wp-content/plugins/kbb-foundation/helpers/location-helper.php:15 Location_Helper::parse_location_data(), wp-content/plugins/kbb-foundation/helpers/location-api-utils.php:15 Location_Helper::get_location_by_zip(), wp-includes/rest-api/class-wp-rest-server.php:1194 Location_Api_Utils->get_kbb_location_by_zipcode(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Attempt to read property "code" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/location-helper.php on line 51 [www.kbb.com/wp-json/location/api/v1/byzipcode/?zipcode=50003] [wp-content/plugins/kbb-foundation/helpers/location-helper.php:15 Location_Helper::parse_location_data(), wp-content/plugins/kbb-foundation/helpers/location-api-utils.php:15 Location_Helper::get_location_by_zip(), wp-includes/rest-api/class-wp-rest-server.php:1194 Location_Api_Utils->get_kbb_location_by_zipcode(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Undefined property: stdClass::$alphaZone in /var/www/wp-content/plugins/kbb-foundation/helpers/location-helper.php on line 53 [www.kbb.com/wp-json/location/api/v1/byzipcode/?zipcode=50003] [wp-content/plugins/kbb-foundation/helpers/location-helper.php:15 Location_Helper::parse_location_data(), wp-content/plugins/kbb-foundation/helpers/location-api-utils.php:15 Location_Helper::get_location_by_zip(), wp-includes/rest-api/class-wp-rest-server.php:1194 Location_Api_Utils->get_kbb_location_by_zipcode(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:26 PM	
PHP message: Warning: Attempt to read property "code" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/location-helper.php on line 53 [www.kbb.com/wp-json/location/api/v1/byzipcode/?zipcode=50003] [wp-content/plugins/kbb-foundation/helpers/location-helper.php:15 Location_Helper::parse_location_data(), wp-content/plugins/kbb-foundation/helpers/location-api-utils.php:15 Location_Helper::get_location_by_zip(), wp-includes/rest-api/class-wp-rest-server.php:1194 Location_Api_Utils->get_kbb_location_by_zipcode(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: vip_safe_wp_remote_request: Blog ID 1: Requesting https://psp-service.prod.duvh.dealer.com/kbb/triggers/v1/fn30y9DH9iAMAoAtQVq9FQCk with method GET and a timeout of 3 failed. Result: O:8:'WP_Error':3:{s:6:'errors';a:1:{s:19:'http_request_failed';a:1:{i:0;s:70:'cURL error 6: Could not resolve host: psp-service.prod.duvh.dealer.com';}}s:10:'error_data';a:0:{}s:18:' in /var/www/wp-content/mu-plugins/vip-helpers/vip-utils.php on line 901 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=fn30y9DH9iAMAoAtQVq9FQCk] [wp-content/mu-plugins/vip-helpers/vip-utils.php:901 trigger_error(), wp-content/mu-plugins/vip-helpers/vip-utils.php:925 vip_safe_wp_remote_request(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:211 vip_safe_wp_remote_get(), wp-content/plugins/kbb-foundation/helpers/researchable-helper.php:69 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php:81 Researchable_Helper::get_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=fn30y9DH9iAMAoAtQVq9FQCk] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=fn30y9DH9iAMAoAtQVq9FQCk] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "body" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=fn30y9DH9iAMAoAtQVq9FQCk] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 84 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=fn30y9DH9iAMAoAtQVq9FQCk] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 84 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=fn30y9DH9iAMAoAtQVq9FQCk] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: vip_safe_wp_remote_request: Blog ID 1: Requesting https://psp-service.prod.duvh.dealer.com/kbb/triggers/v1/d9Gst0lvbHHck5H76Eh9e7mh with method GET and a timeout of 3 failed. Result: O:8:'WP_Error':3:{s:6:'errors';a:1:{s:19:'http_request_failed';a:1:{i:0;s:70:'cURL error 6: Could not resolve host: psp-service.prod.duvh.dealer.com';}}s:10:'error_data';a:0:{}s:18:' in /var/www/wp-content/mu-plugins/vip-helpers/vip-utils.php on line 901 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=d9Gst0lvbHHck5H76Eh9e7mh] [wp-content/mu-plugins/vip-helpers/vip-utils.php:901 trigger_error(), wp-content/mu-plugins/vip-helpers/vip-utils.php:925 vip_safe_wp_remote_request(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:211 vip_safe_wp_remote_get(), wp-content/plugins/kbb-foundation/helpers/researchable-helper.php:69 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php:81 Researchable_Helper::get_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=d9Gst0lvbHHck5H76Eh9e7mh] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=d9Gst0lvbHHck5H76Eh9e7mh] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "body" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=d9Gst0lvbHHck5H76Eh9e7mh] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 84 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=d9Gst0lvbHHck5H76Eh9e7mh] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 84 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=d9Gst0lvbHHck5H76Eh9e7mh] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: vip_safe_wp_remote_request: Blog ID 1: Requesting https://psp-service.prod.duvh.dealer.com/kbb/triggers/v1/YKvRLEbNcSRsP7EzEbEagBD2 with method GET and a timeout of 3 failed. Result: O:8:'WP_Error':3:{s:6:'errors';a:1:{s:19:'http_request_failed';a:1:{i:0;s:70:'cURL error 6: Could not resolve host: psp-service.prod.duvh.dealer.com';}}s:10:'error_data';a:0:{}s:18:' in /var/www/wp-content/mu-plugins/vip-helpers/vip-utils.php on line 901 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=YKvRLEbNcSRsP7EzEbEagBD2] [wp-content/mu-plugins/vip-helpers/vip-utils.php:901 trigger_error(), wp-content/mu-plugins/vip-helpers/vip-utils.php:925 vip_safe_wp_remote_request(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:211 vip_safe_wp_remote_get(), wp-content/plugins/kbb-foundation/helpers/researchable-helper.php:69 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php:81 Researchable_Helper::get_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=YKvRLEbNcSRsP7EzEbEagBD2] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

05:06:27 PM	
PHP message: Warning: Trying to access array offset on value of type null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=YKvRLEbNcSRsP7EzEbEagBD2] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

PHP message: Warning: Undefined array key 1 in /var/www/wp-content/plugins/kbb-foundation/routes/class-kbb-foundation-routes.php on line 260 [www.kbb.com/car-news/how-much-does-it-cost-to-charge-an-ev/?PSID=CSFB1] [wp-includes/class-wp-hook.php:310 KBB_Foundation_Routes->redirect_article_type(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:517 WP_Hook->do_action(), wp-includes/template-loader.php:13 do_action('template_redirect'), wp-blog-header.php:19 require_once('wp-includes/template-loader.php'), index.php:17 require('wp-blog-header.php')]

06:39:48 PM	
PHP message: Warning: vip_safe_wp_remote_request: Blog ID 1: Requesting https://psp-service.prod.duvh.dealer.com/kbb/triggers/v1/P2LSWfeobptDYhR7Ia52ZPKw with method GET and a timeout of 3 failed. Result: O:8:'WP_Error':3:{s:6:'errors';a:1:{s:19:'http_request_failed';a:1:{i:0;s:70:'cURL error 6: Could not resolve host: psp-service.prod.duvh.dealer.com';}}s:10:'error_data';a:0:{}s:18:' in /var/www/wp-content/mu-plugins/vip-helpers/vip-utils.php on line 901 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=P2LSWfeobptDYhR7Ia52ZPKw] [wp-content/mu-plugins/vip-helpers/vip-utils.php:901 trigger_error(), wp-content/mu-plugins/vip-helpers/vip-utils.php:925 vip_safe_wp_remote_request(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:211 vip_safe_wp_remote_get(), wp-content/plugins/kbb-foundation/helpers/researchable-helper.php:69 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php:81 Researchable_Helper::get_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

06:39:48 PM	
PHP message: Warning: Attempt to read property "response" on null in /var/www/wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php on line 83 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=P2LSWfeobptDYhR7Ia52ZPKw] [wp-includes/rest-api/class-wp-rest-server.php:1194 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:418 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:310 rest_api_loaded(), wp-includes/class-wp-hook.php:334 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:398 do_action_ref_array(), wp-includes/class-wp.php:779 WP->parse_request(), wp-includes/functions.php:1335 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]



PHP message: Warning: vip_safe_wp_remote_request: Blog ID 1: 

Requesting https://psp-service.prod.duvh.dealer.com/kbb/triggers/v1/ZfaX5x72isSGrqk4qmFiaBem with method GET and a timeout of 3 failed.

 Result: O:8:'WP_Error':3:{s:6:'errors';a:1:{s:19:'http_request_failed';a:1:{i:0;s:70:'cURL error 6: Could not resolve host: psp-service.prod.duvh.dealer.com';}}s:10:'error_data';a:0:{}s:18:' in /var/www/wp-content/mu-plugins/vip-helpers/vip-utils.php on line 901 
 
 [www.kbb.com/wp-json/reference/api/v1/ads/?pixallid=ZfaX5x72isSGrqk4qmFiaBem] [wp-content/mu-plugins/vip-helpers/vip-utils.php:901 trigger_error(), wp-content/mu-plugins/vip-helpers/vip-utils.php:925 vip_safe_wp_remote_request(), wp-content/plugins/kbb-foundation/helpers/general-helper.php:211 vip_safe_wp_remote_get(), wp-content/plugins/kbb-foundation/helpers/researchable-helper.php:69 GeneralHelper::GetResponseForApi(), wp-content/plugins/kbb-foundation/helpers/reference-api-utils.php:81 Researchable_Helper::get_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1193 Reference_Api_Utils->get_kbb_psp_data(), wp-includes/rest-api/class-wp-rest-server.php:1041 WP_REST_Server->respond_to_request(), wp-includes/rest-api/class-wp-rest-server.php:431 WP_REST_Server->dispatch(), wp-includes/rest-api.php:424 WP_REST_Server->serve_request(), wp-includes/class-wp-hook.php:324 rest_api_loaded(), wp-includes/class-wp-hook.php:348 WP_Hook->apply_filters(), wp-includes/plugin.php:565 WP_Hook->do_action(), wp-includes/class-wp.php:418 do_action_ref_array(), wp-includes/class-wp.php:813 WP->parse_request(), wp-includes/functions.php:1336 WP->main(), wp-blog-header.php:16 wp(), index.php:17 require('wp-blog-header.php')]

06:10:16 PM	

