# Q 5
# ******

def seq_check(numbers):
    number =""
    for i in numbers:
        number += str(i)
    if "123" in number:
        return True
    else:
        return False
numbers=[1,2,3,4,5]
print(seq_check(numbers))

