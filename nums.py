def find_missing_nums(ls):
    ls.sort()
    digits= [item for item in range(1,ls[len(ls)-1]+1)]
    return list(set(digits)-set(ls))

nums = [int(item) for item in input().split()]
print(find_missing_nums(nums))
