# Python

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

# References
- document: document: https://peps.python.org/pep-0008/
