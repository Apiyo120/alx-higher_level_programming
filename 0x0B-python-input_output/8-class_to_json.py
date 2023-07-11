#!/usr/bin/python3
"""Defines python class-to-JSON function."""


def class_to_json(obj):
    """It returns the dctionary representation of simple data structure."""
    return obj.__dict__
