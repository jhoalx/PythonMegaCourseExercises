def weather_condition(temperature: float) -> str:
    if temperature >= 10:
        return "Warm"
    else:
        return "Cold"


current_temperature = float(input("Please type current temperature"))
print(weather_condition(current_temperature))
