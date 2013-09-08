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
