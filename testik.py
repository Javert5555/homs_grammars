def is_unlimited_grammar(grammar):
    for rule in grammar:
        if '->' not in rule:
            return 'Не является грамматикой типа 0 (неограниченной грамматикой)'
    return 'Является грамматикой типа 0 (неограниченной грамматикой)'

def is_non_shortening_grammar(grammar):
    for rule in grammar:
        rule = rule.replace(' ', '')
        left_part = rule.split('->')[0]
        right_part = rule.split('->')[1]
        if ('ε' in list(left_part) or 'ε' in list(right_part)):
            return 'Является укорачивающей контекстно-зависимой грамматикой'
        if (len(left_part) <= len(right_part) and len(left_part) >= 1):
            pass
        else:
            return 'Является укорачивающей контекстно-зависимой грамматикой'
    return 'Является неукорачивающей контекстно-зависимой грамматикой'

def is_context_sensitive_grammar(grammar):
    for rule in grammar:
        rule_left_part = rule.split('->')[0]
        if not any(char.isupper() for char in rule_left_part):
            return 'Не является контекстно-зависимой грамматикой'
        rule_right_part = rule.split('->')[1]
        index_of_upper_char_left = 0
        for i in range(len(rule_left_part)):
            if (rule_left_part[i].isupper()):
                index_of_upper_char_left = i
                break
        xi_left = rule_left_part[:index_of_upper_char_left]

        index_of_upper_char_right = 0
        for i in range(len(rule_left_part)-1, 0, -1):
            if (rule_left_part[i].isupper()):
                index_of_upper_char_right = i
                break
        xi_right = rule_left_part[index_of_upper_char_right+1:]

        # если в α есть терминал
        if any(char.islower() for char in rule_left_part[index_of_upper_char_left:index_of_upper_char_right+1]):
            return 'Не является контекстно-зависимой грамматикой'

        equality_xi_left = True
        if not (len(xi_left) == 0):
            # сравниваем ξ1 и ξ1 в левой и правой частях правила
            equality_xi_left = rule_right_part[:len(xi_left)] == xi_left
        equality_xi_right = True
        if not (len(xi_right) == 0):
            # сравниваем ξ2 и ξ2 в левой и правой частях правила
            equality_xi_right = rule_right_part[-len(xi_right):] == xi_right
        # проверяем равна ли γ (гамма) пустому значению
        len_gamma_more_than_one = len(xi_left) + len(xi_right) < len(rule_right_part)
        
        if ('ε' in list(rule_left_part) or 'ε' in list(rule_right_part)):
            return 'Не является контекстно-зависимой грамматикой'
        # print(xi_left)
        # print(xi_right)
        # print(equality_xi_left)
        # print(equality_xi_right)
        # print(rule_right_part[-len(xi_right):])
        # print(len_gamma_more_than_one)
        if not (equality_xi_left and equality_xi_right and len_gamma_more_than_one):
            return 'Не является контекстно-зависимой грамматикой'
    return 'Является контекстно-зависимой грамматикой'

def is_context_free_grammar(grammar):
    for rule in grammar:
        rule_left_part = rule.split('->')[0]
        if any(char.islower() for char in rule_left_part):
            return 'Не является контекстно-свободной грамматикой'
        rule_right_part = rule.split('->')[1]
        if (rule_right_part == 'ε'):
            return 'Не является контекстно-свободной грамматикой'
    return 'Является контекстно-свободной грамматикой'

def is_shortening_context_free_grammar(grammar):
    for rule in grammar:
        rule_left_part = rule.split('->')[0]
        if any(char.islower() for char in rule_left_part):
            return 'Является неукорачивающей контекстно-свободной грамматикой'
        rule_right_part = rule.split('->')[1]
        if (rule_right_part == 'ε'):
            return 'Является укорачивающей контекстно-свободной грамматикой'
    return 'Является неукорачивающей контекстно-свободной грамматикой'

