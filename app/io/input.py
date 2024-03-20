import pandas

def enter():
    """
    Function gets en input from user and returns it
    :returns: a string object
    """
    prompt = input("Input: ")
    return prompt


def readfile(file_path):
    """
    Function reads a file and returns the contents of the file
    :arg: file_var: a file as an object. It does not accept file pathes
    :returns: a DataFrame object - a special Pandas data format
    """
    try:
        file = open(file_path)
        output = file.read()
        return output
    except FileNotFoundError:
        print("FileNotFoundError: Invalid name of file!")
        return None


def readfilepandas(file):
    """
    Function reads a file and returns the content
    using Pandas functionality
    :arg: file: a file as a path to the needed XML file
    :return: a string object
    """
    try:
        data_frame = pandas.read_table(file)
        return data_frame

    except FileNotFoundError:
        print("FileNotFoundError: Invalid name of file!")
        return None
