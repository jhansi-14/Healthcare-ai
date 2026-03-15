def health_agent(query:str):
    if "medicine" in query:
        return "Remember to take medicine"
    elif "heart" in query:
        return "Heart rate monitoring active"
    else:
        return "Monitoring health data"    
