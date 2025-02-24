def setTemperatureScore(temperature: int) -> int:
    """renvoie le score en fonction de la température
        o -0°c         --> 1 pts   
        o 1°c à 10°c   --> 2 pts
        o 11°c à 20°c  --> 3 pts
        o 21°c à 30°c  --> 4 pts
        o +30°c        --> 5 pts
    """
    try:
        if temperature < 0:
            return 1
        elif 1 <= temperature <= 10:
            return 2
        elif 11 <= temperature <= 20:
            return 3
        elif 21 <= temperature <= 30:
            return 4
        elif temperature > 30:
            return 5     
    except TypeError:
        return None

def setHumidityScore(humidity: int) -> int:
    """renvoie le score en fonction de l'humidité
        o -20%         --> 1 pts
        o +80%         --> 2 pts
        o 61% à 80%    --> 3 pts 
        o 41% à 60%    --> 4 pts
        o 21% à 40%    --> 5 pts
    """
    try:
        if humidity < 20:
            return 1
        elif humidity > 80:
            return 2
        elif 61 <= humidity <= 80:
            return 3
        elif 41 <= humidity <= 60:
            return 4
        elif 21 <= humidity <= 40:
            return 5
    except TypeError:
        return None

def setPrecipitationScore(precipitation: float) -> int:
    """renvoie le score en fonction des précipitations
        o +30mm        --> 1 pts
        o 10.1 à 30mm  --> 2 pts
        o 2.1 à 10mm   --> 3 pts
        o 0.1 à 2mm    --> 4 pts
        o 0mm          --> 5 pts
    """
    try:
        if precipitation > 30:
            return 1
        elif 10.1 <= precipitation <= 30:
            return 2
        elif 2.1 <= precipitation <= 10:
            return 3
        elif 0.1 <= precipitation <= 2:
            return 4
        elif precipitation == 0:
            return 5
    except TypeError:
        return None

def setWindSpeedScore(wind_speed: int) -> int:
    """renvoie le score en fonction de la vitesse du vent
        o +50km/h      --> 1 pts
        o 31 à 50km/h  --> 2 pts
        o 16 à 30km/h  --> 3 pts
        o 5 à 15km/h   --> 4 pts
        o -5km/h       --> 5 pts
    """
    try:
        if wind_speed > 50:
            return 1
        elif 31 <= wind_speed <= 50:
            return 2
        elif 16 <= wind_speed <= 30:
            return 3
        elif 5 <= wind_speed <= 15:
            return 4
        elif wind_speed < 5:
            return 5
    except TypeError:
        return None