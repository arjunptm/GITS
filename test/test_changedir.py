import os
"""
As code and test files are in different folders,
this test makes sure that the code files are accessible in test folder
"""
currpath = os.path.abspath(".")

if "code" not in currpath:
    if "test" in currpath:
        os.chdir(os.path.join("..", "code"))
    else:
        os.chdir("code")
