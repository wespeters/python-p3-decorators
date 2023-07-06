# def hello(name):
#     return "Hello " + name

# print(hello("Guido"))
# # Hello Guido

# greeting = hello
# print(greeting("Guido"))
# # Hello Guido

# def salutation(func):
#     return func("Guido")

# print(salutation(greeting))

# def hello(name):
#     print("Hello from the hello() function.")

#     def greet():
#         print("Greetings from the greet() function.")

#     return greet
# hello("Guido")()

# def decorator(func):
#     def wrapper():
#         print("I am the output that lets you know the function is about to be called.")
#         func()
#         print("I am the output that lets you know the function has been called.")
#     return wrapper

# @decorator
# def get_called():
#     print("I am the function and I am being called.")

# get_called()

def check_working_hours(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            print("I'm off duty!")
    return wrapper

@check_working_hours
def sweep_floors(time):
    print("Sweeping the floors...")

@check_working_hours
def wash_dishes(time):
    print("Washing the dishes...")

@check_working_hours
def chop_vegetables(time):
    print("Chopping the vegetables...")

sweep_floors(800)
# I'm off duty!
wash_dishes(1000)
# I'm off duty!
chop_vegetables(1200)
# Chopping the vegetables...