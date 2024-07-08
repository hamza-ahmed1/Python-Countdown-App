import datetime
x=datetime.datetime.now()



date_str=input("Enter date and Goal --- i-e Python:10-06-2024   :   ")
print(f"Today's Date : {x}")
date_list=date_str.split(":")
date_format=date_list[1].split("-")
y = datetime.datetime(int(date_format[2]),int(date_format[1]), int(date_format[0]))
print(f"Your Goal's Deadline : {y}")

print(f"Total Remaining Days : {y-x}" )