#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: 
"""


from celery import Celery

celery = Celery('tasks', backend='redis://localhost',
        broker='amqp://guest@localhost//')

@celery.task
def add(x, y):
    return x + y
