# #2
# word1 = input().lower()
# word2 = input().lower()
#
# if sorted(word1) == sorted(word2):
#     print("True")
# else:
#     print("False")

# #3
# a = int(input())
# x = int(input())
# y = int(input())
#
# numbers = [a,x,y]
# numbers.sort()
# print(numbers[2])

# # 4
# color1 = input().lower()
# color2 = input().lower()
#
# if color1 == 'красный' and color2 == 'синий' or color1 == 'синий' and color2 == 'красный':
#     print("фиолетовый")
# elif color1 == 'красный' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'красный':
#     print("оранжевый")
# elif color1 == 'синий' and color2 == 'желтый' or color1 == 'желтый' and color2 == 'синий':
#     print("зеленый")
# else:
#     print("ошибка цвета")
# # 5
# x = int(input())
# total_sum = 0
#
# for num in range(11, x + 1):
#     last_digit = num % 10
#     if last_digit in {2, 5, 8}:
#         total_sum += num
#
# print(total_sum)

# # 6
# x = int(input())
# digits = [int(digit) for digit in str(x)]
#
# if digits == sorted(digits):
#     print("Yes")
# else:
#     print("No")

# # 7
# y = int(input())
# for i in range(1, y + 1):
#     print(f"{i} {i} {i} {i} {i}")

# # 8
# text = input()
# print(text[2])
# print(text[-2])
# print(text[:5])
# print(text[:-2])
# print(text[::2])
# print(text[1::2])
# print(text[::-1])
# print(text[::-1][::2])


# # 9
# result = [chr(97 + i) * (i + 1) for i in range(26)]
# print(result)

# # 10
# numbers = list(map(int, input().split()))
# pairs = 0
#
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] == numbers[j]:
#             pairs += 1
#
# print(pairs)