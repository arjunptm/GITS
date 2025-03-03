#!/usr/bin/python3

from subprocess import Popen, PIPE


def gits_commit_func(args):
    """
    ###########################
    Function: gits_commit_func
    Description: Function that commit files as staged in the git command line interface
        Performs operation as similar to git commit command.
        Future additions : user can specify if the commit should be rejected , if the unit test fails for that file.
    Inputs:
         - Commit message (required)
         - amend message (optional)
    Outputs:
         - Returns false if there is any exception else true
    ###########################
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("commit")
        commit_message = args.m
        if not commit_message:
            print("ERROR: gits commit message not present, aborting")
            return False
        subprocess_command.append("-m")
        subprocess_command.append(commit_message)
        if not args.amend:
            # do nothing
            pass
        else:
            subprocess_command.append("--amend")

        # print(subprocess_command)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

    except Exception as e:
        print("ERROR: gits commit command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
