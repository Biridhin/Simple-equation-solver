def get_terms(expression):
    valid_operations = ('+', '-', '/', '*')
    first_term, second_term = expression.split("=")

    for operation in valid_operations:
        if len(second_term.split(operation)) > 1:
            second_term = second_term.split(operation)
            A = "A" if first_term.isalpha() else float(first_term)
            B = "B" if second_term[0].isalpha() else float(second_term[0])
            C = "C" if second_term[1].isalpha() else float(second_term[1])
            
            return (A, B, C, operation) if str(A).isalpha() \
                   else (B, A, C, operation) if str(B).isalpha() \
                   else (C, A, B, operation)

def solve_equation(expression):
    operate = {"+": lambda n1, n2: n1 + n2,
               "-": lambda n1, n2: n1 - n2,
               "*": lambda n1, n2: n1 * n2,
               "/": lambda n1, n2: n1 / n2}
    oposite = {"+": "-",
               "-": "+",
               "*": "/",
               "/": "*"}
    unknown, X, Y, operation = get_terms(expression)
    
    if unknown == "A":
        return operate[operation](X, Y)
    elif unknown == "B":
        return operate[oposite[operation]](X, Y)
    else:
        if operation == "/":
            return operate[operation](Y, X)
        return operate[oposite[operation]](X, Y)
    

expression = ''.join(input('Digite a expressão: ').split())
solution = solve_equation(expression)
print(f"A solução para {' '.join([c for c in expression])} é {get_terms(expression)[0]} = {solution}")
