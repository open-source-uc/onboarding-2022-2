def cursed_sum(a, b):
    first_number = format(a, "b")
    second_number = format(b, "b")
    max_len = max(len(first_number), len(second_number))
    first_number = first_number.zfill(max_len)
    second_number = second_number.zfill(max_len)
    list_first_number = list(first_number)
    list_second_number = list(second_number)
    result = []
    carry = "0"
    for i in range(max_len - 1, -1, -1):
        if list_first_number[i] == "1" and list_second_number[i] == "1":
            if carry == "1":
                result.append("1")
            else:
                result.append("0")
            carry = "1"
        elif list_first_number[i] == "0" and list_second_number[i] == "0":
            if carry == "1":
                result.append("1")
                carry = "0"
            else:
                result.append("0")
        else:
            if carry == "1":
                result.append("0")
                carry = "1"
            else:
                result.append("1")
    if carry == "1":
        result.append("1")
    return int(''.join(result[::-1]), 2)
