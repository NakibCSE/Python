
bd_division_info = {}
bd_division_info["Barishal"] = {"District": 6, "Upazila": 39, "Union": 333}
bd_division_info["Chittagong"] = {"District": 11, "Upazila": 93, "Union":336}
bd_division_info["Dhaka"] = {"District": 13, "Upazila": 93, "Union": 1833}
bd_division_info["Khulna"] = {"District": 10, "Upazila": 59, "Union": 270}
bd_division_info["Mymensingh"] = {"District":4, "Upazila": 34, "Union": 350}
bd_division_info["Rajshahi"] = {"District":8, "Upazila": 70, "Union": 536}
bd_division_info["Rangpur"] = {"District":8, "Upazila": 58, "Union": 536}
bd_division_info["Sylhet"] = {"District":4, "Upazila": 38, "Union": 33}

dis = 0
up = 0
un = 0
for key in bd_division_info:
    dis += bd_division_info[key]["District"]
    up  += bd_division_info[key]["Upazila"]
    un += bd_division_info[key]["Union"]

print(dis)
print(up)
print(un)


