# Modern Python

## Preface
This chapter discusses specific Python features:
- Tools
- APIs and services
- Variables and type hinting
- Data structures
- Web frameworks

## Tools
### Package management
Consider an alternative tool like *Poetry*.

### Virtual Environments
It's common to work with multiple versions of Python, or make installations specific to a project, so you know exactly which packages are in there. To do this, Python suports *virtual environments*. There are just directories into which pip writes downloaded packages.

The program for this is *venv*, and it's been included with standard Python since **version 3.4**

### Poetry
This combination of pip and venv is so common that people started combining them to save steps and avoid that soure shell wizardry. One such package is *Pipenv*, but a newer rival called *Poetry* is becoming more popular.

```
pip install poetry
```

Besides downloading single packages, pip and Poetry manage multiple packages in config files: **requirements.txt** for pip, and **pyproject.toml** for Poetry.

Poetry and pip dont just download packages, but also manage the tricky dependencies that packages may have on other packages. You can specify desired package version as minima, maxima, ranges, or exact values (also known as **pinning**).

### Source Formatting
Source Formatting is helpful. Avoid code formatting (bikeshedding) arguments with a tool that massages source into a standard, nonweird format. One good choice is Black. Install it:
```
pip install black
```

### Testing
The standard Python test package is unittest, the industrial-strength Python test package used by most Python developers is pytest.
```
pip install pytest
```

### Source control and Continuous Integration
The almost-universal solution for source control now is *Git*, with storate repositories (repos) at sties like GitHub and GitLab. The pre-commit tool runs various tests on your local machine (such as black and pytest) before committing to Git. After pushing to a remote Git repo, more continuous integration (CI) tests may be run there.

### Web Tools
- *FastAPI*: The web framework itself
- *Uvicorn*: An asynchronous web server
- *HTTPie*: A text web client, similar to curl
- *Requests*: A synchronous web client package
- *HTTPX*: A synchronous/asynchronous web client package

### API and Services.
We can define higher-level models to make our interlayer communication cleaner. These models rely on a fairly recent Python addition called *type hinting*.

### Variable Are Names
In Python, *object* is a data structure that wraps every distinct piece of data in the program, from an integer to a function, to anything that might define. It specifies, among other bookkeeping info, the following:
- A *unique identity* value
- The low-level *type* that matches the hardware
- The specific *value* (physical bits)
- A *reference count* of the number of variables that refer to it

Python is *strongly typed* at the object level (its type doesn't change, although its value might). Object is termed *mutable* if its value may be changed, *immutable* if not.

In many other languages, *variable* is a direct pointer to an area of memory that contains a raw value, stored in bits that follow the computer's hardware design. If you assign a new value to that variable, the language overwrites the previous value in memory with the new one.

That's direct and fast. The compiler keeps track of what goes where. It's one reason languages like C are faster than Python.

Now, here's the big difference with Python: a Python variable is just a *name* that is temporarily associated with a higher-level object in memory. If you assign a new value to a variable that refers to an immutable object, you're actually creating a new object that contains that value, and then getting the name to refer to that new object. The old object (that the name used to refer to) is then free, and its memory can be reclaimed if no other names are still referencing to it (i.e., its reference count is 0).

### Type Hints
Python 3.6 added *type hints* to declare the type of object to which a variable refers. They are used by various tools to ensure that use of variable is consistent. The standard type checker is called *mypy*.

### Web Frameworks
A Web Framework translates between HTTP bytes and Python data structures. It can save you a lot of effort. 

The *Web Server Gateway Interface (WSGI)* is a synchronous Python standard specification to connect application code to web servers. Tradional python web applications are built on WSGI. But synchronous communication may mean busy waiting for something (disk or network) that's much slower than CPU. Then you will look at concurrency. Concurrency has become more important in recent years.

Python *Asynchronous Server Gateway Interface (ASGI)* specification was developed.

#### Django
Django is a full-featured web framework that tags itself as "the web framework for perfectionists with deadlines". It was announced by **Adrian Holovaty and Simon Willison** in 2003, and named after **Django Reinhardt**, a 20th-centuary Belgian jazz guitarist. Django is often used for database-backed corporate sites

#### Flask
Flask introduced by *Armin Ronacher* in 2010, is a microframework.

#### FastAPI
FastAPI was published by **Sebastian Ramirez** in 2018. It is heavily designed on two third-party Python packages:
- *Starlette* for web details
- *Pydantic* for data details
