def improved_function(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers.")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

#Testing the improved function
result1 = improved_function([1,2],2) #raises TypeError
print(result1) #Output: Inputs must be numbers.

result2 = improved_function(10,"2") #raises TypeError
print(result2) #Output: Inputs must be numbers.

result3 = improved_function(10,0) #raises ZeroDivisionError
print(result3) #Output: Division by zero

result4 = improved_function(10,2) #successful
print(result4) #Output: 5.0