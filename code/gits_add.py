#!/usr/bin/python3


from subprocess import Popen, PIPE

import gits_logging


def gits_add_func(args):
    """
    ###########################
    Function: gits_add_func
    Description:  Function that adds files as passed to the gits add command.
    Performs operation as similar to git add command
    Inputs:
         - list of file names/paths to add to staging area
    Outputs:
         - Returns false if there is any exception else true
    ###########################
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("add")
        file_names_list = args.file_names
        total_files = len(file_names_list)
        if total_files == 0:
            subprocess_command.append(".")
        else:
            for i in range(0, total_files):
                subprocess_command.append(file_names_list[i])
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()

    except Exception as e:
        gits_logging.gits_logger.error("gits add command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits add command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
