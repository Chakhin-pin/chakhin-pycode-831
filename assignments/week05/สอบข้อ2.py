def weather_suggestion(temp):
    if temp > 35:
        return "very hot, stay indoor"
    elif 25 <= temp <= 35:
        return "nice weather"
    elif 20 <= temp <= 24:
        return "quite cool"
    else:  # temp < 20
        return "cool, wear jacket"


# ทดสอบฟังก์ชันตามโจทย์
test_temps = [38, 30, 22, 18]

for t in test_temps:
    print(f"Temp {t}°C: {weather_suggestion(t)}")