#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Using task definition in an example.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from tasks import add

result = add.delay(4, 4)  # putting in queue for async processing
result.ready()  # checks if task was processed
result.get(timeout=1)  # gets task result
