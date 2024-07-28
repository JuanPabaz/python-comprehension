def increment_value(x):
    return x + 1

result = increment_value(5)
print(result)

result_lambda = lambda x: x + 1
print(result_lambda(5))

full_name = lambda name, last_name: f"Full name is: {name} {last_name}"
print(full_name("Juan Pablo","Giraldo"))