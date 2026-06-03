#!/usr/bin/python3
"""append file module"""

def append_write(filename="", text=""):
    """append file module"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))