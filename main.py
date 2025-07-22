import utilities.calculator as a
import utilities.string_operations as b

# Sample inputs and printing results using calculator.py
print("Using calculator.py:")
print("Addition:", a.add(10, 5))
print("Subtraction:", a.subtract(10, 5))
print("Multiplication:", a.multiply(10, 5))
print("Division:", a.divide(10, 5))

# Sample strings and printing results using string_operations.py
sample_string = "hello World"
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", b.reverse_string(sample_string))
print("Capitalized:", b.capitalize_string(sample_string))
print("Lowercase:", b.lowercase_string(sample_string))
print("Uppercase:", b.uppercase_string(sample_string))