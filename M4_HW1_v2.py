from fake_math import divider as fmd
from true_math import divider as tmd

result1 = fmd(69, 3)
result2 = fmd(3, 0)
result3 = tmd(49, 7)
result4 = tmd(15, 0)
result5 = tmd(-15, 0)  # доп. -inf

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)