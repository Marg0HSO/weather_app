from flask import Flask, render_template, jsonify, request
import json
from cities_module import getCitiesClassement
from activities_module import createHTMLPage

FICHIER_JSON = "cities.json"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/citiesForm")
def form1():
    return render_template("cities_form.html")

@app.route("/activitiesForm")
def form2():
    return render_template("activities_form.html")

@app.route("/activitiesResult")
async def result2():
    city = request.args.get("city")
    await createHTMLPage(city)
    return render_template("activities_result.html")

@app.route("/citiesResult")
async def result1():
    classement = await getCitiesClassement()
    try:
        firstname = str(classement[0][0])
        firsttemp = str(classement[0][1][0])
        firsthumi = str(classement[0][1][1])
        firstwind = str(classement[0][1][2])
        firstprec = str(classement[0][1][3])
        try:
            secondname = str(classement[1][0])
            secondtemp = str(classement[1][1][0])
            secondhumi = str(classement[1][1][1])
            secondwind = str(classement[1][1][2])
            secondprec = str(classement[1][1][3])
            try:
                thirdname = str(classement[2][0])
                thirdtemp = str(classement[2][1][0])
                thirdhumi = str(classement[2][1][1])
                thirdwind = str(classement[2][1][2])
                thirdprec = str(classement[2][1][3])
                try:
                    fourthname = str(classement[3][0])
                    fourthtemp = str(classement[3][1][0])
                    fourthhumi = str(classement[3][1][1])
                    fourthwind = str(classement[3][1][2])
                    fourthprec = str(classement[3][1][3])
                except:
                    print("4e bug")
                    fourthname = ""
                    fourthtemp = ""
                    fourthhumi = ""
                    fourthwind = ""
                    fourthprec = ""
            except:
                print("3e bug")
                thirdname = ""
                thirdtemp = ""
                thirdhumi = ""
                thirdwind = ""
                thirdprec = ""
        except:
            print("2e bug")
            secondname = ""
            secondtemp = ""
            secondhumi = ""
            secondwind = ""
            secondprec = ""
    except:
        print("1er bug")
        firstname = ""
        firsttemp = ""
        firsthumi = ""
        firstwind = ""
        firstprec = ""
    with open(FICHIER_JSON, "w") as file:
        json.dump([], file)  # Écrit une liste vide
    return render_template("cities_result.html", first=firstname, second=secondname, third=thirdname, fourth=fourthname, 
    fi_temp=firsttemp, fi_humi=firsthumi, fi_wind=firstwind, fi_prec=firstprec,
    s_temp=secondtemp, s_humi=secondhumi, s_wind=secondwind, s_prec=secondprec,
    t_temp=thirdtemp, t_humi=thirdhumi, t_wind=thirdwind, t_prec=thirdprec,
    fo_temp=fourthtemp, fo_humi=fourthhumi, fo_wind=fourthwind, fo_prec=fourthprec)

# Charger les villes existantes
def charger_villes():
    try:
        with open(FICHIER_JSON, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []

# Sauvegarder les villes dans le fichier JSON
def sauvegarder_villes(villes):
    with open(FICHIER_JSON, "w", encoding="utf-8") as fichier:
        json.dump(villes, fichier, indent=4, ensure_ascii=False)

@app.route("/add_city", methods=["POST"])
def add_city():
    data = request.get_json()
    ville = data.get("ville")
    print(ville)

    if not ville:
        return jsonify({"message": "Aucune ville reçue"}), 400

    villes = charger_villes()

    if ville in villes:
        print("bug")
        return jsonify({"message": "Cette ville est déjà enregistrée"}), 400

    villes.append(ville)
    sauvegarder_villes(villes)

    return jsonify({"message": f"{ville} ajoutée avec succès !"}), 200


app.run(debug=True)