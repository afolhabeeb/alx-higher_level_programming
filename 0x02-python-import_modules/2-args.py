#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    arg_count = len(sys.argv) - 1

    if arg_count == 0:
        print("0 arguments.")
    
    elif arg_count == 1:
        print("1 arguments:")

    else:
        print("{} arguments:".format(arg_count))
    for dig in range(arg_count):
        print("{}: {}".format(dig + 1, sys.argv[dig + 1]))
