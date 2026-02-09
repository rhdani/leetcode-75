def rescue_boats(people, limit):
    numBoats = 0

    pSorted = sorted(people)
    left = 0
    right = len(pSorted) - 1
    while (left <= right):
        if (pSorted[left] + pSorted[right] <= limit):
            left += 1
            right -= 1
        else:
            right -= 1
        numBoats += 1
    return numBoats
# Driver code
def main():
    people = [[1, 2], [3, 2, 2, 1], [3, 5, 3, 4], [
        5, 5, 5, 5], [1, 2, 3, 4], [1, 2, 3], [3, 4, 5]]
    limit = [3, 3, 5, 5, 5, 3, 5]
    for i in range(len(people)):
        print(i + 1, "\tWeights = ", people[i], sep="")
        print("\tWeight Limit = ", limit[i], sep="")
        print("\tThe minimum number of boats required to save people are ",
              rescue_boats(people[i], limit[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
