from langchain_core.messages import HumanMessage, AIMessage


def behavioral_interviewer_node(state, llm):
    prompt = f"""
You are a Behavioral Interview Agent.

Based on the candidate profile and JD generate:

1. Two behavioral interview questions
2. What a good answer should include
3. Common mistakes candidate may make

Candidate Info:
{state['candidate_info']}

JD Analysis:
{state['jd_analysis']}

Experience Mapping:
{state['experience_mapping']}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "behavioral_evaluation": response.content,
        "messages": [
            AIMessage(
                content=f"Behavioral Interview Agent Completed:\n{response.content}"
            )
        ]
    }
