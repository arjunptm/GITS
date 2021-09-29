
from subprocess import Popen, PIPE

def gits_rm_func(args):
    """
    Function to rename a file, but without losing the changelog/history
    of that file.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("rm")
        input_fname = args.input_file
        subprocess_command.append(input_fname)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
    except Exception as e:
        print("ERROR: gits rm command caught an exception")
        print("ERROR: {}".format(str(e)))