user_logged_in = False

def requires_login(func): 
    def wrapper(*args, **kwargs): 
        global user_logged_in
        if not user_logged_in: 
            raise Exception("User not authenticated")
        return func(*args, **kwargs)
    return wrapper


@requires_login 
def view_profile(): 
    print("Showing user profile")


view_profile