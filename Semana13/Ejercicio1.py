def print_params_and_return(func): 
    def wrapper(*args, **kwargs): 
        # Show the parameters 
        print(f"Called {func.__name__} with args={args}, kwargs={kwargs}")

        # Execute the original function 
        result = func(*args, **kwargs)

        # Show the return value 
        print(f"{func.__name__} returned {result}")

        return result 
    return wrapper 