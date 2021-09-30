# GITS - GIT Simplified
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/34/badge)](https://bestpractices.coreinfrastructure.org/projects/34)
![GitHub](https://img.shields.io/github/license/arjunptm/GITS)
[![Build Status](https://github.com/arjunptm/GITS/workflows/Build%20Status/badge.svg)](https://github.com/arjunptm/GITS/actions)
![GitHub](https://img.shields.io/badge/language-python-blue.svg)
![GitHub](https://img.shields.io/badge/language-shell-orange.svg)


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5532929.svg)](https://doi.org/10.5281/zenodo.5532929)
[![codecov](https://codecov.io/gh/arjunptm/GITS/branch/master/graph/badge.svg?token=KNQPMEDEH2)](https://codecov.io/gh/arjunptm/GITS)

![GitHub issues](https://img.shields.io/github/issues/arjunptm/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/arjunptm/GITS)

![GitHub pull requests](https://img.shields.io/github/issues-pr/arjunptm/GITS)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/arjunptm/GITS)

[![Alt text](http://i3.ytimg.com/vi/XWzKtZcDmKU/maxresdefault.jpg)](https://www.youtube.com/watch?v=XWzKtZcDmKU)

## Sitemap

Reading all 3 sections before starting your work will make life a lot easier for the next few weeks!
1. [Jump here](#welcome-potential-developers) for the easiest Phase 2 start-up guide
2. [Jump here](#about-the-project) to get information on how this project works
3. [Jump here](#installation-guidelines) if you want installation instructions

# Welcome, potential developers! <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px">
GITS, or Git Simplified, is a tool designed to help make git commands easier and more intuitive to use for beginners and advanced users alike.
This first section should help you familiarize yourself with this project, so you can spend more time improving/adding features instead of trying to learn how our code works.
<!-- GITS simplifies (makes it human-friendly) many commonly used git commands such as [add](code/gits_add.py), [commit](code/gits_commit.py), [push](code/gits_push.py), and [checkout](code/gits_checkout.py). -->

<!-- The structure of our repo is as follows:
1. [`code`](code) contains all of our working code. The structure is as follows:
   - [`gits.py`](code/gits.py) is where it all starts. For each feature we support, we have a few lines that call the corresponding `gits_<commandname>.py`.
   - `gits_<commandname.>py` is a file describing in detail what each supported command should do. E.g. [`gits_clone.py`](code/gits_clone.py) to clone, and [`gits_add.py`](code/gits_add.py) to add.
   - To modify how a command is called, you need to edit [`gits.py`](code/gits.py). To change what a command does, you need to edit `gits_<commandname.>py`.
   - To add a new command, you need to add corresponding calls and imports to [`gits.py`](code/gits.py), and additionally create a `gits_<commandname.>py` to go with it.
2. [`configurations`](configurations) contains the files required to install/set-up GITS on your system. Further instructions can be found [below](#installation-guidelines).
3. [`docs`](docs) has all other supporting documentation.
4. [`test`](test) contains all of our test cases.  -->

## Repo organization
The structure of our repo is as follows:
1. [`code`](code) contains all of our working code. The structure is as follows:
   - [`gits.py`](code/gits.py) is where it all starts. For each feature we support, we have a few lines that call the corresponding `gits_<commandname>.py`.
   - `gits_<commandname.>py` is a file describing in detail what each supported command should do. E.g. [`gits_clone.py`](code/gits_clone.py) to clone, and [`gits_add`](code/gits_add.py) to add.
2. [`configurations`](configurations) contains the files required to install/set-up GITS on your system. Further instructions can be found [below](#installation-guidelines).
3. [`docs`](docs) has all other supporting documentation.
4. [`test`](test) contains all of our test cases. 

## How to make progress
GITS has support for many commonly used git commands such as [add](code/gits_add.py), [commit](code/gits_commit.py), and [push](code/gits_push.py).
The main way of making progress in this project is to expand the range of commands we support. 

1. To modify how a command is called, you need to edit [`gits.py`](code/gits.py). To change what a command does, you need to edit `gits_<commandname.>py`.
2. To add a new command, you need to add corresponding calls and imports to [`gits.py`](code/gits.py), and additionally create a `gits_<commandname.>py` to go with it.
3. Update or add new test files depending on what changes you made.

Additionally, while you can think of new features to add and more git commands to simplify, we have also left a few issues marked [`good first issue`](https://github.com/arjunptm/GITS/labels/good%20first%20issue) open as a good place to get started from. You may work on these to help you get comfortable with the project to begin with. 

Also check out our [Phase 1 project board](https://github.com/arjunptm/GITS/projects/1) to get a good idea of where each process stands. We also have a [Phase 2 project board](https://github.com/arjunptm/GITS/projects/2) to help you start your project.

Note that if you fork this project to work on it yourself, it won't automatically fork the issues/project boards. You can always come back here to refer to them, and then create a copy in your fork for the Phase 2 work.

## Pre-set tasks
After forking this repository onto your own account, here are some tasks that you can start off with. You can find the same list with more details under [issues](https://github.com/arjunptm/GITS/issues), and also in [projects](https://github.com/arjunptm/GITS/projects/1).

1. Organizational tasks
    - Create your Phase 2 project board.
    - Copy issues from this
    - Create your own account for third party services (Zenodo, Codecov, etc) and also update their badges in the [readme](README.md).
2. Development tasks
    - Add more basic (add link here) commands to GITS.
    - Add more simplified functionalities to GITS. (Add enhancement issues link here)
    - Add more test cases for each command / funcionality.
    - Convert existing functionalities into interactive ones (similar to [`gits_rebase.py`](code/gits_rebase.py)).

# Installation Guidelines:
Please note that this will run directly on Linux/MacOS. If you are running it on Windows, you will need to install some bash terminal for executing it. We recommend git bash, that comes bundled with [git](https://git-scm.com/downloads) during installation. This works best as having git installed is a prerequisite for running this tool anyway.

Once you have git installed, follow these steps: 
1. Clone the GITS repository <br/>
2. Navigate inside GITS folder and enter the following command: <br/> `pip install -r requirements.txt` <br/>
3. Navigate inside the configurations folder and run the folllowing commands: <br/>
4. If your main method of running `.py` files is `python3 ...`, then run the following command: <br/>
  `chmod +x python3_project_init.sh` <br/> 
  `./python3_project_init.sh` <br/><br/>
  If you just use `python ...` then run the following command:  <br/>
  `chmod +x project_init.sh` <br/> 
  `./project_init.sh` <br/> 

5. Update the bashrc file: <br/>
  `source ~/.bashrc` <br/>
6. Run `gits hello_world` from any directory. If you end up getting a welcome message you're good to go! <br/>

# About the project
This section describes all the features of this project that you would want to be aware of.

## About GITS
We hope for GITS to be used as a complete alternative to git (for most day-to-day use cases). This means two things:
  - We need to simplify complex actions that require multiple git commands in a sequence.
  - We also need to support basic git commands, so you won't have to remember whether to use GITS or git everytime you're programming.

A full list and explanation on everything we support can be found in [`supported_commands.md`](docs/supported_commands.md).

We heavily rely on the [`argparse`](https://docs.python.org/3/library/argparse.html) module, and the documentation for [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method will be extremely helpful.

## All the repository BLING
This repository has many features that make the development process easy and fun. Here's a quick overview:

### Github Actions
Contrary to the popular Travis CI, We've set up the repository architecture to use GitHub actions. If you need any more automation on running test files during pushes or pull requests, we've got you covered! Editing this is easy, and you have the added support of the GitHub [marketplace](https://github.com/marketplace) for many extensions you can add in few simple steps. 

### pydoc implementation
We have tried to write as much documentation as possible. You can use pydoc to go through the documentation. 
For example if you want to go through all the documentation for all files in code/ directory, do the following: 

1. Switch to the code directory by using `cd code`<br>
2. Run the pydoc browser-based server `python3 -m pydoc -b `

This will open up a browser window and you can see all the files. You can click on a particular file to access the documentation associated with that file.

### Style Checker and Analyzer
We are using flake8 / pep8 as our style checker and code analyzer. While contributing to this project, make sure you conform to norms dictated by flake8. While our GitHub actions automatically run flake8 tests, you may also run it locally to check for inconsistencies before pushing your code.

1. Install flake8
    - `python -m pip install flake8` to install flake8 for your default python installation.
    - Or, `python<version> -m pip install flake8` to install it to a specific version.
2. Using Flake8
    - To start using Flake8, open an interactive shell and run one of the following,
    - `flake8 path/to/code/to/check.py`
    - `flake8 path/to/code/`

This repository is made for CSC 510 Software Engineering Course at NC State University.

Group 5 Team Members: 

* Rohan Prabhune
* Swetha Gavini
* Arjun Madhusudan
* Ramya Sai Mullapudi
* Krishna Saurabh
