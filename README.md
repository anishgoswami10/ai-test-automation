# AI Test Automation

This project demonstrates automated browser testing using AI-powered agents. It uses the `browser-use` package along with Gemini AI to perform end-to-end testing of web applications.

## Features

- AI-powered browser automation
- Natural language test case definitions
- Automatic test execution and reporting
- Integration with Gemini AI for intelligent browser interactions

## Prerequisites

- Python 3.x
- Gemini API key
- Required Python packages (see requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/anishgoswami10/myrepo.git
cd myrepo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Running Tests

To run the test suite:
```bash
python -m src.tests.main_test
```

The test results will be generated in the `reports` directory as HTML files.

## Project Structure

- `src/core/`: Core functionality
  - `test_runner.py`: Test execution engine
  - `reporter.py`: HTML report generation
- `src/tests/`: Test cases
  - `main_test.py`: Example test suite

## License

MIT License 