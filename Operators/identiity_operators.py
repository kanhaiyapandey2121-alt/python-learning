#do object ki memory location compare karne ke liye identity operator ka use karte hai 
"""
do type ke operator hote hai 
is-True(jab dono object ki same memory location ho)
is not -True(jab dono object ki same memory location nhi ho)

"""
a=[1,2,3]
b= a
c=[1,2,3]
print(a is b)
print(a is c)