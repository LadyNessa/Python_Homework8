# 1. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
# последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).

# def read_last(lines, file):
#     with open(file, "r", encoding="utf-8") as res:
#         res_list = res.read().splitlines()
#         for ind in range(len(res_list) - 1, 0, -1):
#             if ind >= len(res_list) - lines:
#                 print(res_list[ind])
#
# number = int(input("Введите кол-во строк с конца:"))
# read_last(number, "article.txt")

# 2. Требуется реализовать функцию longest_words(file), которая записывает в файл result.txt слово,
# имеющее максимальную длину (или список слов, если таковых несколько).
#
# def longest_words(file):
#     with open(file, "r", encoding='utf-8') as f:
#         text_list = f.read().split()
#         len_max = len(text_list[0])
#         for el in text_list:
#             if len(el) > len_max:
#                 len_max = len(el)
#                 maxim_word = el
#         with open("result.txt", "w", encoding='utf-8') as res:
#             res.write(maxim_word)
#
# longest_words("article.txt")









