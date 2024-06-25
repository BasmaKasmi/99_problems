def open_closed(s):
    parentheses_count = 0
    brackets_count = 0
    single_quote_count = 0
    double_quote_count = 0

    for char in s:
        if char == '(':
            parentheses_count += 1
        elif char == ')':
            parentheses_count -= 1
        elif char == '[':
            brackets_count += 1
        elif char == ']':
            brackets_count -= 1
        elif char == "'":
            if double_quote_count % 2 == 0:
                single_quote_count += 1
        elif char == '"':
            if single_quote_count % 2 == 0:
                double_quote_count += 1
        if parentheses_count < 0 or brackets_count < 0:
            return False
    return (parentheses_count == 0 and
            brackets_count == 0 and
            single_quote_count % 2 == 0 and
            double_quote_count % 2 == 0)
