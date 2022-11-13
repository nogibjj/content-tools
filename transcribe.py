#!/usr/bin/env python
"""
transcribe multiple files using open AI whisper and python subprocess
whisper utils/four-score.m4a --model large --language English """
import os
import click

# create a python function that returns files in a directory
def get_files(directory):
    """get files in a directory"""
    files = []
    for file in os.listdir(directory):
        if file.endswith(".m4a"):
            files.append(file)
    return files

    # create click group


@click.group()
def cli():
    """transcribe multiple files using open AI whisper and python subprocess"""


# create a command that finds files in a directory
@cli.command("find")
@click.option("--directory", default="utils", help="directory to find files")
def find_files(directory):
    """find files in a directory"""
    files = get_files(directory)
    for file in files:
        print(file)


# invoke the command
if __name__ == "__main__":
    cli()
