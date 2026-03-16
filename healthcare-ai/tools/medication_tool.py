medication_interactions = {
    ("aspirin", "ibuprofen"): "Risk of stomach bleeding",
    ("paracetamol", "alcohol"): "Liver damage risk"
}

def check_medication_interaction(med1, med2):

    pair = (med1.lower(), med2.lower())

    if pair in medication_interactions:
        return medication_interactions[pair]

    return "No known interaction"