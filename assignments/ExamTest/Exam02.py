def weather_suggestion(temp):
    if temp > 35:
        return "very hot,stay indoor"
    elif 25 <= temp <= 35:
        return "nice weather"
    elif 20 <= temp <= 24:
        return "quite cool"
    else:
        return "cool,wear jacket"

print(weather_suggestion(38))
print(weather_suggestion(30))
print(weather_suggestion(22))
print(weather_suggestion(18))