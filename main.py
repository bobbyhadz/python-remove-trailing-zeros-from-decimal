# Remove the trailing zeros from a Decimal in Python

from decimal import Decimal

num = Decimal('1.230000')


def remove_exponent(d):
    return (
        d.quantize(Decimal(1))
        if d == d.to_integral()
        else d.normalize()
    )


print(remove_exponent(num))  # 👉️ 1.23