import os
import sys
sys.path.insert(1, os.getcwd())
import argparse
from code import gits_diff, gits_logging
from mock import patch, Mock


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen", return_value="anything")

def test_gits_diff(mock_var, mock_args):
    """
    Function to test gits_diff, success case
    """

    test_result = gits_diff.gits_diff(mock_args)
    assert True == test_result, "Normal case"
