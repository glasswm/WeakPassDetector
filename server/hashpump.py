from lib.utils import dboperator
from lib.utils import fileoperator
import sys

TOP_N = 0
LESS_THAN_8 = 1
LENGTH_8_NUM = 2
LENGTH_8_CHAR = 3
LENGTH_8_SPECIAL = 4
USER_CUSTOM = 5

STRONG = 9


def print_help():
    print("help :")
    print("      hashpump.py -h")
    print("      hashpump.py topn filename")
    print("      hashpump.py custom filename")


def append_knowledge(data_list, note):
    dbo = dboperator()
    dbo.append_knowledge(data_list, note)


if __name__ == "__main__":
    fo = fileoperator()
    if len(sys.argv) == 1 or len(sys.argv) == 2:
        print_help()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "topn":
            temp_data_list = fo.read_list_from_file(sys.argv[2])
            append_knowledge(temp_data_list, TOP_N)
        elif sys.argv[1] == "custom":
            temp_data_list = fo.read_list_from_file(sys.argv[2])
            append_knowledge(temp_data_list, USER_CUSTOM)
        elif sys.argv[1] == "l8":
            temp_data_list = fo.read_list_from_file(sys.argv[2])
            append_knowledge(temp_data_list, LESS_THAN_8)
        else:
            print_help()
    else:
        print_help()
