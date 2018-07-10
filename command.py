import argparse
import os
import pkgutil

if __name__ == '__main__':

    COMMANDS_DIRECTORY = 'commands'

    parser = argparse.ArgumentParser(description='Managing %s commands' % os.environ.get("PROJECT_NAME"))
    subparsers = parser.add_subparsers(help='sub commands')

    subcommands = []
    for _, command_name, _ in pkgutil.iter_modules([COMMANDS_DIRECTORY]):
        path = "%s.%s" % (COMMANDS_DIRECTORY, command_name)
        commands_import = __import__(path)
        subcommands.append(getattr(commands_import, command_name))

    for subcommand in subcommands:
        subcommand.parse_args(subparsers)

    args = parser.parse_args()

    args.func(args)

