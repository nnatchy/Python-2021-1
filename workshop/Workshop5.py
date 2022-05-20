
#1.1
# def factorial(value):
#     if value == 0:
#         return 1
#     else:
#         total = 1
#         for i in range(1,value+1):
#             total = total*i
#         return total

#1.2
def factorial(value):
    if value == 0:
        return 1
    else:
        fact = factorial(value-1)
        return value * fact

print(factorial(3))
print(factorial(4))
print(factorial(10))

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.left.left = TreeNode(5)
#t1.right = TreeNode(2)