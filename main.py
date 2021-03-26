#!/usr/bin/env python3

import click


class todo:
    def __init__(self, priority, text):
        self.priority = priority
        self.text = text

    def __lt__(self, other):
        if self.priority < other.priority:
            return True
        else:
            return False


class todos:
    def __init__(self):
        self.plan = []

    def list(self):
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
