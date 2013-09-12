#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Celery task definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from celery import task


@task()
def add(x, y):
    """
    Add 2 numbers
    """
    return x + y

@task()
def fail(x, y):
    """
    Simulates a task that raises an exception.
    """
    raise Exception('what?')
    return add(x, y)

# vim:ft=python ts=4 tw=80 cc=+1:
