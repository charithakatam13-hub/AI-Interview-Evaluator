from langchain_core.messages import HumanMessage, AIMessage


def jd_analyst_node(state, llm):
    prompt = f"""
You are a JD Analyst Agent.

Analyze this job description and extract:

1. Role title
2. Required skills
3. Responsibilities
4. Experience level
5. Important keywords
6. What the interviewer may focus on

Job Description:
{state['job_description']}
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "jd_analysis": response.content,
        "messages": [
            AIMessage(
                content=f"JD Analyst Completed:\n{response.content}"
            )
        ]
    }
