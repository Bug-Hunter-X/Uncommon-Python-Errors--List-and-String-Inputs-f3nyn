def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type error"

# Uncommon error: Passing a list to the function
result1 = function_with_uncommon_error([1, 2], 2) #expecting TypeError
print(result1) # Output: Type error

# Another uncommon error: Passing a string to the function
result2 = function_with_uncommon_error(10, "2") # expecting TypeError
print(result2) #Output: Type error

# Common Error: Passing 0 to the function
result3 = function_with_uncommon_error(10, 0)
print(result3) # Output: Division by zero