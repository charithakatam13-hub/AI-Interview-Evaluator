from langchain_core.messages import HumanMessage, AIMessage


def technical_interviewer_node(state, llm):
    prompt = f"""
You are a Technical Interview Agent.

Based on the JD generate:

1. Three technical interview questions
2. Expected answer points
3. Mistakes or blunders to avoid

JD Analysis:
{state['jd_analysis']}

Candidate Info:
{state['candidate_info']}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "technical_evaluation": response.content,
        "messages": [
            AIMessage(
                content=f"Technical Interview Agent Completed:\n{response.content}"
            )
        ]
    }
