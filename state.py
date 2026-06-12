from typing import TypedDict, Annotated
import operator

class InterviewState(TypedDict):
    messages: Annotated[list, operator.add]
    job_description: str
    candidate_info: str
    jd_analysis: str
    experience_mapping: str
    behavioral_evaluation: str
    technical_evaluation: str
    final_report: str
