def count_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1
