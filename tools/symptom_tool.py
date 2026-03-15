symptom_database = {
    "fever": "Possible infection",
    "headache": "Migraine or stress",
    "chest pain": "Consult doctor immediately"
}

def check_symptom(symptom):

    symptom = symptom.lower()

    if symptom in symptom_database:
        return symptom_database[symptom]

    return "No information available"