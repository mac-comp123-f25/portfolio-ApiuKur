def count_negatives(numbers):
    if len(numbers)==0:
        return 0
    else:
        firstnum=numbers[0]
        if firstnum<0:
            return 1+count_negatives(numbers[1:])
        else:
            print(numbers[1:])
            return count_negatives(numbers[1:])


print(count_negatives([-1,2,3,4,5,-6,7]))