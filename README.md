# AI Interview Evaluator

A Multi-Agent AI Interview Preparation System built using LangGraph, LangChain, and Google's Gemini 2.5 Flash model.

## Overview

This project helps candidates prepare for interviews by analyzing a Job Description (JD) and comparing it with a candidate's profile. Multiple AI agents collaborate to generate interview questions, identify strengths and weaknesses, and provide a comprehensive preparation strategy.

The system follows a multi-agent architecture where each agent is responsible for a specific task.

---

## Architecture

```text
Candidate Profile + Job Description
                │
                ▼
        JD Analyst Agent
                │
                ▼
     Experience Mapper Agent
                │
                ▼
 Behavioral Interview Agent
                │
                ▼
 Technical Interview Agent
                │
                ▼
      Brain Evaluator Agent
                │
                ▼
      Final Interview Report
```

---

## Agents

### 1. JD Analyst Agent

Analyzes the Job Description and extracts:

* Role Title
* Required Skills
* Responsibilities
* Experience Requirements
* Important Keywords
* Interview Focus Areas

---

### 2. Experience Mapper Agent

Compares candidate experience against the JD.

Outputs:

* Candidate Strengths
* Skill Gaps
* Relevant Projects
* Experience Alignment
* Personalized Interview Questions

---

### 3. Behavioral Interview Agent

Generates behavioral interview preparation.

Outputs:

* Behavioral Questions
* Ideal Answer Guidelines
* Common Behavioral Mistakes

---

### 4. Technical Interview Agent

Creates role-specific technical interview questions.

Outputs:

* Technical Questions
* Expected Answer Points
* Technical Mistakes to Avoid

---

### 5. Brain Evaluator Agent

Combines all previous analyses and generates a final report.

Outputs:

* Candidate Readiness Score
* JD Match Score
* Communication Readiness
* Technical Readiness
* Strengths
* Weaknesses
* Preparation Strategy

---

## Features

* Multi-Agent Workflow using LangGraph
* Gemini 2.5 Flash Integration
* Job Description Analysis
* Candidate Profile Evaluation
* Behavioral Interview Preparation
* Technical Interview Preparation
* Final Interview Readiness Report
* Modular Architecture

---

## Project Structure

```text
ai-interview-evaluator/
│
├── main.py
├── state.py
├── requirements.txt
│
├── agents/
│   ├── jd_analyst.py
│   ├── experience_mapper.py
│   ├── behavioral_interviewer.py
│   ├── technical_interviewer.py
│   └── brain_evaluator.py
│
└── workflow/
    └── graph.py
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langgraph
pip install langchain
pip install langchain-core
pip install langchain-google-genai
pip install google-generativeai
```

---

## API Key Setup

### Google Colab

Store your Gemini API Key in Colab Secrets.

Secret Name:

```text
apikey
```

Access it using:

```python
from google.colab import userdata

userdata.get("apikey")
```

---

## Running the Project

```bash
python main.py
```

Input:

1. Job Description
2. Candidate Skills, Projects, and Experience

The system will automatically run all agents and generate a final interview preparation report.

---

## Example Output

```text
Overall Readiness Score: 87/100

JD Match Score: 90/100

Strengths:
- Strong Python Development
- Experience with LangChain
- Good Problem Solving

Weaknesses:
- Limited Cloud Deployment Experience

Communication Readiness:
8/10

Technical Readiness:
9/10

Mistakes to Avoid:
- Giving generic answers
- Not quantifying achievements

Final Preparation Strategy:
Focus on system design, cloud concepts,
and project impact storytelling.
```

---

## Technologies Used

* Python
* LangGraph
* LangChain
* Google Gemini 2.5 Flash
* Multi-Agent AI Systems

---

## Future Enhancements

* Resume Upload (PDF)
* ATS Score Calculation
* Resume Parsing
* Interactive Mock Interviews
* Streamlit Web Interface
* Vector Database Integration
* RAG-based Interview Preparation

---

## Learning Outcomes

This project demonstrates:

* Multi-Agent System Design
* LangGraph Workflows
* Prompt Engineering
* LLM Orchestration
* State Management
* AI-Powered Interview Preparation

---

## Author

Charitha Katam

Built as an AI Engineering and LangGraph portfolio project.
