import re

def parse_testcase(testcase):
    testcase_dict = {}

    # Extract the testcase number
    number_match = re.search(r"\# Testcase (\d+):", testcase)
    if number_match:
        testcase_number = int(number_match.group(1))
        testcase_dict["Number"] = testcase_number

    # Extract headings and data fields
    headings_and_content = re.findall(r"## (.*?)(?:\r?\n)+(.+?)(?=(?:\r?\n)+##|\Z)", testcase, re.DOTALL)
    for heading, content in headings_and_content:
        testcase_dict[heading.strip()] = content.strip()

    return testcase_dict

# Example usage
testcase = """
# Testcase 42: Short description

Table of contents

--

## Data field one

content of data field one

## Data field two

content of data field two
"""

result = parse_testcase(testcase)
print(result)