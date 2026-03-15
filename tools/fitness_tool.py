def analyze_fitness(steps,calories,sleep_hours):
    score=(steps/10000)*40+(sleep_hours/8)*30+(calories/2000)*30
    if score>80:
        status="excellent"
    elif score>60:
        status="good"
    else:
        status="needs improvement"
    return{
        "fitness_score":score,
        "status":status
    }            