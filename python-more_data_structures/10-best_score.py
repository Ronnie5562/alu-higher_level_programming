#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and len(a_dictionary) > 0:
        return max(a_dictionary, key=a_dictionary.get)
    return None
