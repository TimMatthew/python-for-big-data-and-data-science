
from app.io.input import enter, readfile, readfilepandas
from app.io.output import printconsole, writefile, writefilepandas

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    print("---------------STRING READING AND PRINTING---------------")
    test_str = enter()
    printconsole(test_str)

    print("---------------FILE READING AND PRINTING---------------")
    test_str = readfile("data/test3.txt")
    printconsole(test_str)

    print("---------------PANDAS FILE READING AND PRINTING---------------")
    test_str = readfilepandas("data/test3.txt")
    printconsole(test_str)

    print("---------------FILE WRITING AND PRINTING---------------")
    writefile("data/test3.txt", "Some string...")
    test_str = readfile("data/test3.txt")
    printconsole(test_str)

    print("---------------PANDAS FILE WRITING AND PRINTING---------------")
    writefilepandas("data/test3.txt", "Some string...")
    test_str = readfilepandas("data/test3.txt")
    printconsole(test_str)

if __name__ == '__main__':
    main()


