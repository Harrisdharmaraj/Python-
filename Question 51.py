def calculate(s):
    # Initialize a stack to keep the numbers
    stack = []
    # Initialize the current number and the last sign to '+' (as we can consider the start of the string as a positive sign)
    num, sign = 0, '+'
    # Loop through each character in the string
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])  # Build the current number
        # If we encounter an operator or reach the end of the string, we process the last number
        if s[i] in "+-*/" or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                # Python division truncates towards negative infinity, so we manually truncate toward 0
                top = stack.pop()
                if top < 0:
                    stack.append(-(-top // num))
                else:
                    stack.append(top // num)
            num = 0  # Reset the current number
            sign = s[i]  # Update the last seen sign
    # The final result is the sum of the numbers in the stack
    return sum(stack)

# Test cases
test_inputs = ["3+2*2", " 3/2 ", " 3+5 / 2 ", "-1+5", "2+3+5"]
test_outputs = []

for test_input in test_inputs:
    test_outputs.append(calculate(test_input))

test_outputs
