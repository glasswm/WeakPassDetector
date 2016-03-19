from lib.utils import dboperator
from lib.utils import fileoperator
import sys


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
            append_knowledge(temp_data_list, "topn")
        elif sys.argv[1] == "custom":
            temp_data_list = fo.read_list_from_file(sys.argv[2])
            append_knowledge(temp_data_list, "custom")
        elif sys.argv[1] == "length_less_then_8":
            temp_data_list = fo.read_list_from_file(sys.argv[2])
            append_knowledge(temp_data_list, "length_less_then_8")
        else:
            print_help()
    else:
        print_help()
