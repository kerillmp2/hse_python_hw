# Найти все числа от 1 до 1000, которые делятся на 17
def task_1():
    ans = []
    for i in range(1, 1001):
        if i % 17 == 0:
            ans.append(i)
    return ans

# Найти все числа от 1 до 1000, которые содержат в себе цифру 2
def task_2():
    ans = []
    for i in range(1, 1001):
        n = i
        while n > 0:
            if n % 10 == 2:
                ans.append(i)
                break
            n = n // 10
    return ans

# Найти все числа от 1 до 10000, которые являются палиндромом	
def task_3():
    ans = []
    for i in range(1, 10001):
        s = str(i)
        pol = True
        for j in range(0, len(s) // 2 + 1):
            if s[j] !=  s[len(s) - j - 1]:
                pol = False
        if pol:
            ans.append(i)
    return ans

# Посчитать количество пробелов в строке
def task_4(s):
    ans = 0
    for c in s:
        if c == " ":
            ans += 1
    return ans


# Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова
def task_5(s):
    new_s = ""
    for c in s:
        if c not in ["e", "y", "u", "i", "o", "a"]:
            new_s += (c)
    return new_s

# На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5
def task_6(s):
    ans = []
    words = s.split(" ")
    for word in words:
        if len(word) <= 5:
            ans.append(word)
    return ans


# На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении 
длина этого слова.
def task_7(s):
    ans = {}
    words = s.split(" ")
    for word in words:
        ans[word] = len(word)
    return ans

# На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то 
есть на выходе список уникальных букв.
def task_8(s):
    ans = []
    for c in s:
        # Если список должен быть регистронезависимым, нужно переводить c в lower case.
        if c >= 'A' and c <= "z":
            if c not in ans:
                ans.append(c)
    return ans

# На входе список чисел, получить список квадратов этих чисел / use map
def task_9(nums):
    return [x**2 for x in nums]


# На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
# На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
def task_10(coords):
    ans = {}
    for point in coords:
        if point[1] == (5 * point[0] - 2):
            ans[point] = (point[0]**2 + point[1] ** 2) ** (1/2)
    return ans


# Возвести в квадрат все четные числа от 2 до 27. На выходе список.
def task_11():
    ans = []
    for i in range(2, 28):
        if i % 2 == 0:
            ans.append(i**2)
    return ans

# На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти 
def task_12(coords):
    mx = 0
    for point in coords:
        if point[0] >= 0 and point[1] >= 0:
            mx = max(mx, point[0]**2 + point[1] ** 2)
    return mx ** (1/2)


# На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), 
(11, -5), ...]
def task_13(nums_first, nums_second):
    ans = []
    for i in range(0, min(len(nums_first), len(nums_second))):
        ans.append((nums_first[i] + nums_second[i], nums_first[i] - nums_second[i]))
    return ans


# На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать 
снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.
def task_14(ss):
    ans = []
    for s in ss:
        n = int(s)
        if n % 2 == 0:
            ans.append(str(n ** 2))
    return ans


# Менеджер как обычно придумал свое представление данных, а нам оно не подходит
# Мы хотим получить нормальную таблицу, чтобы импортировать в csv
def task_15(input_str):
    rows = input_str.split("\n")
    ans = []
    for row in rows:
        row_splitted = row.split(",")
        param_name = row_splitted[0]
        for i in range(1, len(row_splitted)):
            if (len(ans) < i):
                ans.append({})
            ans[i - 1][param_name] = row_splitted[i]
    return ans
    
    
def task_16(a):
    if len(a) < 1:
        return []
    ans = [0] * len(a[0])
    for l in a:
        for i in range(len(l)):
            ans[i] += l[i]
    return ans
