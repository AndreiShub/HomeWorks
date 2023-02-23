import re

string = r"The side bar includes a Cheatsheet 09:00. ,You can al29:59so 21:21 Sha24:24re with the Comm11:11unity and view patterns you create or favorite in My Patterns.25:28"
result_time = re.findall(r"[0-2][0-9]:[0-5][0-9]", string)
print(result_time)
for i in result_time:
    r = i[0] + i[1]
    if int(r) > 23:
        result_time.remove(i)

print(result_time)