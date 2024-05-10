def calculate_offspring(int1, int2, int3, int4, int5, int6):
    int_list = [int1, int2, int3, int4, int5, int6]
    scaling_list = [2, 2, 2, 1.5, 1, 0]

    offspring_list = [x * y for x, y in zip(int_list, scaling_list)]

    return sum(offspring_list)

if __name__ == '__main__':
    print(calculate_offspring(18450, 17800, 17426, 19348, 17260, 19716))

