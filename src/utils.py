"""This module contains utility functions for the application."""
import json

def load_data():
    try:
        with open("data.json") as json_file:
            data = json.load(json_file)
            return data
    except:
        return {}