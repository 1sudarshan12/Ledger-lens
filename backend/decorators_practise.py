def show(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show(1, 2, 3)
show(name="Sudarshan", city="Kathmandu")
show(10, "hi", debug=True)
show()



def make_invoice(vendor, amount, currency="NPR"):
    return f"{vendor}: {amount} {currency}"

data_list = ["Daraz", 2500]
data_dict = {"vendor": "Pathao", "amount": 800, "currency": "USD"}

# Call make_invoice once using data_list and once using data_dict, using only * and **, without indexing like data_list[0].
print("Second part of the code:")
print(make_invoice(*data_list))
print(make_invoice(**data_dict))



def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper
@timer
def slow_function():
    import time
    time.sleep(2)
    return "Finished"



print("Third part of the code:")
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"Hello, {name}!"

print(greet("Sudarshan"))  # Output: "HELLO, SUDARSHAN!"




def positive_only(func):
    def wrapper(*args, **kwargs):
        if args and args[0] < 0:
            return "Amount must be positive"
        return func(*args, **kwargs)
    return wrapper

@positive_only
def pay(amount: float) -> str:
    return f"Paid {amount}"

print(pay(500))    # Paid 500
print(pay(-20))



# Final one

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.get("user"):
            return "Redirect to /login"
        return func(request, *args, **kwargs)
    return wrapper


@login_required
def dashboard(request):
    return f"Welcome {request['user']}"

@login_required
def profile(request, tab="overview"):
    return f"{request['user']}'s profile, tab: {tab}"


print(dashboard({"user": "sudarshan"}))          # Welcome sudarshan
print(dashboard({"user": None}))                 # Redirect to /login
print(profile({"user": "sudarshan"}, tab="tax")) # sudarshan's profile, tab: tax
print(profile({"user": None}, tab="tax"))        # Redirect to /login
print(dashboard.__name__)  