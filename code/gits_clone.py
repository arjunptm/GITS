from subprocess import Popen, PIPE


def gits_clone_func(args):
    """
    Function to target an existing repository and create a clone, or copy of the target repository.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("clone")
        site_url = args.site_url

        if len(site_url) == 0:
            pass
        else:
            subprocess_command.append(site_url)
        process = Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
    except Exception as e:
        print("ERROR: gits clone command caught an exception")
        print("ERROR: {}".format(str(e)))
