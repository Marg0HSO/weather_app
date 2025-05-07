import csv
import python_weather
import asyncio
from cities_module import setTemperatureScore, setWindSpeedScore, setHumidityScore, setPrecipitationScore

# Lecture du CSV
import csv

activities_dict = {}

def setActivitiesDico():
    global activities_dict
    with open("activities.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            activity = row["activity"]
            type_    = row["type"]

            # -- température --
            temp_str = row["temperature"].strip("[]").strip()
            if not temp_str:
                temperature = []
            elif "," in temp_str:
                start, end = temp_str.split(",")
                temperature = [i for i in range(int(start), int(end) + 1)]
            else:
                temperature = [int(temp_str)]

            # -- vent --
            wind_str = row["wind_speed"].strip("[]").strip()
            if not wind_str:
                wind_speed = []
            elif "," in wind_str:
                s, e = wind_str.split(",")
                wind_speed = [i for i in range(int(s), int(e)+1)]
            else:
                wind_speed = [int(wind_str)]

            # -- humidité --
            hum_str = row["humidite"].strip("[]").strip()
            if not hum_str:
                humidite = []
            elif "," in hum_str:
                s, e = hum_str.split(",")
                humidite = [i for i in range(int(s), int(e)+1)]
            else:
                humidite = [int(hum_str)]

            # -- précipitations --
            prec_str = row["precipitation"].strip("[]").strip()
            if not prec_str:
                precipitation = []
            elif "," in prec_str:
                s, e = prec_str.split(",")
                precipitation = [i for i in range(int(s), int(e)+1)]
            else:
                precipitation = [int(prec_str)]

            # -- dictionnaire final --
            activities_dict[activity] = [
                type_, temperature, wind_speed, humidite, precipitation
            ]


# Test d'affichage
# print(activities_dict)

async def oneCityMatrice(city) -> list:
    """créer la matrice de la ville demandée"""
    async with python_weather.Client(unit=python_weather.METRIC) as client:
        try:
            weather = await client.get(city)
            tempInd = setTemperatureScore(weather.temperature)
            humiInd = setHumidityScore(weather.humidity)
            windInd = setWindSpeedScore(weather.wind_speed)
            precInd = setPrecipitationScore(weather.precipitation)
        except python_weather.RequestError:
            return [None]
    return [city, (tempInd, humiInd, windInd, precInd)]

async def activities(city, dico):
    listAct = []
    cityMatrice = await oneCityMatrice(city)
    c = 0
    print(cityMatrice)
    for activity in dico:
        if cityMatrice[1][0] in dico[activity][1] and cityMatrice[1][1] in dico[activity][2] and cityMatrice[1][2] in dico[activity][3] and cityMatrice[1][3] in dico[activity][4]:
            listAct.append((activity, dico[activity][0]))
    return listAct

setActivitiesDico()

async def createHTMLPage(city):
    acts = await activities(city, activities_dict)
    html_debut = f"""<!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>MétéoTrip | Activitées</title>
        <link rel="stylesheet" href="static/style.css">
    </head>
    <body>
    <header>
        MétéoTrip
    </header>
    <div class="container">
    <h1> On vous propose de faire </h1>
    <p> Les informations données ici ne prennent en compte que les données métérologique et non pas la location, certaines activités peuvent donc devenir impossible </p>
    <ul class="activity-list">
    """

    html_cartes = ""
    for nom, type_ in acts:
        nom = nom.strip('""')
        type_ = type_.strip('""')
        if type_ == "aartistique":
            html_cartes += f"""
        <li>
        <div class="activity-card">
            <img class="activity-icon" src="static/icons/aartistique.png" alt=icon_art>
            <p>{nom}</span>
        </div>
        </li> \n
        """
        elif type_ == "aloisirs":
            html_cartes += f"""
        <li>
        <div class="activity-card">
            <img class="activity-icon" src="static/icons/aloisirs.png" alt=icon_loisirs>
            <p>{nom}</p>
        </div>
        </li> \n
        """
        elif type_ == "abienetre":
            html_cartes += f"""
        <li>
        <div class="activity-card">
            <img class="activity-icon" src="static/icons/abienetre.png" alt=icon_bienetre>
            <p>{nom}</p>
        </div>
        </li> \n
        """
        elif type_ == "asportive":
            html_cartes += f"""
        <li>
        <div class="activity-card">
            <img class="activity-icon" src="static/icons/asportive.png" alt=icon_sport>
            <p>{nom}</p>
        </div>
        </li> \n
        """
        elif type_ == "aexterieur":
            html_cartes += f"""
        <li>
        <div class="activity-card">
            <img class="activity-icon" src="static/icons/aexterieur.png" alt=icon_ext>
            <p>{nom}</p>
        </div>
        </li> \n
        """

    html_fin = """  </ul>
                <a id="return-button" href="http://localhost:5000/">Retour à l'accueil</a>
                </div>
                </body>
                </html>"""
    html_code = html_debut + html_cartes + html_fin
    with open("templates/activities_result.html", "w", encoding="utf-8") as f:
        print(f)
        f.write(html_code)

       