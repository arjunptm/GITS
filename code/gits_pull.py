import gits_logging
from subprocess import Popen, PIPE


def gits_pull_func(args):
    """
    ###########################
    Function: gits_pull_func
    Description: Function to pull the latest content of a remote branch to local branch.
        Function similar to git pull command
    Inputs:
         - The branch you want to pull from
    Outputs:
         - Returns false if there is any exception else true
    ###########################
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("pull")

        print('Enter the branch you want to pull')
        branch = input()

        subprocess_command.append(branch)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
