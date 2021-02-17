#!/usr/bin/python3
import sys


def main():
    next_biggest_number(sys.argv[1])


def next_biggest_number(num):
    # CAUTION: num argument will be of type str as it is sourced from sys.argv input in main function
    # Test File Passes numbers as int type
    # Below line will force correct construction of a python list of ints in either case
    digit_list = [int(x) for x in str(num)]

    i = len(digit_list) - 1
    while True:
        if digit_list[i] > digit_list[max(i-1, 0)]:
            break  # using break as keeping the value of i will save us a pass through the loop below

        if i == 0:
            return -1  # number is already largest configuration possible of these integers; rules say return -1
        i -= 1

    # Find smallest number to the right of index i, that is also greater than the lower digit detected to the left of i
    lowest_found_right_index = i
    for j in range(i + 1, len(digit_list)):
        if digit_list[lowest_found_right_index] > digit_list[j] > digit_list[i-1]:
            lowest_found_right_index = j

    digit_list[lowest_found_right_index], digit_list[i-1] = digit_list[i-1], digit_list[lowest_found_right_index]

    digit_list = digit_list[:i] + sorted(digit_list[i:])
    digit_list = [str(x) for x in digit_list]

    return int("".join(digit_list))


if __name__ == "__main__":
    main()
