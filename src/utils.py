"""This module contains utility functions for the application."""
import json


def load_data():
    """Loads the data from the data.json file."""
    try:
        with open("data.json", "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        return {}


def update_data():
    """Update the data dictionary"""
    return load_data()
