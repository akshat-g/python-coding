def countBits(num):
    no_one_bits_zero = 0
    no_one_bits_one = 1
    no_one_bits_two = 1

    if num == 1:
        return [no_one_bits_zero, no_one_bits_one]
    if num == 2:
        return [no_one_bits_zero, no_one_bits_one, no_one_bits_two]

    toReturnArray = [0, 1, 1]
    landmark = 2
    i = 3
    counter = 1
    while i <= num:
        if counter == landmark:
            counter = 1
            landmark = 2*landmark
            toReturnArray.append(1)
        else:
            toAppend = toReturnArray[landmark] + toReturnArray[counter]
            toReturnArray.append(toAppend)
            counter += 1
        i += 1

    return toReturnArray

if __name__ == '__main__':
    print countBits(7)
