#!/usr/bin/env python
"""
transcribe multiple files using open AI whisper and python subprocess
whisper utils/four-score.m4a --model large --language English """
import os
import click
import subprocess

# create a python function that returns files in a directory
def get_files(directory):
    """get files in a directory"""
    files = []
    for file in os.listdir(directory):
        files.append(file)
    return files


# find the size of all the files in a directory using subprocess and ls -lah
def get_size(directory):
    """get size of files in a directory"""
    filesize = subprocess.check_output(["ls", "-lah", directory])
    return filesize


# transcribe multiple files in a directory
def transcribe(directory, model, language):
    files = get_files(directory)
    for file in files:
        subprocess.run(
            [
                "whisper",
                f"{directory}/{file}",
                "--model",
                model,
                "--language",
                language,
            ],
            check=True,
        )


@click.group()
def cli():
    """transcribe multiple files using open AI whisper and python subprocess"""


# create a click command to transcribe multiple files
@cli.command("transcribe")
@click.option("--directory", default="utils", help="transcribe files in a directory")
@click.option("--model", default="tiny", help="model to use for transcribing")
@click.option("--language", default="English", help="language to use for transcribing")
def transcribe_cli(directory, model, language):
    """transcribe multiple files using open AI whisper and python
    example: whisper utils/four-score.m4a --model large --language English"""
    transcribe(directory, model, language)


# create a command that determines the size of all the files in a directory
@cli.command("size")
@click.option("--directory", default="utils", help="directory to find size of files")
def size(directory):
    """get size of files in a directory"""
    click.echo(get_size(directory))


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
