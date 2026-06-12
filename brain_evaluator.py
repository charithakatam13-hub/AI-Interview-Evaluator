from langchain_core.messages import HumanMessage, AIMessage


def brain_evaluator_node(state, llm):
    prompt = f"""
You are the Brain Evaluator Agent.

Prepare a final interview preparation report.

Candidate Info:
{state['candidate_info']}

JD Analysis:
{state['jd_analysis']}

Experience Mapping:
{state['experience_mapping']}

Behavioral Evaluation:
{state['behavioral_evaluation']}

Technical Evaluation:
{state['technical_evaluation']}

Include:

1. Readiness score /100
2. JD match score
3. Communication readiness
4. Technical readiness
5. Strengths
6. Weaknesses
7. Mistakes to avoid
8. Serious blunders
9. Final preparation strategy
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "final_report": response.content,
        "messages": [
            AIMessage(
                content=f"Brain Evaluator Completed:\n{response.content}"
            )
        ]
    }
