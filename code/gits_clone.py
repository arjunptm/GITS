from subprocess import Popen, PIPE


def gits_clone_func(args):
    """
    ###########################
    Function: gits_clone_func
    Description: Function to target an existing repository and create a clone, or copy of the target repository.
    Inputs:
         - The site url to clone from
    Outputs:
         - Returns false if there is any exception else true
    ###########################
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("clone")
        siteurl = args.site_url

        if len(siteurl) == 0:
            pass
        else:
            subprocess_command.append(siteurl)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
    except Exception as e:
        print("ERROR: gits clone command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True