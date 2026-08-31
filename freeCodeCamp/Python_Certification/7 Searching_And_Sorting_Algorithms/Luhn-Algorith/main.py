def verify_card_number(nums):
    nums = nums.replace("-", "")
    nums = nums.replace(" ", "")
    numsInt = list(map(int, nums[::-1]))
    total = 0

    for index, num in enumerate(numsInt):
        if index % 2 != 0:
            numsInt[index] = num * 2
            if numsInt[index] > 9:
                numsInt[index] = numsInt[index] - 9

        total += numsInt[index]

    print(total)            
    if total % 10 == 0: 
        return "VALID!"

    return "INVALID!"

verify_card_number("453914889")
verify_card_number('4111-1111-1111-1111')
verify_card_number('1234 5678 9012 3456')