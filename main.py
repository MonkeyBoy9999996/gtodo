#!/usr/bin/env python3

import click
from os.path import exists
from sys import exit
import pickle


class todo:
    def __init__(self, priority, text):
        self.priority = int(priority)
        self.text = text

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        else:
            return False


class todos:
    def __init__(self):
        self.plan = []

    def __load(self):
        try:
            file = open("TODO.pytodo", 'rb')
        except FileNotFoundError:
            click.echo("No TODO file. Run pytodo init.")
            exit(1)
        obj = pickle.load(file)
        self.plan = obj.plan
        file.close()

    def __dump(self):
        file = open("TODO.pytodo", 'wb')
        pickle.dump(self, file)
        file.close()

    def __enter__(self):
        self.__load()
        return self

    def __exit__(self, exc_type, ecx_val, exc_tb):
        self.__dump()

    def list(self):
        if self.plan == []:
            print('empty')
            return
        for i, t in enumerate(self.plan, start=1):
            click.echo("[{}]: ".format(i), nl=False)
            if t.priority == 1:
                click.secho(t.text, fg='red')
            elif t.priority == 2:
                click.secho(t.text, fg='yellow')
            elif t.priority == 3:
                click.secho(t.text)
            elif t.priority == 4:
                click.secho(t.text, fg='blue')
            else:
                click.secho(t.text, fg='green')

    def add(self, todo):
        self.plan.append(todo)
        self.plan.sort()

    def delete(self, index):
        self.plan.pop(index - 1)


@click.group()
def pytodo():
    '''CLI tool for TODO keeping'''
    pass


@pytodo.command()
def init():
    '''Re/Initialize TODO file'''
    if exists("TODO.pytodo"):
        click.echo("Reinitializing TODO")
    else:
        click.echo("Initializing TODO")
    file = open("TODO.pytodo", 'wb')
    pickle.dump(todos(), file)
    file.close()


@pytodo.command()
def list():
    '''List available TODOs'''
    with todos() as td:
        td.list()


@pytodo.command()
@click.option("-p", "--priority",
              type=click.Choice(['1', '2', '3', '4', '5']), default='3')
@click.option("-t", "--text", multiple=True)
def add(priority, text):
    '''Add TODO to list'''
    with todos() as td:
        td.add(todo(priority, '\n'.join(text)))


@pytodo.command()
@click.argument('num', type=int, required=True)
def delete(num):
    '''Delete TODO from list'''
    with todos() as td:
        td.delete(num)
