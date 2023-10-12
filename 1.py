# print('Язык: L(G)={a^n (ab)^m; n>0}')
# print('P: S -> aaAab')
# print('   A -> aaAab | aaab')
# var_A = 'aaAab'
# var_S = ['S ->', 'aaAab']

# while True:
#     print(' '.join((var_S)))
#     continue_cycle = input('Продолжить (да/нет): ').lower()
#     if (continue_cycle not in ['yes', 'y', 'да', 'д', 'l']):
#         var_S.append('->')
#         var_S.append(f'{var_S[-2].replace("A", "aaab")}')
#         print(' '.join((var_S)))
#         break
#     var_S.append('->')
#     var_S.append(f'{var_S[-2].replace("A", "aaAab")}')








# import numpy as np

# def cyk_parse(grammar, string):
#     n = len(string)
#     nonterminals = list(grammar.keys())
#     num_nonterminals = len(nonterminals)

#     # Создаем трехмерный массив для хранения результатов
#     table = np.zeros((n, n, num_nonterminals), dtype=bool)

#     # Заполняем таблицу для терминальных символов
#     for i in range(n):
#         for nonterminal in nonterminals:
#             if string[i] in grammar[nonterminal]:
#                 table[i, i, nonterminals.index(nonterminal)] = True

#     # Заполняем таблицу для нетерминальных символов
#     for l in range(2, n + 1):
#         for i in range(n - l + 1):
#             j = i + l - 1
#             for k in range(i, j):
#                 for nonterminal in nonterminals:
#                     for production in grammar[nonterminal]:
#                         if len(production) == 2:
#                             left, right = production
#                             left_index = nonterminals.index(left)
#                             right_index = nonterminals.index(right)
#                             if table[i, k, left_index] and table[k + 1, j, right_index]:
#                                 table[i, j, nonterminals.index(nonterminal)] = True

#     # Возвращаем результат
#     return table[0, n - 1, nonterminals.index('S')]

# grammar = {
#     'S': [('A', 'B')],
#     'A': [('C', 'D'), ('a',)],
#     'B': [('E', 'F'), ('b',)],
#     'C': [('c',)],
#     'D': [('d',)],
#     'E': [('e',)],
#     'F': [('f',)]
# }

# string = 'acdefb'
# result = cyk_parse(grammar, string)
# print(result)  # Выводит True

def continue_or_not(text):
    
    if (text in ['yes', 'y', 'да', 'д']):
        return True
    elif (text in ['нет', 'н', 'не', 'n', 'no']):
        return False
    else:
        print('Указано неверное значение')
        return 'Указано неверное значение'

def main():
    rules = []
    is_continue = True

    while is_continue:
        rules.append(input('Введите правило: '))
        cont = input('Продолжить вводить правила (да/нет): ').lower()
        is_continue = continue_or_not(cont)
        if (is_continue == 'Указано неверное значение'):
            print(is_continue)
            return

    sequence = ''
    # rules = ['S->aaAab', 'A->aaAab', 'A->aaab']
    # rules = ['S->AB', 'A->a', 'B->b']
    print('Правила грамматики:', rules)
    for rule in rules:
        if ('S' in rule.split('->')[0]):
            sequence += rule
            print('Начальная последовательность:', rule)
            break
    
    is_continue = True
    while is_continue:
        num = 0
        available_rules = []
        for rule in rules:
            if (rule.split('->')[0] in sequence.split('->')[-1]):
                available_rules.append(rule)
                print(f'{num}) {rule}')
                num += 1
        if (num == 0):
            print('Нет доступных правил')
            return
        num_of_rule = int(input('Выберите следующее правило: '))
        if (num_of_rule < 0 or num_of_rule >= len(available_rules)):
            print('Указано некорректное значение')
            return
        chosen_rule = available_rules[num_of_rule].split('->')
        # print(chosen_rule)

        new_sequence_part = '->' + sequence.split('->')[-1].replace(chosen_rule[0], chosen_rule[1])
        sequence = sequence + new_sequence_part
        print(sequence)
        cont = input('Продолжить вводить правила (да/нет): ').lower()
        is_continue = continue_or_not(cont)
        if (is_continue == 'Указано неверное значение'):
            print(is_continue)
            return
    # print(rules)

main()