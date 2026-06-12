from langchain_google_genai import ChatGoogleGenerativeAI
from google.colab import userdata

from workflow.graph import create_workflow


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=userdata.get("apikey")
)

app = create_workflow(llm)

job_description = input(
    "Paste the Job Description:\n"
)

candidate_info = input(
    "\nEnter candidate skills, projects, experience:\n"
)

initial_state = {
    "messages": [],
    "job_description": job_description,
    "candidate_info": candidate_info,
    "jd_analysis": "",
    "experience_mapping": "",
    "behavioral_evaluation": "",
    "technical_evaluation": "",
    "final_report": ""
}

result = app.invoke(initial_state)

print("\n" + "=" * 60)
print("FINAL INTERVIEW REPORT")
print("=" * 60)
print(result["final_report"])
