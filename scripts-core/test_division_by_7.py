def check_divisible_by_7(in_number: int) -> int:

    number_groups = []
    group_digits = ""


    string_to_work_with = str(in_number)[::-1]

    for i, digit in enumerate(string_to_work_with):
        # print(f"Position {i+1} = {digit}")


        if (i + 1) % 3 == 0 or (i + 1) == len(str(in_number)): # 3rd in group or last digit reached
            group_digits = group_digits + digit
            # print(f"Before adding to list {group_digits}")
            number_groups.append(group_digits)
            group_digits = ""
        elif (i + 1) % 3 != 0:
            group_digits = group_digits + digit

    # print(number_groups)

    if len(number_groups) > 0:
        first_number = int(number_groups[0])
        last_number = int(number_groups[len(number_groups)-1])

        print(f"first_number = {first_number}, last_number = {last_number}")
        check_for_7 = abs(int(first_number) - int(last_number))

        """
        if check_for_7 % 7 == 0:
            print(f"{str(in_number)} is divisible by 7")
        else:
            print(f"{str(in_number)} is not divisible by 7")
        
        """


        if ((check_for_7 % 7) == 0 and (in_number % 7) != 0) or ((check_for_7 % 7) != 0 and (in_number % 7) == 0):
            return in_number
        else:
            return 0




if __name__ == "__main__":

    datatype_check = True
    test_number = 0

    """
    try:
        test_number = int(input("Input any number \n"))
    except ValueError:
        datatype_check = False
    """

    start_number = 1001
    end_number = 1002

    number_list_to_check = [i for i in range(start_number, end_number)]

    div_fails_list = []

    if datatype_check:
        for i in range(len(number_list_to_check)):
            return_val = check_divisible_by_7(number_list_to_check[i])
            if return_val != 0:
                div_fails_list.append(return_val)

    if len(div_fails_list) > 0:
        print(div_fails_list)