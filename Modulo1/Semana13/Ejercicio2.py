def require_numbers(func): 
    def wrapper(*args, **kwargs): 
        # Check positional arguments 
        for i, a in enumerate(args): 
            if not isinstance(a, (int, float)): 
                raise TypeError(f"Argument {i} ({a!r}) is not a number ")
            
        # Check keyword arguments 
        for k, v in kwargs.items(): 
            if not isinstance(v, (int, float)): 
                raise TypeError(f"Argument '{k}' ({v!r}) is not a number")
        
        return func(*args, **kwargs)
    return wrapper 
    

@require_numbers
def add(a, b): 
    return a + b 


print(add(5, 7))

try: 
    print(add(5, "hello"))  # Raises TypeError 
except TypeError as e: 
    print("Error:", e)
    
    
    
    
