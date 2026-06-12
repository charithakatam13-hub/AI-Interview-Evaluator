from langgraph.graph import StateGraph, END

from state import InterviewState

from agents.jd_analyst import jd_analyst_node
from agents.experience_mapper import experience_mapper_node
from agents.behavioral_interviewer import behavioral_interviewer_node
from agents.technical_interviewer import technical_interviewer_node
from agents.brain_evaluator import brain_evaluator_node


def create_workflow(llm):

    workflow = StateGraph(InterviewState)

    workflow.add_node(
        "jd_analyst",
        lambda state: jd_analyst_node(state, llm)
    )

    workflow.add_node(
        "experience_mapper",
        lambda state: experience_mapper_node(state, llm)
    )

    workflow.add_node(
        "behavioral_interviewer",
        lambda state: behavioral_interviewer_node(state, llm)
    )

    workflow.add_node(
        "technical_interviewer",
        lambda state: technical_interviewer_node(state, llm)
    )

    workflow.add_node(
        "brain_evaluator",
        lambda state: brain_evaluator_node(state, llm)
    )

    workflow.set_entry_point("jd_analyst")

    workflow.add_edge("jd_analyst", "experience_mapper")
    workflow.add_edge("experience_mapper", "behavioral_interviewer")
    workflow.add_edge("behavioral_interviewer", "technical_interviewer")
    workflow.add_edge("technical_interviewer", "brain_evaluator")
    workflow.add_edge("brain_evaluator", END)

    return workflow.compile()
