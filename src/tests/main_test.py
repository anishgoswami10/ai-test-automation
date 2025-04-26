import asyncio
import json
import os
from src.core.test_runner import TestRunner
from src.core.reporter import HTMLReporter

async def main():
    # Load test cases
    test_cases = [
        {
            "test_name": "Valid Login and Checkout",
            "steps": [
                {
                    "action": "Navigate to",
                    "target": "https://www.saucedemo.com/",
                    "expected": "Login page should load"
                },
                {
                    "action": "Enter text",
                    "target": "username field",
                    "value": "standard_user",
                    "expected": "Username entered"
                },
                {
                    "action": "Enter text",
                    "target": "password field",
                    "value": "secret_sauce",
                    "expected": "Password entered"
                },
                {
                    "action": "Click",
                    "target": "login button",
                    "expected": "Inventory page should load"
                },
                {
                    "action": "Click",
                    "target": "add to cart button for first item",
                    "expected": "Item added to cart"
                },
                {
                    "action": "Click",
                    "target": "shopping cart icon",
                    "expected": "Cart page should load"
                },
                {
                    "action": "Click",
                    "target": "checkout button",
                    "expected": "Checkout page should load"
                }
            ]
        }
    ]
    
    # Initialize components
    runner = TestRunner(base_url="https://www.saucedemo.com/")
    reporter = HTMLReporter()
    
    # Execute tests
    results = []
    for case in test_cases:
        print(f"\nExecuting test: {case['test_name']}")
        result = await runner.execute_test_case(case)
        results.append(result)
        print(f"Status: {result.status}")
        print(f"Log: {result.log}")
    
    # Generate report
    report_path = reporter.generate(results)
    print(f"\nReport generated: {report_path}")

if __name__ == "__main__":
    asyncio.run(main()) 