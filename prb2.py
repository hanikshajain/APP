
import re

text = "The products cost Rs500, Rs1250 and Rs 99.50."

# Extract monetary values using Regex
pattern = r'Rs\s*\d+(?:\.\d{1,2})?'

result = re.findall(pattern, text)

print("Monetary Values:")
print(result)