def is_reg_grammar(grammar):
    left_flag = False
    for rule in grammar:
        rule_left_part = rule.split('->')[0]
        rule_right_part = rule.split('->')[1]
        if (rule_right_part == 'ε'):
            return 'Не является регулярной грамматикой'
        
        if any(char.islower() for char in rule_left_part):
            return 'Не является регулярной грамматикой'
        
        if any(char.isupper() for char in rule_right_part):
            index_of_upper_char_right = 0
            for i in range(len(rule_right_part)-1, 0, -1):
                if (rule_right_part[i].isupper()):
                    index_of_upper_char_right = i
                    break

            index_of_upper_char_left = 0
            for i in range(len(rule_right_part)):
                if (rule_right_part[i].isupper()):
                    index_of_upper_char_left = i
                    break
            if any(char.islower() for char in rule_right_part[index_of_upper_char_left:index_of_upper_char_right+1]):
                return 'Не является регулярной грамматикой'
            
            left_part = rule_right_part[:index_of_upper_char_left]
            right_part = rule_right_part[index_of_upper_char_right+1:]
            # print('left_part ', left_part)
            # print('right_part ', right_part)
            if (len(left_part) > 0 and len(right_part) > 0):
                return 'Не является регулярной грамматикой'
            if (len(left_part) > 0):
                left_flag = True

    if left_flag:
        return 'Является леволинейной грамматикой'
    else:
        return 'Является праволинейной грамматикой'

# Является грамматикой типа 0 (неограниченной грамматикой)
# Является неукорачивающей грамматикой
# Является контекстно-зависимой грамматикой
# Является контекстно-свободной грамматикой
# Является укорачивающей контекстно-свободной грамматикой
# Не является грамматикой типа 3

def continue_or_not(text):
    
    if (text in ['yes', 'y', 'да', 'д']):
        return True
    elif (text in ['нет', 'н', 'не', 'n', 'no']):
        return False
    else:
        print('Указано неверное значение\n')
        return 'Указано неверное значение'

def main():
    rules = []
    is_continue = True

    while is_continue:
        rules.append(input('Введите правило: '))
        cont = input('Продолжить вводить правила (да/нет): ').lower()
        is_continue = continue_or_not(cont)
        if (is_continue == 'Указано неверное значение\n'):
            return
    # ε
    # формат ['S->AB', 'A->a', 'B->b']
    # rules = ['S->aaAab', 'A->aaAab', 'A->aaab']
    # grammar = ['S->aAd', 'A->bSb', 'A->bb']
    # grammar = ['S->tB', 'A->t']
    # grammar = ['S->aQb', 'S->accb', 'Q->ε']

    is_unlimited = is_unlimited_grammar(rules)
    is_context_sensitive = is_context_sensitive_grammar(rules)
    is_non_shortening = is_non_shortening_grammar(rules)
    is_context_free = is_context_free_grammar(rules)
    is_shortening_context_free = is_shortening_context_free_grammar(rules)
    is_reg = is_reg_grammar(rules)

    print()
    print(is_unlimited)

    if (is_context_sensitive == 'Является контекстно-зависимой грамматикой'):
        print(is_context_sensitive)
        print(is_non_shortening)
    else:
        print(is_context_sensitive)

    if (is_context_free == 'Является контекстно-свободной грамматикой'):
        print(is_shortening_context_free)
    else:
        print(is_context_free)
    print(is_reg, '\n')


    sequence = ''
    # rules = ['S->aaAab', 'A->aaAab', 'A->aaab']
    # rules = ['S->AB', 'A->a', 'B->b']
    print('Правила грамматики:', rules)
    for rule in rules:
        if ('S' in rule.split('->')[0]):
            sequence += rule
            print('Начальная последовательность:', rule)
            cont = input('Продолжить последовательность (да/нет): ').lower()
            is_continue = continue_or_not(cont)
            if (is_continue == 'Указано неверное значение'):
                return
            if not is_continue:
                return
            print()
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
        print()
        print('Текущая последовательность: ', sequence)
        cont = input('Продолжить последовательность (да/нет): ').lower()
        print()
        is_continue = continue_or_not(cont)
        if (is_continue == 'Указано неверное значение'):
            return
    # print(rules)

main()