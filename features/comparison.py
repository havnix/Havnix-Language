def execute_comparison_operation(left_operand, operator, right_operand):
    if operator == "==":
        return left_operand == right_operand
    elif operator == "!=":
        return left_operand != right_operand
    elif operator == ">":
        return left_operand > right_operand
    elif operator == ">=":
        return left_operand >= right_operand
    elif operator == "<":
        return left_operand < right_operand
    elif operator == "<=":
        return left_operand <= right_operand
    else:
        print("عملية مقارنة غير صحيحة")
        return False
