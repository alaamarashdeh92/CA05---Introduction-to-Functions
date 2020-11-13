# Q 6
# ******

def compare_length(s1, s2):
    if len(s1) > len(s2) :
        return len(s1) - len(s2)
    else:
        return len(s2) - len(s1)
  
print(f"the difference in length between the strings {compare_length('aaaaa', 'asasasas')}")

