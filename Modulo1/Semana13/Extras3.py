def validate_numbers(func): 
    def wrapper(*args, **kwargs): 
        for a in args: 
            if not isinstance(a, (int, float)): 
                raise TypeError("All arguments must be numeric: {}".format(repr(a)))
        for k, v in kwargs.items(): 
            if not isinstance(v, (int, float)): 
                raise TypeError("All arguments must be numeric. Argument {} is not numeric: {}".format(k, repr(v)))
        return func(*args, **kwargs)
    return wrapper
        

def log_call(func): 
    def wrapper(*args, **kwargs): 
        result = func(*args, **kwargs)
        # Get the current date/time without using the "import" statement
        datetime = __import__('datetime').datetime 
        now = datetime.now()
        args_str = ', '.join(str(a) for a in args)
        print("func:{} - args: {} - [{}] - Result: {}". format(func.__name__, args_str, now, result))
        print("Result {}".format(result))
        return result
    return wrapper


@log_call
@validate_numbers
def multiply(a, b): 
    return a * b


                
            
            