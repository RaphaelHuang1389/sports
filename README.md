# Sports Predictions

## Dartmouth Machine Learning Club

This repository is for the Sports Statistics Prediction Section.

## Getting Started

Download [Pycharm](https://www.jetbrains.com/pycharm/download/) and [Python 3](https://www.python.org/downloads/). We use the [SciKit-Learn](http://scikit-learn.org/stable/) library for Machine Learning so install that too. Also make sure to join our [Slack page](https://dartmouthml.slack.com/).

### Installing Libraries

Installing Python 3 should also install [pip](https://pip.pypa.io/en/stable/), which you will use to install 3rd party Python libraries. To install the libraries open the Terminal (or Command Line on Windows) and type the following:

```
pip install -U scikit-learn
```

### Git
We use git to "push" and "pull" code from GitHub. It should already be installed on Macs. To use it open a folder you want to store the ML files in. In terminal type `cd filepath` where `filepath` is the path to the folder you want to use. Type `git init`. This will recreate a repository. 
From there you need to "clone" the repository from Github. Type the following:

```
git clone https://github.com/DartmouthMachineLearning/sports.git
cd sports/
git remote add origin https://github.com/DartmouthMachineLearning/sports.git
git pull
```

Whenever you write code, you need to push it to GitHub. First irst update your local copy with `git pull`. Then add changed files to your staging area with `git add .`, then commit these changes with `git commit -m "message"` where `message` is a description of what you changed, like "Updated README.md". Once committed, push your code with `git push`.


## Style Guide
When collaborating on code, consistent style is important. This [Python Style Guide](https://www.python.org/dev/peps/pep-0008/) is a good start. Here are some general things to keep in mind:

- Comment your code well.
- Give variables and functions names such that other people will understand what they're for without reading the code thoroughly.
- Group lines of code by function with blocks never being more than 8 lines or so.
- Make code modular and write functions wherever possible.
- Sorry, python uses snake case (`like_this`) for all names other than class names which use Camel Case (`LikeThis`).

Here is an example of how your files should be setup:

```python
# File name, Creation Date
# Collaborator name, Last Modification Date
# Short description of what the code does

# import statements

class MyClass:
    """
    This is my custom class description, my class has the same name as the file
    """
    def __init__(self, var1, var2):
        self.variable1 = var1  # this variable is used for ____
        self.variable2 = var2  # this variable is used for ____
        self.variable3 = self.setup_func(self.variable1, self.variable2)  # what this func is setting up
        
    
    def setup_func(self, var1, var2):
        """
        Description of what this function does
        :param var1: This is what var1 is
        :type var1: This is the datatype of var1
        :param var2: This is what var2 is
        :type var2: This is the datatype of var2
        """
        var3 = var1 + var2  # this line adds the sum
        var3 += var1 - var2  # this line adds the difference
        return var3  # return the variable
```


## Helpful Links

- [Slack](https://dartmouthml.slack.com/)

- [Pycharm](https://www.jetbrains.com/pycharm/download/)

- [SciKit-Learn Python Library](http://scikit-learn.org/stable/)
