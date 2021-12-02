with open("nums.txt", "r") as f:
    nums = [int(i) for i in f.readlines()]

    # Part 1
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == 2020:
                print(nums[i] * nums[j])

    # Part 2
    for i in range(len(nums)-2):
        for j in range(i, len(nums)-1):
            for k in range(j, len(nums)):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print(nums[i] * nums[j] * nums[k])
