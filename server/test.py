from lib.utils import raintableoperator
from lib.utils import fileoperator
from lib.utils import dboperator
import os

if __name__ == '__main__':

    dbo = dboperator()

    data_list = ["ac3478d69a3c81fa62e60f5c3696165a4e5e6ac4","aaaa","aaaaaa","sssssss"]

    weak_list,weak_type_list,strong_list,len_of_unknownList = dbo.ask_sha1table(data_list)

    print weak_list
    print weak_type_list
    print strong_list
    print len_of_unknownList
