from browser_use import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel
import asyncio
import json
import os

class TestResult(BaseModel):
    test_name: str
    status: str
    steps: list
    screenshot: str = ""
    log: str

class TestRunner:
    def __init__(self, base_url):
        self.base_url = base_url
        
    async def execute_test_case(self, test_case):
        agent = Agent(
            task=self._create_agent_task(test_case),
            llm=ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="AIzaSyAWK4-rjn5UYGRzhU4ZZAMSwj80KZCmdmk"),
            use_vision=True
        )
        
        try:
            result = await agent.run()
            final_result = result.final_result if hasattr(result, 'final_result') else str(result)
            if not isinstance(final_result, str):
                final_result = str(final_result)
            return TestResult(
                test_name=test_case["test_name"],
                status="Passed" if "success" in final_result.lower() else "Failed",
                steps=test_case["steps"],
                log=final_result
            )
        except Exception as e:
            return TestResult(
                test_name=test_case["test_name"],
                status="Failed",
                steps=test_case["steps"],
                log=str(e)
            )
    
    def _create_agent_task(self, test_case):
        task = f"""Test: {test_case['test_name']}
Base URL: {self.base_url}

Steps:"""
        for step in test_case["steps"]:
            task += f"\n- {step['action']} {step['target']}"
            if step.get('value'):
                task += f" with value '{step['value']}'"
            task += f" (Expected: {step['expected']})"
        return task 