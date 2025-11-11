def climb_stairs(nums):

    steps = [0]*nums
    if nums == 1:
        return 1
    if nums == 2:
        return 2
    steps[0] = 1
    steps[1] = 2
    for i in range(2, nums):
        steps[i] = steps[i-1] + steps[i-2]

    return steps[nums - 1]

# Driver code
def main():
    inputs = [1, 4, 3, 5, 6]

    for i in range(len(inputs)):
        print(i + 1, ".\t Steps: ",inputs[i],"\n\n\t", \
                         " Number of ways: ", climb_stairs(inputs[i]), sep="")

        print("-" * 100)

if __name__ == '__main__':
    main()


