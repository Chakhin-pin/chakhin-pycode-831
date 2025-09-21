def create_user_profile(username, age=18, premium=False):
    if premium == True:
        return f"{username} (age: {age}) - Premius User"
    else:
        return f"{username} (age: {age}) - Standard User"
