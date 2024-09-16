import re
import os

pwd = os.getcwd()
file_location = pwd + "/week8_regex/search.txt"
with open(file_location, "r") as file:
    reader = file.read()
    extracted = re.findall(
        r"([A-Za-z\s]+) <([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})> (\d{10})",
        reader,
    )
    # for name, email, phone in extracted:
    #     name = name.strip()
    #     print(f"Name: {name} Phone: {phone} Email: {email}")


new_file = pwd + "/week8_regex/output.txt"

with open(new_file, "w") as file:
    for name, email, phone in extracted:
        name = name.strip()
        formatted_output = (
            f"name of user is {name} with phone {phone} and email {email}\n"
        )
        file.write(formatted_output)
