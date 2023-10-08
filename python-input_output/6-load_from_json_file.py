#!/usr/bin/python3
"""
    Module to create an object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
        Function
    """

    with open(filename, encoding="utf-8") as f:
        """open"""
        return (json.loads(f.read()))
