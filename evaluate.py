__author__ = "Jonnas Freire"
      
def separate_expression(expression:str) -> list:
    expression += "+"
    signals:list = ["-","+","/","*"]
    numbers:str = ""
    expression_items:list = []
    
    for item in expression:
        if item.isspace():
            expression.strip(item)
                           
        if item in signals:                
            expression_items.append(to_int(float(numbers.replace(",","."))))
            expression_items.append(item)
            numbers = ""
              
        else:
            numbers += item
             
    expression_items.pop()
    return expression_items


def to_int(number_to_int: float) -> int:    
    if "." in str(number_to_int):    
        pos = str(number_to_int).index(".")    
        zero:str = str(number_to_int)[pos+1:] == "0"

        if zero:
            number = int(number_to_int)
            return number
                
    return number_to_int
    

def calc(expression:str, detail:bool=False) -> int or float:
    if not expression: return 0

    res:list = separate_expression(expression)
    
    def evaluate(signal:str, i:int) -> int or float:        
        if signal == "/":
            return (res[i-1]) / (res[i+1])
        if signal == "*":
            return (res[i-1]) * (res[i+1])
        if signal == "+":
            return (res[i-1]) + (res[i+1])
        if signal == "-":
            return (res[i-1]) - (res[i+1])
        
       
    if len(res) == 1:   
        return to_int(res[0])
            
    elif len(res) > 1:
        signals:list = ["/","*","+","-"]      
        
        for signal in signals:
            for __ in range(res.count(signal)):                
                i = res.index(signal)                   
                result = evaluate(signal, i)
                    
                for __ in range(3):
                    res.pop(i-1)
                                            
                res.insert(i-1, to_int(result))
              
                if detail:
                    vs = ""
                    for a in res:
                        vs += str(a) + " "                                                                
                    print(vs)                                                
      
        return res[0]



if __name__ == "__main__":
    import os
    if os.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    print("="*51)
    exp = input("Calculate an expression: ")
    print("\nDetails:")
    print(calc(exp, True))
    print("="*51)
    
    
    
    
    
    
