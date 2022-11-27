""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ⋀ - and ⋁ - or ¬ - not
 """
num = [0, 1]
for x in num:
    for y in num:
        for z in num:
            res1 = not (x or y or z)
            res2 = (not x) and (not y) and (not z)
            result = res1 is res2
            print(x, y, z, res1, res2, result)
