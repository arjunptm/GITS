## Functionalities Simplified
--- 
### gits pr_update
This functionality makes sure that the current branch is able to make a PR without much trouble ( conflict ). It makes sure that the current branch has the latest commit off master branch, and that the local master has all the commits from the upstream master. This helps in reducing merge conflicts

`gits sync`

### gits create_branch
This automatically checks out a new branch from local master , after pulling all the changes from the remote master to local master. The idea behind this is that this new branch should have all the latest commits before a developer starts working on them.

`gits create -b <Branch name to create>`

### gits init
Function that creates an empty Git repository or re-initializes an existing one. There are three versions of this function, 
* `gits init --url <cloning url>` : Clones the repository at url at current directory
* `gits init` : This variant creates a repository with a working directory so you can actually work
* `gits init --bare` : This variant creates a repository without a working directory

### gits profile
This functionality allows the user to change the git account quickly with a single command. There are situations when a developer has a personal github account and a enterprise github account as well. Changing between these accounts is a little complicated. This functionality aims to simplify it.

`gits profile --email <EMAIL> --name <NAME>`

### gits rebase 
This is a highly simplified version of git rebase command. This interactive command asks for the branch that you want to rebase and automatically rebases it off master. This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a confusion , about the source branch and the destination branch. 

`gits rebase`

### gits upstream
This functionality changes the upstream with a single command. No need to manually remove the existing upstream, and adding a new upstream. This command will automatically change the upstream for the git repo. If there is any existing upstream , it will be overwritten.

`gits upstream [--remote <REMOTE>] [--local <LOCAL>] [--upstream <UPSTREAM>]`

### gits super reset
Have you ever run into a situation, where you had to clone the repository again ? Yes, this functionality is exactly for that scenario. It will remove the current repository. It will clone it again, and add all the 'remote' to this freshly cloned repository. 

`gits super-reset --name <name of the git repository>`

### gits sync
This function returns the trunk branch

`gits sync`

## Basic Git functionalities supported
--- 

### gits add 
Function that adds files as passed to the gits add command. Performs operation as similar to git add command.
<br />To add all files changed/ added/ deleted in the current directory and sub-directories to the staging area. 
<br />Specify the list of files to add as an argument 

`gits add` : adds all the files.
<br />`gits add <list of file names to add>` : adds only the files mentioned

### gits all-branch
This command lists all the branches on both local and remote repositories.

`gits all-branch`

### gits checkout
This command switches between two branches. The function takes branch name as input and returns True for successful execution or False otherwise with an exception.

`gits checkout <branch-name>`

### gits clone
This command clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository and creates and checks out an initial branch that is forked from the cloned repository’s currently active branch.

`gits clone <site_url>`

### gits commit
It is a highly simplified version of git commit command. We are actively working on this functionality such that a commit would fail if the unit tests does not pass. We can specify the tests that need to pass before the commit can actually happen.

`gits commit -m <commit message> [--amend <amend message>]`

### gits diff
This is a function to analyze the current state of a Git repo. It shows difference commits, branches, files and more. 

`gits diff`

### gits logging
This function initializes gits logger and creates handler to be used consequently

### gits mv 
Function that moves/renames a file, while maintaining the file history. Performs operation as similar to git mv command.

`gits move <input_file> <output_file>`

### gits pull
This pulls the latest content of a remote branch to local branch.

`gits pull`
### gits push
This pushes all the local changes of origin to the branch specified. 

`gits push`

### gits remote-branch
This command lists all the branches on remote repository.

`gits remote-branch`
### gits reset
'Reset' intuitively means a HARD reset. This functionality does a HARD reset on your branch, and makes it even with the remote branch. This aims to simplify the confusion between HARD and the SOFT reset. 

`gits reset --branch <branch name to reset>`
### gits remove
This command is used to remove individual files and to remove tracked files from the git index. Additionally, it can be used to remove files from both the staging index and the working directory.

`gits remove <file_name>`
### gits set
This functionality sets the parent branch. 

### gits status
This function displays the state of the working directory and the staging area

`gits status`

### gits unstage
This command moves files from staging area to the working directory. These untracked files will not be considered for the upcoming commits. The function filenames as input to move from staging area to working directory and returns True for successful execution or False with an exception.

`gits unstage <file names to unstage>`


---
Note: More functionality are being added to this project. Please refer to the 'issues' tab for more information. In case you want to contribute to this project , please refer to 'Contributing.md' file.