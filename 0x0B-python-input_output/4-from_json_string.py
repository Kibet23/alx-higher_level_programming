#!/usr/bin/python3
"""defines a JSON-to-Object function"""


import json


def from_json_string(my_str):
    """returns an Python data structure reprented by a JSON string"""

    return json.loads(my_str)
