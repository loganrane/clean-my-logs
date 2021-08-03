import argparse


class Input():
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Clean Logs: A anamoly detection CLI tool'
        )

        parser.add_argumen(
            'file',
            default='-',
            type=str,
            nargs='*',
            help='File name (log file) to use. Default: stdin'
        )

        parser.add_argument(
            '-m',
            '--max-dist',
            default=0.55,
            type=float,
            help="""
            This controls how granular cluster should be.
            Lower value will generate more clusters. Default: 0.55
            """
        )

        parser.add_argument(
            '-p',
            '--placeholder',
            default='----',
            type=str,
            help="""
            Use a custom string as placeholder in output. Default: ----
            """
        )

        parser.add_argument(
            '-s',
            '--sorted',
            type=str,
            choices=['desc', 'asc'],
            help="""
            Sort the cluster on the count of members.
            Default: desc
            """
        )

        self.parser = parser

    def get_args(self):
        return vars(self.parser.parse_args())

    def print_help(self):
        return self.parser.print_help()