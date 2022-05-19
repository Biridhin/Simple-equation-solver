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


expression = ''.join(input('Digite a expressão: ').split())
