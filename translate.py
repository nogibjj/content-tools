#!/usr/bin/env python
"""
build a python command line tool that translates a file full of words in english
"""
import click
import boto3

# build a function that translates using boto3
def translate_text(text, source, target):
    """translate text using boto3"""
    client = boto3.client("translate")
    response = client.translate_text(
        Text=text, SourceLanguageCode=source, TargetLanguageCode=target
    )
    return response["TranslatedText"]


# build a function that translates a file full of words in english
# chunk the file into 4900 bytes at a time
def translate_file(file, source, target):
    """translate a file full of words in english"""
    # open the file
    with open(file, "r", encoding="utf-8") as f:
        # read the file
        text = f.read()
        # chunk the file into 4900 bytes at a time
        chunks = [text[i : i + 4900] for i in range(0, len(text), 4900)]
        # translate the chunks
        translated_chunks = []
        for chunk in chunks:
            translated_chunks.append(
                translate_text(chunk, source=source, target=target)
            )
        # combine the translated chunks
        translated_text = "".join(translated_chunks)
        # write the translated text to a file
        with open(f"{file}.translated", "w", encoding="utf-8") as f:
            f.write(translated_text)


# build click tool to translate a file full of words in english
@click.group()
def cli():
    """translate a file full of words in english"""


# create a click command to translate a file full of words in english
@cli.command("translate")
@click.option("--file", default="utils/words.txt", help="file to translate")
@click.option("--source", default="en", help="source language")
@click.option("--target", default="es", help="target language")
def translate_cli(file, source, target):
    """translate a file full of words in english"""
    translate_file(file, source, target)


# invoke the cli
if __name__ == "__main__":
    cli()
