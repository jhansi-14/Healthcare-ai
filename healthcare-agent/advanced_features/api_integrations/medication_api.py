def check_drug_interaction(drug1, drug2):

    interactions = {
        ("aspirin", "ibuprofen"): "Increased bleeding risk"
    }

    if (drug1, drug2) in interactions:
        return interactions[(drug1, drug2)]

    return "No known interaction"