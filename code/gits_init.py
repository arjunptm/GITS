#!/usr/bin/python3
from subprocess import Popen, PIPE


def gits_init_func(args):
    """
    Function that creates an empty Git repository or re-initializes an existing one.
    This function is similar to git init command.
    """
    try:
        subprocess_command = list()
        if args.url:
            subprocess_command.append("git")
            subprocess_command.append("clone")
            subprocess_command.append(args.url)
        else:
            subprocess_command.append("git")
            subprocess_command.append("init")
            if args.bare is not False:
                subprocess_command.append("--bare")
        # print(subprocess_command)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stderr = stderr.decode("utf-8")
        print(stderr)

    except Exception as e:
        print("ERROR: gits init command caught an exception")

        print("ERROR: {}".format(str(e)))
        print("ERROR: {}".format(str(e)))
        return False

    return True
