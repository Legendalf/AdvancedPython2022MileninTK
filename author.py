def author(decorator_arg): 
    def decorator(func):
        func._author = decorator_arg
        return func
    return decorator

@author("Dany Longo")
def add2(num: int) -> int:
    return num + 2

print(add2._author)
