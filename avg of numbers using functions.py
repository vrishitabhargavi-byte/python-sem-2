def compute_average(numbers):
    return sum(numbers)//len(numbers)
n=int(input("enter count:"))
nums = list(map(int,input().split()))
avg = compute_average(nums)
print("average:",avg)