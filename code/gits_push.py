import gits_logging
from subprocess import Popen, PIPE


def gits_push_func(args):
    """
    ###########################
    Function: gits_push_func
    Description: Function to upload local repository content to a remote repository.
        Function similar to git push command.
    Inputs:
         - Branch name to push to
    Outputs:
         - Returns false if there is any exception else true
    ###########################
    """
    print('Welcome to gits push')
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("push")
        subprocess_command.append("origin")

        print('Enter the branch you want to push to')
        branch = input()

        subprocess_command.append(branch)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
