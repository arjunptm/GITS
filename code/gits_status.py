from subprocess import Popen, PIPE

def gits_status(args):
	"""
	Function to display the state of the working directory and the staging area.
	This function is similar to the git status command.
	"""
	print("Welcome to gits status")
	try:
		subprocess_command = list()
		subprocess_command.append("git")
		subprocess_command.append("status")
		process=Popen(subprocess_command, stdout=PIPE, stderr=PIPE)
		stdout,stderr=process.communicate()
		stdout=stdout.decode("utf-8")

		final=stdout.split("\n")
		final = list(filter(None, final)) 
		for f in final:
			print(f)

	except Exception as e:
		print("ERROR: gits status did not run correctly")
		print("ERROR: {}".format(str(e)))
		return False
	
	return True