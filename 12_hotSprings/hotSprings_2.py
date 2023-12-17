with open('./12_hotSprings/input.txt', 'r') as file:
    input = file.readlines()

cache = {}

def main():
    ans = 0
    for line in input:
        data, nums = line.split()
        nums = tuple(map(int, nums.split(",")))
        
        data = "?".join([data] * 5)
        nums *= 5
        
        ans += count(data, nums)
    
    # print(newData)
    # print(newNums)
    print(ans)
    
    return

def count(data, nums):
    if data == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if "#" in data else 1
    
    key = (data, nums)
    if key in cache:
        return cache[key]
    
    result = 0
    if data[0] in ".?":
        result += count(data[1:], nums)
    
    if data[0] in "#?":
        if nums[0] <= len(data) and "." not in data[:nums[0]] and (nums[0] == len(data) or data[nums[0]] != "#"):
            result += count(data[nums[0] + 1:], nums[1:])
    
    cache[key] = result
    return result


main()