def analyze_symptoms(symptoms):

    mapping = {
        "fever": "Possible infection",
        "headache": "Possible dehydration",
        "fatigue": "Possible low iron"
    }

    results = []

    for s in symptoms:
        if s in mapping:
            results.append(mapping[s])

    return results