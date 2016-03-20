import os
import time
import psycopg2
import hashlib
from server.__setting__ import LESS_THAN_8, STRONG, LENGTH_8_SPECIAL, LENGTH_8_CHAR, LENGTH_8_NUM


class fileoperator:
    def get_data_str(self):
        dataStr = time.strftime("%Y-%m-%d", time.localtime())
        return dataStr

    def get_time_str(self):
        timeStr = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime())
        return timeStr

    def read_list_from_file(self, file_name):
        f = open(file_name, "r")
        try:
            fData = f.readlines()
            for i in range(0, len(fData)):
                fData[i] = fData[i].replace("\r", "").replace("\n", "")
        finally:
            f.close()
        return fData

    def append_list_to_file(self, file_name, input_list):
        f = open(file_name, "a")
        try:
            for line in input_list:
                f.write(line + "\n")
        finally:
            f.close()

    def append_record_to_file(self, file_name, input_data):
        f = open(file_name, "a")
        try:
            f.write(input_data + "\n")
        finally:
            f.close()

    def write_list_to_file(self, data_list, file_name):
        f = open(file_name, 'w')
        try:
            for data in data_list:
                f.write(data + "\r\n")
        finally:
            f.close()

    def write_log(self, log_data):
        log_file_name = os.path.dirname(__file__) + "/../log/runtimelog_" + self.get_data_str() + ".log"
        log_data_with_time = self.get_time_str() + log_data
        self.append_record_to_file(log_file_name, log_data_with_time)


