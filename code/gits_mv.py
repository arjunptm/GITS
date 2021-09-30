import gits_logging
from subprocess import Popen, PIPE


def gits_mv_func(args):
    """
    Function to rename a file, but without losing the changelog/history
    of that file.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("mv")
        input_fname = args.input_file
        output_fname = args.output_file
        subprocess_command.append(input_fname)
        subprocess_command.append(output_fname)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
    except Exception as e:
        print("ERROR: gits mv command caught an exception")
        print("ERROR: {}".format(str(e)))
