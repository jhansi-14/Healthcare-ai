from langgraph.graph import StateGraph
from tools.fitness_tool import analyze_fitness
from tools.nutrition_tool import analyze_nutrition
from tools.symptom_tool import check_symptom

class HealthState(dict):
    pass

def fitness_node(state):

    result = analyze_fitness(
        state["steps"],
        state["calories"],
        state["sleep_hours"]
    )

    state["fitness"] = result
    return state


def nutrition_node(state):

    result = analyze_nutrition(
        state["calories"],
        state["protein"],
        state["carbs"],
        state["fats"]
    )

    state["nutrition"] = result
    return state


def symptom_node(state):

    result = check_symptom(state["symptom"])

    state["symptom_result"] = result
    return state


def build_graph():

    builder = StateGraph(HealthState)

    builder.add_node("fitness", fitness_node)
    builder.add_node("nutrition", nutrition_node)
    builder.add_node("symptom", symptom_node)

    builder.set_entry_point("fitness")

    builder.add_edge("fitness", "nutrition")
    builder.add_edge("nutrition", "symptom")

    return builder.compile()