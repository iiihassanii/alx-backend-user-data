#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
    """
import re


def filter_datum(fields, redaction, message, separator):
    """_summary_

    Args:
        fields (_type_): _description_
        redaction (_type_): _description_
        message (_type_): _description_
        separator (_type_): _description_

    Returns:
        _type_: _description_
    """
    pattern = f"({'|'.join(fields)})=[^({separator})]*"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
