#!/usr/bin/python3

from subprocess import Popen, PIPE


def gits_remote_branch_func(args):
    """
    ###########################
    Function: gits_remote_branch_func
    Description: Function to list the branches in remote branch
        Performs operation as similar to git branch -r command
    Inputs: None
    Outputs:
        - display the list of all branches in the remote repo
        - Returns false if there is any exception else true
    ###########################
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("branch")
        subprocess_command.append("-r")
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        # print(stdout)
        stdout = stdout.decode("utf-8")

        branches = list(filter(None, stdout.split("\n")))
        for branch in branches:
            print(branch)

    except Exception as e:
        print("ERROR: gits branch command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
