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

# Welcome, potential developers!
GITS, or Git Simplified, is a tool designed to help make git commands easier and more intuitive to use for beginners and advanced users alike.
This first section should help you familiarize yourself with this project, so you can spend more time improving/adding features instead of trying to learn how our code works.

We heavily rely on the [`argparse`](https://docs.python.org/3/library/argparse.html) module, and the documentation for [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument) method will be extremely helpful.

1. [`code`](code) contains all of our working code. The structure is as follows:
   - [`gits.py`](code/gits.py) is where it all starts. For each feature we support, we have a few lines that call the corresponding `gits_<commandname>.py`.
   - `gits_<commandname.>py` is a file describing in detail what each supported command should do. E.g. [`gits_clone.py`](code/gits_clone.py) to clone, and [`gits_add`](code/gits_add.py) to add.
   - To modify how a command is called, you need to edit [`gits.py`](code/gits.py). To change what a command does, you need to edit `gits_<commandname.>py`.
   - To add a new command, you need to add corresponding calls and imports to [`gits.py`](code/gits.py), and additionally create a `gits_<commandname.>py` to go with it.
2. [`configurations`](configurations) contains the files required to install/set-up GITS on your system. Further instructions can be found [below](#installation-guidelines).
3. [`test`](test) contains all of our test cases. 

Additionally, while you can think of new features to add and more git commands to simplify, we have also left a few issues marked [`good first issue`](https://github.com/arjunptm/GITS/labels/good%20first%20issue) open as a good place to get started from. You may work on these to help you get comfortable with the project to begin with. 

Also check out our [Phase 1 project board](https://github.com/arjunptm/GITS/projects/1) to get a good idea of where each process stands. 

Note that if you fork this project to work on it yourself, it won't automatically fork the issues/project boards. You can always come back here to refer to them, and then create a copy in your fork for the Phase 2 work.

### Installation Guidelines:

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

### Supported functionality

#### gits pr_update
This functionality makes sure that the current branch is able to make a PR without much trouble ( conflict ). It makes sure that the current branch has the latest commit off master branch, and that the local master has all the commits from the upstream master. This helps in reducing merge conflicts

#### gits profile
This functionality allows the user to change the git account quickly with a single command. There are situations when a developer has a personal github account and a enterprise github account as well. Changing between these accounts is a little complicated. This functionality aims to simplify it.

#### gits rebase 
This is a highly simplified version of git rebase command. This interactive command asks for the branch that you want to rebase and automatically rebases it off master. This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a confusion , about the source branch and the destination branch.  

#### gits reset
'Reset' intuitively means a HARD reset. This functionality does a HARD reset on your branch, and makes it even with the remote branch. This aims to simplify the confusion between HARD and the SOFT reset.  

#### gits set
This functionality sets the parent branch. 

#### gits upstream
This functionality changes the upstream with a single command. No need to manually remove the existing upstream, and adding a new upstream. This command will automatically change the upstream for the git repo. If there is any existing upstream , it will be overwritten.

#### gits super reset
Have you ever run into a situation, where you had to clone the repository again ? Yes, this functionality is exactly for that scenario. It will remove the current repository. It will clone it again, and add all the 'remote' to this freshly cloned repository. 

#### gits add 
Function that adds files as passed to the gits add command. Performs operation as similar to git add command.

#### gits mv 
Function that moves/renames a file, while maintaining the file history. Performs operation as similar to git mv command.

#### gits commit
It is a highly simplified version of git commit command. We are actively working on this functionality such that a commit would fail if the unit tests does not pass. We can specify the tests that need to pass before the commit can actually happen. 

#### gits create_branch
This automatically checks out a new branch from local master , after pulling all the changes from the remote master to local master. The idea behind this is that this new branch should have all the latest commits before a developer starts working on them.

#### gits all-branch
This command lists all the branches on both local and remote repositories.

#### gits remote-branch
This command lists all the branches on remote repository.

#### gits init
Function that creates an empty Git repository or re-initializes an existing one. There are three versions of this function, 
* `gits init --url='cloning url': Clones the repository at url at current directory`
* `gits init: This variant creates a repository with a working directory so you can actually work`
* `gits init --bare: This variant creates a repository without a working directory`

#### gits push
This pushes all the local changes of origin to the branch specified. 

#### gits checkout
This command switches between two branches. The function takes branch name as input and returns True for successful execution or False otherwise with an exception.

#### gits unstage
This command moves files from staging area to the working directory. These untracked files will not be considered for the upcoming commits. The function filenames as input to move from staging area to working directory and returns True for successful execution or False with an exception.

#### gits clone
This command clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository and creates and checks out an initial branch that is forked from the cloned repository’s currently active branch.

Note: More functionality are being added to this project. Please refer to the 'issues' tab for more information. In case you want to contribute to this project , please refer to 'Contributing.md' file.


### pydoc implementation
We have tried to write as much documentation as possible. You can use pydoc to go through the documentation. 
For example if you want to go through all the documentation for all files in code/ directory, do the following: 

`cd code`<br>
`python3 -m pydoc -b `

This will open up a browser and you can see all the files. You can click on a particular file to access the documentation associated with that file.

## Style Checker and Analyzer
We are using flake9 as our style checker and code analyzer. While contrivuting to this project, make sure you conform to norms dictated by flake8
### Flake8 
<b>Installation</b>
- `python<version> -m pip install flake8`

If you want Flake8 to be installed for your default Python installation, you can instead use:
- `python -m pip install flake8`

 <b>Using Flake8</b> 
 <br/>To start using Flake8, open an interactive shell and run one of the following,
- `flake8 path/to/code/to/check.py`
- `flake8 path/to/code/`

This repository is made for CSC 510 Software Engineering Course at NC State University.

Group 5 Team Members: 

* Rohan Prabhune
* Swetha Gavini
* Arjun Madhusudan
* Ramya Sai Mullapudi
* Krishna Saurabh
