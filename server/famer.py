import threading
import time
from lib.utils import raintableoperator
from lib.utils import fileoperator
from lib.utils import dboperator
from hashcat_decoder import HashcatDecoder

def test_hash_type(data_list):
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letter_list_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_list_hig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                       'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    char_set = num_list + letter_list_low + letter_list_hig
    dbo = dboperator()
    is_md5 = True
    is_sha1 = True
    for data in data_list:
        if not dbo.string_all_in_set(data, char_set) or len(data) != 32:
            is_md5 = False
        if not dbo.string_all_in_set(data, char_set) or len(data) != 40:
            is_sha1 = False
    return is_md5, is_sha1


def ask_db(data_list, data_type):
    print 'askDB'
    dbo = dboperator()
    if data_type == "md5":
        return dbo.ask_md5table(data_list)
    elif data_type == "sha1":
        return dbo.ask_sha1table(data_list)
    elif data_type == "oracle10":
        return dbo.ask_decode_table('oracle10', 'oracle10table', data_list)
    elif data_type == "oracle11":
        return dbo.ask_decode_table('oracle11', 'oracle11table', data_list)
    elif data_type == "sapg":
        return dbo.ask_decode_table('sapg', 'sapgtable', data_list)
    elif data_type == 'spab':
        return dbo.ask_decode_table('sapb', 'sapbtable', data_list)
    elif data_type == "isc":
        return dbo.ask_isctable(data_list)
    else:
        return -1, -1, -1, -1


def digger(data_type, count):
    rto = raintableoperator()
    dbo = dboperator()
    fo = fileoperator()
    hd = HashcatDecoder()
    unknow_list = []
    if data_type == "md5":
        while 1:
            unknow_list = dbo.get_unknown_md5_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("md5 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("md5 digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = rto.ask_raintable(unknow_list, "md5")
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_md5table(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("md5 digger is waitting for work")
                print(" ")
                print("md5 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("md5 digger:hash list is: " + str(unknow_list))
                print("md5 digger:duang")
    elif data_type == "sha1":
        while 1:
            unknow_list = dbo.get_unknown_sha1_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("sha1 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("sha1 digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = rto.ask_raintable(unknow_list, "sha1")
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_sha1table(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("sha1 digger is waitting for work")
                print(" ")
                print("sha1 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("sha1 digger:hash list is: " + str(unknow_list))
                print("sha1 digger:duang")
    elif data_type == "oracle10":
        while 1:
            unknow_list = dbo.get_unknown_oracle10_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("oracle10 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("oracle10 digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = hd.decrypt_oracle_7_plus(unknow_list)
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_oracle10_table(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("oracle10 digger is waitting for work")
                print(" ")
                print("oracle10 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("oracle10 digger:hash list is: " + str(unknow_list))
                print("oracle10 digger:duang")
    elif data_type == "oracle11":
        while 1:
            unknow_list = dbo.get_unknown_oracle11_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("oracle11 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("oracle11 digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = hd.decrypt_oracle_11_plus(unknow_list)
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_oracle11_table(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("oracle11 digger is waitting for work")
                print(" ")
                print("oracle11 digger:get " + str(len(unknow_list)) + " hash to dig")
                print("oracle11 digger:hash list is: " + str(unknow_list))
                print("oracle11 digger:duang")
    elif data_type == "sapg":
        while 1:
            unknow_list = dbo.get_unknown_sapg_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("sapg digger:get " + str(len(unknow_list)) + " hash to dig")
                print("sapg digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = hd.decrypt_sap_g(unknow_list)
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_sapg_table(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("sapg digger is waitting for work")
                print(" ")
                print("sapg digger:get " + str(len(unknow_list)) + " hash to dig")
                print("sapg digger:hash list is: " + str(unknow_list))
                print("sapg digger:duang")
    elif data_type == "sapb":
        while 1:
            unknow_list = dbo.get_unknown_sapb_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("sapb digger:get " + str(len(unknow_list)) + " hash to dig")
                print("sapb digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = hd.decrypt_sap_b(unknow_list)
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_sapb_table(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("sapb digger is waitting for work")
                print(" ")
                print("sapb digger:get " + str(len(unknow_list)) + " hash to dig")
                print("sapb digger:hash list is: " + str(unknow_list))
                print("sapb digger:duang")
    elif data_type == "isc":
        while 1:
            unknow_list = dbo.get_unknown_isc_list(count)
            if len(unknow_list) > 0:
                print(" ")
                print("isc digger:get " + str(len(unknow_list)) + " hash to dig")
                print("isc digger:hash list is: " + str(unknow_list))
                weak_en_list, weak_pl_list = dbo.ask_iscknowledge(unknow_list)
                strong_en_list = set(unknow_list) - set(weak_en_list)
                dbo.refresh_isctable(weak_en_list, weak_pl_list, strong_en_list)
            else:
                time.sleep(10)
                fo.write_log("isc digger is waitting for work")
                print(" ")
                print("isc digger:get " + str(len(unknow_list)) + " hash to dig")
                print("isc digger:hash list is: " + str(unknow_list))
                print("isc digger:duang")
    else:
        fo.write_log("you input an unknow data_type in digger(data_type,count)")


def start_digger(data_type, count):
    brute_handler = threading.Thread(target=digger, args=(data_type, count))
    brute_handler.start()


if __name__ == "__main__":
    start_digger("md5", 5)
    start_digger("sha1", 5)
    start_digger("isc", 5)
