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

# ε
# формат ['S->AB', 'A->a', 'B->b']
# grammar = ['S->ε', 'A->aAbb', 'A->aaab']
grammar = ['S->aAd', 'A->bSb', 'A->bb']
# grammar = ['S->tB', 'A->t']
# grammar = ['S->aQb', 'S->accb', 'Q->ε']
print(is_unlimited_grammar(grammar))

if (is_context_sensitive_grammar(grammar) == 'Является контекстно-зависимой грамматикой'):
    print(is_context_sensitive_grammar(grammar))
    print(is_non_shortening_grammar(grammar))
else:
    print(is_context_sensitive_grammar(grammar))

if (is_context_free_grammar(grammar) == 'Является контекстно-свободной грамматикой'):
    print(is_shortening_context_free_grammar(grammar))
else:
    print(is_context_free_grammar(grammar))
    
print(is_reg_grammar(grammar))

# Является грамматикой типа 0 (неограниченной грамматикой)
# Является неукорачивающей грамматикой
# Является контекстно-зависимой грамматикой
# Является контекстно-свободной грамматикой
# Является укорачивающей контекстно-свободной грамматикой
# Не является грамматикой типа 3