


def gen(value: str, start: int = 1) -> {}:
    """
    :param value: str, generator data
    :param start: int, start value
    :return: dict, consist from index as a kye and value as a dict value
    """
    yield 1
    # for i in range(len(value)):
    #     yield {(i + start): value[i]}

    # '', (1,2,5), [1,5,7], {1:1}

d = {}
for i in gen(10, start=1):
    print(i)
    #
    # i = next('abc')  # -> 1
    # i = next(I)  # -> 2
    # i = next(I)  # -> 5
    # x = gen()
    # I = iter(x)
    # i = next(I)
print(d)
