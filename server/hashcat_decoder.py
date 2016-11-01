# -*- coding: utf-8 -*-
# @Time         : 16/10/21 下午10:03
# @Author       : Tao Xu
# @File         : hashcat_decoder.py
# @Software     : PyCharm
# @description  : 基于Hashcat破解Oracle和SAP方式的加密

import os

from lib.utils import (TOP_N, LESS_THAN_8, LENGTH_8_NUM, LENGTH_8_CHAR, LENGTH_8_SPECIAL, USER_CUSTOM, EASY_CRACK, STRONG)
from lib.utils import dboperator

class HashcatDecoder(object):
    def __init__(self):
        self.file_path_pre = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + '\\server\\hashcat_'

        self.dbo = dboperator()

    def decrypt_oracle_7_plus(self, datalist):
        sep = ':'
        hash_type = 3100    #Oracle 7+
        file_path = self.file_path_pre + 'oracle10\\'
        weak_en_list, weak_pl_list = self._decrypt(sep, hash_type, file_path, datalist)

        return weak_en_list, weak_pl_list

    def decrypt_oracle_11_plus(self, datalist):
        sep = ':'
        hash_type = 112    #Oracle 11+
        file_path = self.file_path_pre + 'oracle11\\'
        weak_en_list, weak_pl_list = self._decrypt(sep, hash_type, file_path, datalist)

        return weak_en_list, weak_pl_list


    def decrypt_sap_g(self, datalist):
        sep = '$'
        hash_type = 7800    #SAP G
        file_path = self.file_path_pre + 'sapg\\'
        weak_en_list, weak_pl_list = self._decrypt(sep, hash_type, file_path, datalist)

        return weak_en_list, weak_pl_list

    def decrypt_sap_b(self, datalist):
        sep = '$'
        hash_type = 7700    #SAP B
        file_path = self.file_path_pre + 'sapb\\'
        weak_en_list, weak_pl_list = self._decrypt(sep, hash_type, file_path, datalist)

        return weak_en_list, weak_pl_list

    def _decrypt(self, sep, hash_type, file_path, datalist):
        dict_file = 'dict'
        if self.is_64Windows():
            program = 'hashcat64.exe'
        else:
            program = 'hashcat32.exe'

        input_file_path = '%s%s' % (file_path, 'input.csv')
        with open(input_file_path, 'w') as f:
            lines = '\r\n'.join(datalist)
            f.writelines(lines)

        result_file_path = '%s%s' % (file_path, 'decrypt_result')
        '''
            -a 0:基于字典的破解
            -m %d: 不同的破解算法
            -p %s：分隔符
            --quiet: 命令行静默
            --remove: 将破解的从原始输入文件中移除
            -o %s: 待破解原始输入文件
            %s%s:字典路径
        '''
        cmd = '%s%s -a 0 -m %d -p %s --quiet --remove %s -o %s %s%s' % (file_path, program,
                        hash_type, sep, input_file_path, result_file_path, file_path, dict_file)
        os.system(cmd)

        #通过解析结果文件得到最终结果
        weak_en_list = []
        weak_pl_list = []
        if os.path.exists(result_file_path):
            with open(result_file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line:
                        passwd = line.split(sep)
                        weak_en_list.append('%s%s%s' % (passwd[0], sep, passwd[1]))
                        weak_pl_list.append(passwd[2])

        '''
        #删除该次生成结果文件时的缓存文件，以免影响下次生成结果文件
        '''
        return weak_en_list, weak_pl_list

    def is_64Windows(self):
        return 'PROGRAMFILES(X86)' in os.environ