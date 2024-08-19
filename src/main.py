import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame


def main():
    sns.set_style("darkgrid")
    plt.figure(figsize=(10, 10))

    # DataFrame.add()

    total_number = 1000

    seed: int = 7  # X0
    multiplier: int = 400  # a
    increment: int = 400  # c
    # module: int = 5465486464684684068468068  # M
    module = 9999

    current_number = seed

    numbers_list = []

    for i in range(total_number):
        current_number = randomize(
            a=multiplier, x=current_number, c=increment, m=module)
        numbers_list.append(current_number)
        # numbers_list.append(dict(x = i, n=current_number))

    print(f'Final list. Count: {len(numbers_list)}')

    for number in range(len(numbers_list)):
        print(f'{number} | {numbers_list[number]}')

    g = sns.scatterplot(data=DataFrame({'Numbers': numbers_list}))
    plt.show()


def randomize(a, x, c, m: int) -> int:
    return (a * x + c) % m


if __name__ == '__main__':
    main()
