#!/usr/bin/python3

from subprocess import Popen, PIPE


def create_branch(args):
    """
    ###########################
    Function: create_branch
    Description: Function that creates a new local branch from local master after updating local master from remote master.
        The idea here is that the new branch should have all the latest commits.
    Inputs:
         - Branch name to create
    Outputs:
         - Returns false if there is any exception else true
    ###########################
    """
    try:
        # checkout master first
        checkout_master = list()
        checkout_master.append("git")
        checkout_master.append("checkout")
        checkout_master.append("master")
        process1 = Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()

        # update with remote
        update_master = list()
        update_master.append("git")
        update_master.append("pull")
        process2 = Popen(update_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process2.communicate()

        # checkout new branch
        if not args.b:
            print("Name of new branch not provided. Use -b branchName")
            return False
        checkout_feature = list()
        checkout_feature.append("git")
        checkout_feature.append("checkout")
        checkout_feature.append("-b")
        checkout_feature.append(args.b)
        process3 = Popen(checkout_feature, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()

        process1 = Popen(checkout_master, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
    except Exception as e:
        print("ERROR: gits create command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