class dboperator:
    cur = 0
    conn = 0
    fo = fileoperator()

    def __init__(self):
        self.conn = psycopg2.connect(database="hashdb", user="postgres", password="1qaz2wsx", host="127.0.0.1",
                                     port="5432")
        self.cur = self.conn.cursor()

    def append_knowledge(self, data_list, note):
        for data in data_list:
            temp_data = data.replace("\'", "")
            md5_str = hashlib.md5(temp_data).hexdigest()
            sha1_str = hashlib.sha1(temp_data).hexdigest()
            if self.is_in_md5table(md5_str):
                update_md5_knowledge_sql = "update md5table set isweak='y',updatetime=current_date,weaktype=" + str(note) + ",text=\'" + temp_data + "\' where md5=\'" + md5_str + "\'"
                print(update_md5_knowledge_sql)
                self.cur.execute(update_md5_knowledge_sql)
                self.fo.write_log("excute:" + update_md5_knowledge_sql)
                print(update_md5_knowledge_sql)
                self.conn.commit()
                self.fo.write_log("excute:commit")
            else:
                append_md5_knowledge_sql = "insert into md5table values(\'" + md5_str + "\','y',current_date," + str(note) + ",\'" + temp_data + "\')"
                self.cur.execute(append_md5_knowledge_sql)
                self.fo.write_log("excute:" + append_md5_knowledge_sql)
                print(append_md5_knowledge_sql)
                self.conn.commit()
                self.fo.write_log("excute:commit")
            if self.is_in_sha1table(sha1_str):
                update_sha1_knowledge_sql = "update sha1table set isweak='y',updatetime=current_date,weaktype=" + str(note) + ",text=\'" + temp_data + "\' where sha1=\'" + sha1_str + "\'"
                self.cur.execute(update_sha1_knowledge_sql)
                self.fo.write_log("excute:" + update_sha1_knowledge_sql)
                print(update_sha1_knowledge_sql)
                self.conn.commit()
                self.fo.write_log("excute:commit")
            else:
                append_sha1_knowledge_sql = "insert into sha1table values(\'" + sha1_str + "\','y',current_date," + str(note) + ",\'" + temp_data + "\')"
                self.cur.execute(append_sha1_knowledge_sql)
                self.fo.write_log("excute:" + append_sha1_knowledge_sql)
                print(append_sha1_knowledge_sql)
                self.conn.commit()
                self.fo.write_log("excute:commit")

    def is_in_md5table(self, md5_str):
        sql = "select count(*) from md5table where md5= \'" + md5_str.lower() + "\'"
        self.cur.execute(sql)
        resultSet = self.cur.fetchall()
        result = resultSet[0][0]
        if result > 0:
            self.fo.write_log(md5_str.lower() + " is in md5table")
            return True
        else:
            self.fo.write_log(md5_str.lower() + " is not in md5table")
            return False

    def is_in_sha1table(self, sha1_str):
        sql = "select count(*) from sha1table where sha1= \'" + sha1_str.lower() + "\'"
        self.cur.execute(sql)
        resultSet = self.cur.fetchall()
        result = resultSet[0][0]
        if result > 0:
            self.fo.write_log(sha1_str.lower() + " is in sha1table")
            return True
        else:
            self.fo.write_log(sha1_str.lower() + " is in sha1table")
            return False

    def append_record_to_md5table(self, md5_str):
        sql = "insert into md5table values('" + md5_str.lower() + "','u',current_date,-1,'')"
        self.cur.execute(sql)
        self.fo.write_log("excute:" + sql)
        print(sql)
        self.conn.commit()
        self.fo.write_log("excute:commit")

    def append_record_to_sha1table(self, sha1_str):
        sql = "insert into sha1table values('" + sha1_str.lower() + "','u',current_date,-1,'')"
        self.cur.execute(sql)
        self.fo.write_log("excute:" + sql)
        print(sql)
        self.conn.commit()
        self.fo.write_log("excute:commit")

    def get_unknown_md5_list(self, count):
        data_list = []
        sql = "select md5 from md5table where isweak='u' limit " + str(count)
        self.cur.execute(sql)
        result_set = self.cur.fetchall()
        for result in result_set:
            data_list.append(result[0])
        self.fo.write_log("get " + str(len(data_list)) + " unknown md5 hash")
        return data_list

    def get_unknown_sha1_list(self, count):
        data_list = []
        sql = "select sha1 from sha1table where isweak='u' limit " + str(count)
        self.cur.execute(sql)
        result_set = self.cur.fetchall()
        for result in result_set:
            data_list.append(result[0])
        self.fo.write_log("get " + str(len(data_list)) + " unknown sha1 hash")
        return data_list

    def string_all_in_set(self, test_str, test_set):
        for s in test_str:
            if s in test_set:
                pass
            else:
                return False
        return True

    def get_weak_type(self, weak_pl):
        num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        letter_list_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        letter_list_hig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letter_list = letter_list_low + letter_list_hig
        xxx_list = [' ', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}',
                    '\\', '|', ';', ':', '\'', '\"', ',', '<', '.', '>', '/', '?']
        length = len(weak_pl)
        if length < 8:
            return LESS_THAN_8
        elif length == 8:
            if self.string_all_in_set(weak_pl, num_list):
                return LENGTH_8_NUM
            elif self.string_all_in_set(weak_pl, letter_list):
                return LENGTH_8_CHAR
            elif self.string_all_in_set(weak_pl, xxx_list):
                return LENGTH_8_SPECIAL
            else:
                return STRONG
        else:
            return STRONG

    def refresh_md5table(self, weak_en_list, weak_pl_list, strong_en_list):
        if len(weak_en_list) != len(weak_pl_list):
            self.fo.write_log("the length of weak_en_list and weak_pl_list is not equal")
            return
        for i in range(0, len(weak_en_list)):
            weak_type = self.get_weak_type(weak_pl_list[i])
            sql = "update md5table set isweak='y',updatetime=current_date,weaktype=" + str(weak_type) + ",text=\'" + \
                  weak_pl_list[i] + "\' where md5='" + weak_en_list[i] + "'"
            print(sql)
            self.cur.execute(sql)
            self.fo.write_log("excute:" + sql)
            self.conn.commit()
            self.fo.write_log("excute:commit")
        for strong in strong_en_list:
            sql = "update md5table set isweak='n',updatetime=current_date where md5='" + strong + "'"
            print(sql)
            self.cur.execute(sql)
            self.fo.write_log("excute:" + sql)
            self.conn.commit()
            self.fo.write_log("excute:commit")

    def refresh_sha1table(self, weak_en_list, weak_pl_list, strong_en_list):
        if len(weak_en_list) != len(weak_pl_list):
            self.fo.write_log("the length of weak_en_list and weak_pl_list is not equal")
            return
        for i in range(0, len(weak_en_list)):
            weak_type = self.get_weak_type(weak_pl_list[i])
            sql = "update sha1table set isweak='y',updatetime=current_date,weaktype=" + str(weak_type) + ",text=\'" + \
                  weak_pl_list[i] + "\' where sha1='" + weak_en_list[i] + "'"
            print(sql)
            self.cur.execute(sql)
            self.fo.write_log("excute:" + sql)
            self.conn.commit()
            self.fo.write_log("excute:commit")
        for strong in strong_en_list:
            sql = "update sha1table set isweak='n',updatetime=current_date where sha1='" + strong + "'"
            print(sql)
            self.cur.execute(sql)
            self.fo.write_log("excute:" + sql)
            self.conn.commit()
            self.fo.write_log("excute:commit")

    def ask_md5table(self, data_list):
        weak_list = []
        weak_type_list = []
        strong_list = []
        unknown_list = []
        for i in range(0, len(data_list)):
            sql = "select isweak,weaktype from md5table where md5='" + data_list[i] + "'"
            self.cur.execute(sql)
            resultSet = self.cur.fetchall()
            if len(resultSet) > 0:
                isweak = resultSet[0][0]
                weak_type = resultSet[0][1]
                print(weak_type)
                if isweak == 'y':
                    weak_list.append(i)
                    weak_type_list.append(weak_type)
                elif isweak == 'n':
                    strong_list.append(i)
                else:
                    unknown_list.append(i)
            else:
                unknown_list.append(i)
                self.append_record_to_md5table(data_list[i])
        return weak_list, weak_type_list, strong_list, len(unknown_list)

    def ask_sha1table(self, data_list):
        weak_list = []
        weak_type_list = []
        strong_list = []
        unknown_list = []
        for i in range(0, len(data_list)):
            sql = "select isweak,weaktype from sha1table where sha1='" + data_list[i] + "'"
            self.cur.execute(sql)
            resultSet = self.cur.fetchall()
            if len(resultSet) > 0:
                isweak = resultSet[0][0]
                weak_type = resultSet[0][1]
                print(weak_type)
                if isweak == 'y':
                    weak_list.append(i)
                    weak_type_list.append(weak_type)
                elif isweak == 'n':
                    strong_list.append(i)
                else:
                    unknown_list.append(i)
            else:
                unknown_list.append(i)
                self.append_record_to_sha1table(data_list[i])
        return weak_list, weak_type_list, strong_list, len(unknown_list)


