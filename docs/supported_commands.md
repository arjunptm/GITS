### Supported functionality

#### gits add 
Function that adds files as passed to the gits add command. Performs operation as similar to git add command.

#### gits all-branch
This command lists all the branches on both local and remote repositories.

#### gits checkout
This command switches between two branches. The function takes branch name as input and returns True for successful execution or False otherwise with an exception.

#### gits clone
This command clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository and creates and checks out an initial branch that is forked from the cloned repository’s currently active branch.

Note: More functionality are being added to this project. Please refer to the 'issues' tab for more information. In case you want to contribute to this project , please refer to 'Contributing.md' file.

#### gits commit
It is a highly simplified version of git commit command. We are actively working on this functionality such that a commit would fail if the unit tests does not pass. We can specify the tests that need to pass before the commit can actually happen.

#### gits create_branch
This automatically checks out a new branch from local master , after pulling all the changes from the remote master to local master. The idea behind this is that this new branch should have all the latest commits before a developer starts working on them.

#### gits init
Function that creates an empty Git repository or re-initializes an existing one. There are three versions of this function, 
* `gits init --url='cloning url': Clones the repository at url at current directory`
* `gits init: This variant creates a repository with a working directory so you can actually work`
* `gits init --bare: This variant creates a repository without a working directory`

#### gits mv 
Function that moves/renames a file, while maintaining the file history. Performs operation as similar to git mv command.

#### gits profile
This functionality allows the user to change the git account quickly with a single command. There are situations when a developer has a personal github account and a enterprise github account as well. Changing between these accounts is a little complicated. This functionality aims to simplify it.

#### gits pull
This pulls the latest content of a remote branch to local branch.

#### gits push
This pushes all the local changes of origin to the branch specified. 

#### gits rebase 
This is a highly simplified version of git rebase command. This interactive command asks for the branch that you want to rebase and automatically rebases it off master. This is the most common scenario. The original GIT rebase command is a little un-intuitive and there is always a confusion , about the source branch and the destination branch. 

#### gits remote-branch
This command lists all the branches on remote repository.

#### gits reset
'Reset' intuitively means a HARD reset. This functionality does a HARD reset on your branch, and makes it even with the remote branch. This aims to simplify the confusion between HARD and the SOFT reset. 

#### gits remove
This command is used to remove individual files and to remove tracked files from the git index. Additionally, it can be used to remove files from both the staging index and the working directory.

#### gits set
This functionality sets the parent branch. 

#### gits upstream
This functionality changes the upstream with a single command. No need to manually remove the existing upstream, and adding a new upstream. This command will automatically change the upstream for the git repo. If there is any existing upstream , it will be overwritten.

#### gits super reset
Have you ever run into a situation, where you had to clone the repository again ? Yes, this functionality is exactly for that scenario. It will remove the current repository. It will clone it again, and add all the 'remote' to this freshly cloned repository. 

#### gits unstage
This command moves files from staging area to the working directory. These untracked files will not be considered for the upcoming commits. The function filenames as input to move from staging area to working directory and returns True for successful execution or False with an exception.