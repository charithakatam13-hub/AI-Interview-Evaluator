from langchain_core.messages import HumanMessage, AIMessage


def experience_mapper_node(state, llm):
    prompt = f"""
You are an Experience Mapper Agent.

Compare the candidate information with the JD analysis.

Candidate Info:
{state['candidate_info']}

JD Analysis:
{state['jd_analysis']}

Find:

1. Candidate strengths
2. Skill gaps
3. Matching projects/experience
4. How candidate should present themselves
5. Two personalized interview questions
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "experience_mapping": response.content,
        "messages": [
            AIMessage(
                content=f"Experience Mapper Completed:\n{response.content}"
            )
        ]
    }
