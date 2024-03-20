import pandas


def printconsole(str):
    """
    Function prints str string to the console
    :arg: str - user input
    """
    print(str)


def writefile(file_path, content):
    """
    Function records a content to the file
    :arg:
    file - file to record/rewrite
    content - str as content to be recorded/rewritten
    """
    try:
        file = open(file_path, 'a')
        file.write(content)
    except FileNotFoundError:
        print("Invalid name of file!")

def writefilepandas(file, content):
    """
    Function records a content to the file
    using Pandas functionality
    :arg:
    file - path of file to record/rewrite
    content - content to be recorded/rewritten
    """
    try:
        data_frame = pandas.read_table(file, header=None, names=['Content'])
        data_frame = data_frame._append({'Content': content}, ignore_index=True)
        data_frame.to_csv(file, sep='\t', index=False, header=None, mode='w')
    except FileNotFoundError:
        print("Invalid name of file!")
