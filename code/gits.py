#!/usr/bin/python3

import sys
import argparse
from gits_logging import init_gits_logger
from gits_hello import gits_hello_world
from gits_add import gits_add_func
from gits_mv import gits_mv_func
from gits_commit import gits_commit_func
from gits_set import gits_set_func
from gits_setupstream import upstream
from gits_create_branch import create_branch
from gits_super_reset import super_reset
from gits_push import gits_push_func
from gits_init import gits_init_func
from gits_all_branch import gits_all_branch_func
from gits_remote_branch import gits_remote_branch_func
from gits_checkout import checkout
from gits_rebase import gits_rebase
from gits_reset import gits_reset
from gits_unstage import unstage
from gits_profile import gits_set_profile
from gits_pr_update import gits_pr_update_func
from gits_status import gits_status
from gits_diff import gits_diff
from gits_sync import gits_sync
from gits_pull import gits_pull_func
from gits_clone import gits_clone_func
from gits_rm import gits_rm_func

logger_status = init_gits_logger()
if not logger_status:
    print("ERROR: logger not initialised")
    sys.exit(1)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

gits_hello_subparser = subparsers.add_parser('hello_world', help="To check if GITS is configured correctly")
gits_hello_subparser.set_defaults(func=gits_hello_world)

gits_set_subparser = subparsers.add_parser('set', help='To set important environment variables')
gits_set_subparser.add_argument('--parent', help='git parent branch')
gits_set_subparser.set_defaults(func=gits_set_func)

gits_add_subparser = subparsers.add_parser('add', help='Add files to the staging area')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='*',
                                help='all file names')
gits_add_subparser.set_defaults(func=gits_add_func)

gits_mv_subparser = subparsers.add_parser('move', help='Rename file without loosing history of the file')
gits_mv_subparser.add_argument('input_file',
                               type=str,
                               help='File to rename')
gits_mv_subparser.add_argument('output_file',
                               type=str,
                               help='New name of file')
gits_mv_subparser.set_defaults(func=gits_mv_func)

gits_rm_subparser = subparsers.add_parser('remove')
gits_rm_subparser.add_argument('input_file',
                               type=str,
                               help='File to remove')
gits_rm_subparser.set_defaults(func=gits_rm_func)

gits_commit_subparser = subparsers.add_parser('commit', help='commit changes added to the staging')
gits_commit_subparser.add_argument('-m',
                                   required=True,
                                   help='git commit message')
gits_commit_subparser.add_argument('--amend',
                                   action='store_true',
                                   help='amend commit message')
gits_commit_subparser.set_defaults(func=gits_commit_func)

gits_create_subparser = subparsers.add_parser('create', help='create new branch with latest changes from master')
gits_create_subparser.add_argument('-b', help="branch name to create")
gits_create_subparser.set_defaults(func=create_branch)

gits_upstream_subparser = subparsers.add_parser('upstream', help='Modify the upstream repository')
gits_upstream_subparser.add_argument('--remote',
                                     help='the remote branch name')
gits_upstream_subparser.add_argument('--local',
                                     help="local branch name")
gits_upstream_subparser.add_argument('--upstream',
                                     help="the upstream branch name")
gits_upstream_subparser.set_defaults(func=upstream)

gits_profile_subparser = subparsers.add_parser('profile',
                                               help='To change the git account quickly with a single command')
gits_profile_subparser.set_defaults(func=gits_set_profile)
gits_profile_subparser.add_argument('--email',
                                    required=True,
                                    help='email to be used')
gits_profile_subparser.add_argument('--name',
                                    required=True,
                                    help='name to be used')

gits_pr_subparser = subparsers.add_parser('sync', help='Helps to make a PR without many conflicts')
gits_pr_subparser.set_defaults(func=gits_pr_update_func)
gits_pr_subparser.add_argument('--upstream', nargs='?')

gits_super_reset_subparser = subparsers.add_parser('super-reset',
                                                   help='To remove local repo and freshly clone the same repository')
gits_super_reset_subparser.add_argument(
    '--name', help="Name of the repository to super reset")
gits_super_reset_subparser.set_defaults(func=super_reset)

gits_rb_subparser = subparsers.add_parser('rebase', help='Rebase a branch off the master')
gits_rb_subparser.set_defaults(func=gits_rebase)

gits_reset_subparser = subparsers.add_parser('reset', help='Hard reset a branch to match the remote')
gits_reset_subparser.set_defaults(func=gits_reset)
gits_reset_subparser.add_argument(
    '--branch', required=True, help='branch to be used')

gits_push_subparser = subparsers.add_parser('push', help='Push local commits to remote repository')
gits_push_subparser.set_defaults(func=gits_push_func)

gits_push_subparser = subparsers.add_parser('pull', help='Pulls latest changes from remote repository to local')
gits_push_subparser.set_defaults(func=gits_pull_func)

gits_add_subparser = subparsers.add_parser('checkout', help='Checkout a specified branch')
gits_add_subparser.add_argument('branch_name')
gits_add_subparser.set_defaults(func=checkout)

gits_add_subparser = subparsers.add_parser('clone', help='Clone a repository into a new directory')
gits_add_subparser.add_argument('site_url')
gits_add_subparser.set_defaults(func=gits_clone_func)

gits_add_subparser = subparsers.add_parser('unstage', help='To move files from staging area to the working directory')
gits_add_subparser.add_argument('file_names',
                                metavar='N',
                                type=str,
                                nargs='+',
                                help='all file names')
gits_add_subparser.set_defaults(func=unstage)

gits_status_subparser = subparsers.add_parser('status', help='Show the working tree status')
gits_status_subparser.set_defaults(func=gits_status)

gits_diff_subparser = subparsers.add_parser('diff', help='Show changes between commits, commit and working tree, etc')
gits_diff_subparser.set_defaults(func=gits_diff)

gits_sync_subparser = subparsers.add_parser('sync', help='To sync and rebase local master with remote master')
gits_sync_subparser.set_defaults(func=gits_sync)

gits_init_subparser = subparsers.add_parser(
    'init', help='Initialize local git repository')
gits_init_subparser.add_argument("--bare", action="store_true",
                                 help="Omit the working directory and initialize an empty git repository")
gits_init_subparser.add_argument(
    "--url", help="Url for cloning an already existing repo")
gits_init_subparser.set_defaults(func=gits_init_func)

gits_all_branch_subparser = subparsers.add_parser('all-branch', help='List all the branches')
gits_all_branch_subparser.set_defaults(func=gits_all_branch_func)

gits_remote_branch_subparser = subparsers.add_parser('remote-branch', help='list the branches in remote branch')
gits_remote_branch_subparser.set_defaults(func=gits_remote_branch_func)

args = parser.parse_args()
args.func(args)
