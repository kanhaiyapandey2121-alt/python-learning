"""
multiple condition combine-boolean true/false

and-all conditions must be true>true
or-atleat one condition true>true
not-singal operand,reverse 
"""
age=20
is_student= True

print(age>18 and is_student)
print(age>25 or is_student)
print(not is_student)

#or one more example

a=10
b=20
print(a>5 and b>10)
print(a<2 or b==20)
print(not(a==10))
