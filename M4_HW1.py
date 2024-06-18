import fake_math as fm
import true_math as tm

result1 = fm.divider(69, 3)
result2 = fm.divider(3, 0)
result3 = tm.divider(49, 7)
result4 = tm.divider(15, 0)
result5 = tm.divider(-15, 0)  # доп. -inf

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
