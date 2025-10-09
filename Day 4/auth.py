# Authorization check
def require_admin(func):
    def wrapper(user):
        if user != "admin":
            print("Access denied!")
            return
        return func(user)
    return wrapper

@require_admin
def delete_database(user):
    print(f"{user} deleted the database!")

delete_database("guest")
delete_database("admin")