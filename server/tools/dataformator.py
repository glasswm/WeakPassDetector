def string_all_in_set(test_str, test_set):
    for s in test_str:
        if s in test_set:
            pass
        else:
            return False
    return True


def get_weak_type(weak_pl):
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
        return "length_less_then_8"
    elif length == 8:
        if string_all_in_set(weak_pl, num_list):
            return "8_length_numeric"
        elif string_all_in_set(weak_pl, letter_list):
            return "8_length_character"
        elif string_all_in_set(weak_pl, xxx_list):
            return "8_length_special_character"
        else:
            return "8_length_mix_type"
    else:
        return "it_is_strong"


def append_record_to_file(file_name, input_data):
    f = open(file_name, "a")
    try:
        f.write(input_data + "\n")
    finally:
        f.close()


if __name__ == '__main__':
    file_name = "csdn"
    f = open(file_name, "r")
    try:
        line = f.readline()
        while line:
            passwd_str = line.split(" # ")
            if len(passwd_str) > 1:
                format_data = passwd_str[1].replace("\"", "").replace("\'", "").replace("-", "").replace(",",
                                                                                                         "").replace(
                    "\r", "").replace("\n", "")
                weak_type = get_weak_type(format_data)
                append_record_to_file(weak_type, format_data)
            line = f.readline()
    finally:
        f.close()
