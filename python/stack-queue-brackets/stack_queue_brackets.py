
def validate_brackets(string):
    stack = []
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0 or bracket_map[char] != stack.pop():
                return False
    
    return len(stack) == 0

print(validate_brackets("{}"))  # True
print(validate_brackets("{}(){}"))  # True
print(validate_brackets("()[[Extra Characters]]"))  # True
print(validate_brackets("(){}[[]]"))  # True
print(validate_brackets("{}{Code}[Fellows](())"))  # True
print(validate_brackets("[({}]"))  # False
print(validate_brackets("(]"))  # False
print(validate_brackets("{(})"))  # False


# this function we can use it if i need the user input string
# def input_validate_brackets():
#     string = input("Enter a string: ")
#     stack = []
#     opening_brackets = ['(', '[', '{']
#     closing_brackets = [')', ']', '}']
#     bracket_map = {')': '(', ']': '[', '}': '{'}
    
#     for char in string:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if len(stack) == 0 or bracket_map[char] != stack.pop():
#                 return False
    
#     return len(stack) == 0

# result = input_validate_brackets()
# print(result)