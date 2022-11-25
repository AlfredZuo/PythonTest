def check_next_type(input_list: []) -> bool:
    if input_list[0] == 4 and len(input_list) >= 4 and \
            input_list[1] == 1 and input_list[2] == 1 and \
            input_list[3] == 1:
        return True
    elif input_list[0] == 3 and len(input_list) >= 3 and \
            input_list[1] == 1 and input_list[2] == 1:
        return True
    elif input_list[0] == 2 and len(input_list) >= 2 and \
            input_list[1] == 1:
        return True
    elif input_list[0] == 0 and len(input_list) >= 1:
        return True
    else:
        return False


def check_list_type(input_list: []) -> int:
    if input_list[0] == 0:
        return 0
    elif input_list[0] == 1:
        count_one = 0
        for n in range(5):
            if input_list[n] != 0:
                count_one += 1
            else:
                break
        print(count_one)
        return count_one


class Solution:
    def validUtf8(self, data: [int]) -> bool:
        data_long = len(data)
        need_check_list = [[] * 8] * data_long
        # 首先要将队列中的数据变为二进制，注意需要加前导的零
        for i in range(data_long):
            j = 0
            temp_list = []
            while data[i] != 0:
                temp_list.append(data[i] % 2)
                data[i] //= 2
                j += 1
                if j >= 8:
                    break
            need_check_list[i] = temp_list
            # 补齐前导的零
            orig_len = len(need_check_list[i])
            if orig_len < 8:
                for k in range(orig_len, 8):
                    need_check_list[i].append(0)
            need_check_list[i].reverse()
            print(need_check_list[i], len(need_check_list[i]))
        print(need_check_list, len(need_check_list))

        need_check_list_type = []
        for i in range(len(need_check_list)):
            need_check_list_type.append(
                check_list_type(need_check_list[i]))
        print(need_check_list_type)

        while len(need_check_list_type) != 0:
            if check_next_type(need_check_list_type):
                if need_check_list_type[0] > 0:
                    for i in range(need_check_list_type[0]):
                        need_check_list_type.pop(0)
                    continue
                elif need_check_list_type[0] == 0:
                    need_check_list_type.pop(0)
                    continue
            else:
                print(False)
                return False
        print(True)
        return True
