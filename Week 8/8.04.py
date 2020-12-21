from functools import reduce

print(
    reduce(
        lambda x, y: x * y,
        map(
            lambda x: int(input()),
            range(int(input()))
        )
    ) == 0
)
