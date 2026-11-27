class User: 
    def __init__(self, date_of_birth): 
        self.date_of_birth = date_of_birth

    @property 
    def age(self): 
        return 2025 - self.date_of_birth 
    

def require_adult(func):
    def wrapper(user, *args, **kwargs): 
        if user.age < 18: 
            raise Exception("The user is underage")
        return func(user, *args, **kwargs)
    return wrapper 


@require_adult 
def enter_club(user): 
    return "Welcome to the club"


u1 = User(2010)
u2 = User(2000)


try:
    print(enter_club(u2))
except Exception as e: 
    print("Error:", e)

try: 
    print(enter_club(u1))
except Exception as e: 
    print("Error:", e)
