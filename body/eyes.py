import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_blue(text='', newline='\n', bold=False):

    if bold:
        sys.stdout.write(bcolors.BOLD + bcolors.OKBLUE + text + newline + bcolors.ENDC)
    else:
        sys.stdout.write(bcolors.OKBLUE + text + newline + bcolors.ENDC)


def print_green(text='', newline='\n', bold=False):

    if bold:
        sys.stdout.write(bcolors.BOLD + bcolors.OKGREEN + text + newline + bcolors.ENDC)
    else:
        sys.stdout.write(bcolors.OKGREEN + text + newline + bcolors.ENDC)


def print_header(text='', newline='\n', bold=False):

    if bold:
        sys.stdout.write(bcolors.BOLD + bcolors.HEADER + text + newline + bcolors.ENDC)
    else:
        sys.stdout.write(bcolors.HEADER + text + newline + bcolors.ENDC)


def print_fail(text='', newline='\n', bold=False):

    if bold:
        sys.stdout.write(bcolors.BOLD + bcolors.FAIL + text + newline + bcolors.ENDC)
    else:
        sys.stdout.write(bcolors.FAIL + text + newline + bcolors.ENDC)


def print_underline(text='', newline='\n', bold=False):

    if bold:
        sys.stdout.write(bcolors.BOLD + bcolors.UNDERLINE + text + newline + bcolors.ENDC)
    else:
        sys.stdout.write(bcolors.UNDERLINE + text + newline + bcolors.ENDC)


def print_warning(text='', newline='\n', bold=False):

    if bold:
        sys.stdout.write(bcolors.BOLD + bcolors.WARNING + text + newline + bcolors.ENDC)
    else:

        sys.stdout.write(bcolors.WARNING + text + newline + bcolors.ENDC)