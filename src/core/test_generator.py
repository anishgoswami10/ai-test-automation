from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import json

class TestGenerator:
    def __init__(self, model_name="gemini-2.0-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model_name)
        
    def generate_from_text(self, scenario_text):
        prompt = ChatPromptTemplate.from_template(
            """Convert this test scenario into executable test cases:
            {scenario}
            
            Output format:
            {{
                "test_name": string,
                "steps": [
                    {{
                        "action": string,
                        "target": string,
                        "value": string,
                        "expected": string
                    }}
                ]
            }}"""
        )
        
        chain = prompt | self.llm
        response = chain.invoke({"scenario": scenario_text})
        return json.loads(response.content) 