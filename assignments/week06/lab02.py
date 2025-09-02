def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return {
        "area":area, 
        "circumference":circumference
    }