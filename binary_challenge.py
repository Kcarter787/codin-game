# This program finds the nth term of the sequence where s(n+1) is the number
# of letters in the spelled-out binary form of the previous term,
# s(0) is determined by the starting input value


class Bin_function:

    # Map 0 and 1 to the number of letters in their respective strings
    eng_nums = ("zero", "one")
    mapper = {idx: len(num) for idx, num in enumerate(eng_nums)}

    def __init__(self, value):
        self._value = value

    def __iter__(self):
        return self

    def __next__(self):
        res = 0
        for char in self.bin_string:
            res += self.mapper[int(char)]
        self._value = res

    @property
    def value(self):
        return self._value

    @property
    def bin_string(self):
        return bin(self._value)[2:]

#TODO: - Create a frame which takes a start number and the nth term
def find_nth_term(start, n):
    """
    :param start: The initial value of the function (S(0) == start)
    :type start: Int

    :param n: The number of steps you want to take
    :type n: Int

    :return: The value of the nth number in the sequence
    :rtype: Int
    """
    example = Bin_function(start)
    for _ in range(n):
        next(example)
    return example.value


if __name__ == '__main__':
    # Write tests here
    try:
        start = int(input("Input a value for S(0)\n"))
        n = int(input("Input n\n"))
    except ValueError:
        print("Your input did not consist entirely of numeric characters. "
              "Stopping program.\n")

    print(find_nth_term(abs(start), abs(n)))