class raintableoperator:
    md5_file_name = ""
    sha1_file_name = ""
    bin_file_name = ""
    fo = fileoperator()

    def __init__(self):
        self.md5_file_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/dic/md5*"
        self.sha1_file_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/dic/sha1*"
        self.bin_file_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/bin/digdata"

    def get_md5_dig_command(self):
        command_line_str = self.bin_file_name + " " + self.md5_file_name + " -l /tmp/temp_data_of_md5_dig.data" + "|grep \"plaintext of\" "
        return command_line_str

    def get_sha1_dig_command(self):
        command_line_str = self.bin_file_name + " " + self.sha1_file_name + " -l /tmp/temp_data_of_sha1_dig.data" + "|grep \"plaintext of\" "
        return command_line_str

    def ask_raintable(self, data_list, hash_type):
        weak_en_list = []
        weak_pl_list = []
        md5_temp_data_file_name = "/tmp/temp_data_of_md5_dig.data"
        sha1_temp_data_file_name = "/tmp/temp_data_of_sha1_dig.data"
        if hash_type == "md5":
            self.fo.write_list_to_file(data_list, md5_temp_data_file_name)
            cmd_str = self.get_md5_dig_command()
            self.fo.write_log("excete:" + cmd_str)
            result_list = os.popen(cmd_str).readlines()
            self.fo.write_log("result_list:" + str(result_list))
            for record in result_list:
                elements = record.split(" ")
                weak_en_list.append(elements[2])
                weak_pl_list.append(elements[4].replace("\n", ""))
        elif hash_type == "sha1":
            self.fo.write_list_to_file(data_list, sha1_temp_data_file_name)
            cmd_str = self.get_sha1_dig_command()
            self.fo.write_log("excete:" + cmd_str)
            result_list = os.popen(cmd_str).readlines()
            self.fo.write_log("result_list:" + str(result_list))
            for record in result_list:
                elements = record.split(" ")
                weak_en_list.append(elements[2])
                weak_pl_list.append(elements[4].replace("\n", ""))
        else:
            self.fo.write_log("you input an unknown hash_type in ask_rain_table(self,data_list,hash_type)")
        return weak_en_list, weak_pl_list


if __name__ == '__main__':
    pass
