from utils import fileoperator
from hashlib import *
import os

encryption_algorithm_md5 = 'md5'
encryption_algorithm_sha1 = 'sha1'


def md5_encode(plain_text):
    return md5(plain_text).hexdigest()


def sha1_encode(plain_text):
    return sha1(plain_text).hexdigest()


def encode_by_ea_list(plain_text, encryption_algorithm_list):
    temp_text = plain_text
    for encryption_algorithm in encryption_algorithm_list:
        if encryption_algorithm == encryption_algorithm_md5:
            temp_text = md5_encode(temp_text)
        elif encryption_algorithm == encryption_algorithm_sha1:
            temp_text = sha1_encode(temp_text)
        else:
            print("ERROR! UNKNOWN encryption_algorithm .")
    return temp_text


def get_dic_file_name_by_ea_list(encryption_algorithm_list):
    temp_filename = '../ammo/plain'
    for encryption_algorithm in encryption_algorithm_list:
        if encryption_algorithm == encryption_algorithm_md5:
            temp_filename = temp_filename + '-md5'
        elif encryption_algorithm == encryption_algorithm_sha1:
            temp_filename = temp_filename + '-sha1'
        else:
            pass
    temp_filename = temp_filename + '.txt'
    return temp_filename


def build_dic(encryption_algorithm_list):
    fo = fileoperator()
    plain_file_dir = '../ammo/plain.txt'
    plain_text_list = fo.read_list_from_file(plain_file_dir)

    dic_file_name = get_dic_file_name_by_ea_list(encryption_algorithm_list)
    dic_list = []
    for plain_text in plain_text_list:
        record_str = plain_text + ' ' + encode_by_ea_list(plain_text, encryption_algorithm_list)
        dic_list.append(record_str)
    fo.write_list_to_file(dic_list, dic_file_name)


def find_plain_text_from_dic(entext, dic_data_list):
    for dic_data in dic_data_list:
        elem = dic_data.split(' ')
        if entext == elem[1]:
            return elem[0]
        else:
            pass
    return -1


def read_dic(data_list, encryption_algorithm_list):
    dic_file_name = get_dic_file_name_by_ea_list(encryption_algorithm_list)
    fo = fileoperator()
    dic_data_list = fo.read_list_from_file(dic_file_name)

    weak_index_list = []
    weak_plain_text_list = []
    for i in range(0, len(data_list)):
        result = find_plain_text_from_dic(data_list[i], dic_data_list)
        if result != -1:
            weak_index_list.append(i)
            weak_plain_text_list.append(result)
        else:
            pass
    return weak_index_list, weak_plain_text_list


def brute_force_attack(data_list, encryption_algorithm_list):
    if os.path.exists(get_dic_file_name_by_ea_list(encryption_algorithm_list)):
        print("Match dic.")
        return read_dic(data_list, encryption_algorithm_list)
    else:
        print("Build dic.")
        build_dic(encryption_algorithm_list)
        return read_dic(data_list, encryption_algorithm_list)


def magic_test(username, en_str, encryption_algorithm_list):
    fo = fileoperator()
    magic_dic_file_name = '../ammo/magic.txt'
    magic_list = fo.read_list_from_file(magic_dic_file_name)
    for magic_str in magic_list:
        test_str = username + magic_str
        if en_str == encode_by_ea_list(test_str, encryption_algorithm_list):
            return test_str
        else:
            pass
    return -1


def magic_force_attack(user_name_list, en_list, encryption_algorithm_list):
    weak_index_list = []
    weak_plain_text_list = []
    if len(user_name_list) == len(en_list):
        for i in range(0, len(user_name_list)):
            result = magic_test(user_name_list[i], en_list[i], encryption_algorithm_list)
            if result != -1:
                weak_index_list.append(i)
                weak_plain_text_list.append(result)
            else:
                pass
    else:
        print("ERROR! length of user_name_list and en_list are not same.")
        return -1, -1
    return weak_index_list, weak_plain_text_list


if __name__ == '__main__':
    al = ['md5', 'md5', 'sha1']
    user_name_list = ['aa', 'bb', 'cc']
    print encode_by_ea_list('aa123', al)
    print encode_by_ea_list('bb1qaz2wsx', al)
    print encode_by_ea_list('cc+1234', al)
    en_list = ['69b6ad8333955876fbb52720506029e2d814be36', '3dd25a4f36fe4ddeb13a01616e79f4f6390ace08',
               '805c8964a1fbcb5513c27bd19a7177bfcbf49e1f']
    index_list, plain_list = magic_force_attack(user_name_list, en_list, al)
    print index_list
    print plain_list
