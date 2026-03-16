def generate_report(results):

    report = f"""
    Health Summary Report

    Fitness Score: {results['fitness']}
    Nutrition Analysis: {results['nutrition']}
    Symptom Assessment: {results['symptom_result']}

    Recommendations:
    - Maintain balanced diet
    - Regular exercise
    - Consult doctor if symptoms persist
    """

    return report