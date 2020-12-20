__author__ = "Jonnas Freire"

OPERATORS = "(/*+-)"

def separate_expression(expression:str) -> list:
    expression += "+"
    numbers:str = ""
    expression_items:list = []
    
    for item in expression:
        if item.isspace(): expression.strip(item)
        
        first_element_len:bool = len(expression[expression.index(item)]) == 0
        first_element_is_open_parenthesis:bool = expression[expression.index(item)-1] == '('                
        if item in OPERATORS:
            if item == '-' and first_element_len or first_element_is_open_parenthesis:
                numbers = item
            else:
                expression_items.append(to_int(numbers.replace(",",".")))
                expression_items.append(item)
                numbers = ""
        else:
            numbers += item
             
    expression_items.pop()
    new_expression:list = []
    for item in expression_items:
        if item in OPERATORS:
            new_expression.append(item)

        if item.strip() not in OPERATORS:
            new_expression.append(to_int(float(item.replace(',', '.'))))
    
    new_expression = [x for x in new_expression if x != ''] 
    return new_expression


def to_int(number_to_int: float) -> int:    
    if "." in str(number_to_int):    
        pos = str(number_to_int).index(".")    
        
        if str(number_to_int)[pos+1:] == "0":
            return int(number_to_int)
                
    return number_to_int
    

def evaluate(exp:list, operator:str, i:int) -> int or float:        
    f_num = i - 1
    s_num = i + 1
    operations = {
        "/": exp[f_num] / exp[s_num],
        "*": exp[f_num] * exp[s_num],
        "+": exp[f_num] + exp[s_num],
        "-": exp[f_num] - exp[s_num]
    } 
   
    return operations[operator]


def operation(operation:list) -> int or float:
    for op in OPERATORS[1:-1]:
        for __ in range(operation.count(op)):                
            i = operation.index(op)                   
            result = evaluate(operation, op, i)
                
            [operation.pop(i-1) for __ in range(3)]                                     
            operation.insert(i-1, to_int(result))

            if len(operation) == 1:
                return operation[0]


def calc(expression:str) -> int or float:
    from string import ascii_letters        
    
    if not expression:
        return False
   
    for it in expression:
        if it.lower() in ascii_letters[:26]:
            return None 
    
    res:list = separate_expression(expression)

    if len(res) == 1:   
        return to_int(res[0])
            
    elif len(res) > 1:
        try:
            while '(' in res:
                open_parenthesis:int = res.index('(')
                close_parenthesis:int = res.index(')')
                
                parenthesis_expression:list = res[open_parenthesis+1:close_parenthesis]
                parenthesis_result:int or float = operation(parenthesis_expression)

                [res.pop(open_parenthesis) for __ in range(open_parenthesis, close_parenthesis+1)]                   
                res.insert(open_parenthesis, parenthesis_result)
            
            return operation(res)
        except ValueError:
            print('\nThere's something wrong, please verify the expression.')


def main():
    import os, sys
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    print("="*51)
    print(" "*20+"Calculator"+" "*20)
    print("="*51)

    exp = input("> ")
    res = calc(exp)

    if res == None:
        print("error: Only expression allowed!")
    elif not res:
        print("error: Please type an expression!")    
    else:
        print(f"{exp} = {str(res).replace('.', ',')}\n")

    print("="*51)
        
    answer = input("Calculate again? Y/N: ")
    if answer.upper() == "Y":
        main()


if __name__ == "__main__":
    main()

