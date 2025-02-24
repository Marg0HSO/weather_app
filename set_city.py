# Importations
import python_weather
import asyncio
from score_set import *

debug = True
if debug:
    import nest_asyncio
    nest_asyncio.apply()

"""
POUR UTILISER LE PROGRAMME SUR SPYDER :
    import nest_asyncio
    nest_asyncio.apply()
"""

# FONCTIONS

async def addCity(city: str, matrice: list) -> None:
    """ajoute une ville à la matrice de ville"""
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        try:
            weather = await client.get(city)

            tempScore = setTemperatureScore(weather.temperature)
            humiScore = setHumidityScore(weather.humidity)
            windScore = setWindSpeedScore(weather.wind_speed)
            precScore = setPrecipitationScore(weather.precipitation)

            description = weather.description

            try:
                total = tempScore + humiScore + windScore + precScore
            except TypeError:
                total = None

            assert type(matrice) == list
            matrice.append([city, (tempScore, humiScore, windScore, precScore, description), total])
        except python_weather.RequestError:
            print("Erreur : Les données n'ont pas pu être chargées")

