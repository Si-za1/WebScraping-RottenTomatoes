import os

def ls(path):
    return [f"{path}/{file}" for file in os.listdir(path)]


def read_file(path):
    with open(path, 'r') as f:
        query = f.read()
    return query
