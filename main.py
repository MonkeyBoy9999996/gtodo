#!/usr/bin/env python3

import click


@click.group()
def pytodo():
    '''CLI tool for TODO keeping'''
    pass


@pytodo.command()
def init():
    '''Re/Initialize TODO file'''


@pytodo.command()
def list():
    '''List available TODOs'''
    print()


@pytodo.command()
def add():
    '''Add TODO to list'''
    pass


@pytodo.command()
def delete():
    '''Delete TODO from list'''
    pass


@pytodo.command()
def change():
    '''Changes content of TODO'''
    pass


@pytodo.command()
def show():
    '''Show full TODO description'''
    pass


if __name__ == "__main__":
    pytodo()
