from datetime import datetime
import json
import os

class HTMLReporter:
    def generate(self, results, report_dir="reports"):
        html = """
        <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    padding: 8px;
                    text-align: left;
                    border: 1px solid #ddd;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                .passed {{
                    color: green;
                }}
                .failed {{
                    color: red;
                }}
                .steps {{
                    white-space: pre-line;
                }}
            </style>
        </head>
        <body>
            <h1>Test Automation Report</h1>
            <p>Generated: {date}</p>
            <table>
                <tr>
                    <th>Test Name</th>
                    <th>Status</th>
                    <th>Steps</th>
                    <th>Log</th>
                </tr>
        """.format(date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        for result in results:
            html += f"""
                <tr>
                    <td>{result.test_name}</td>
                    <td class="{'passed' if result.status == 'Passed' else 'failed'}">
                        {result.status}
                    </td>
                    <td class="steps">{self._format_steps(result.steps)}</td>
                    <td>{result.log}</td>
                </tr>
            """
        
        html += "</table></body></html>"
        
        os.makedirs(report_dir, exist_ok=True)
        report_path = os.path.join(report_dir, f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
        with open(report_path, "w") as f:
            f.write(html)
        return report_path
    
    def _format_steps(self, steps):
        return "<br>".join([
            f"{step['action']} {step['target']} "
            f"({step.get('value', '')})<br>"
            f"Expected: {step.get('expected', 'N/A')}"
            for step in steps
        ]) 