from subprocess import Popen, PIPE


def gits_status(args):
    """
    ###########################
    Function: gits_status
    Description: Function to display the state of the working directory and the staging area.
        This function is similar to the git status command.
    Inputs: None
    Outputs:
        - display the state of the working directory and the staging area
        - Returns false if there is any exception else true
    ###########################
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("status")
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        stdout = stdout.decode("utf-8")

        final = stdout.split("\n")
        final = list(filter(None, final))
        for f in final:
            print(f)

    except Exception as e:
        print("ERROR: gits status did not run correctly")
        print("ERROR: {}".format(str(e)))
        return False

    return True
