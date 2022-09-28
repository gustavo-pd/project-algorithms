def find_duplicate(nums):
    if len(nums) < 2 or not nums or not isinstance(nums, list):
        return False

    dict_nums = {}
    for n in nums:
        if n in dict_nums:
            return n
        if isinstance(n, str) or n < 0 or n == "":
            return False

        dict_nums[n] = 1

    return False
