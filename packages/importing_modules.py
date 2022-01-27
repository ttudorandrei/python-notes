# # from the my_functions package import the os_functions file
# import my_functions.os_functions as my_func
# print(my_func.work_dir)
# print(my_func.return_cpu_info())
# print(my_func.return_new_vegas())

# PIP -> PIP Installs Packages (Auto-acronym)

import requests

r = requests.get("https://www.bbc.co.uk")
print(r, type(r))

print(r)

