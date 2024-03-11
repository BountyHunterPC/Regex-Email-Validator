# 1st char should be a-z
# 0-9 nums allowed
# . or _ only 1 time allowed
# @ only 1 time allowed
# . position 2nd or 3rd from last

import re
email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter your Email:")
if re.search(email_conditions, user_email):
    print("Right Email")
else:
    print("Wrong Email!")