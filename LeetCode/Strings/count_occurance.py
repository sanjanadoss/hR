string = "geeks for geeks"
string = string.replace(" ", "")
ans_dict = {}
  
for i in string:
    if i in ans_dict:
        ans_dict[i] += 1
    else:
        ans_dict[i] = 1
print(ans_dict)