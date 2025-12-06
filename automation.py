# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "requests",
# ]
# ///
import os
import requests
import shutil
from pathlib import Path

# Load .env file if it exists
env_file = Path(__file__).parent / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

def setup_new_day(day_number):
    day_dir = f"day{day_number}"
    test_file = f"tests/test_{day_number}.py"
    
    session_cookie = os.getenv('AOC_SESSION_COOKIE')
    if not session_cookie:
        print("Session cookie not found. Please set the AOC_SESSION_COOKIE environment variable.")
        return
    
    if not os.path.exists(day_dir):
        url = f"https://adventofcode.com/2025/day/{day_number}/input"
        headers = {'Cookie': f'session={session_cookie}'}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to download input for day {day_number}. Status code: {response.status_code}")
            print(f"Not creating {day_dir} directory.")
            return
        
        # Only create directory and files if input download succeeded
        os.makedirs(day_dir)
        
        with open(os.path.join(day_dir, 'input.txt'), 'w') as f:
            f.write(response.text)
        print(f"Input for day {day_number} downloaded successfully.")
        
        # Create empty test_input.txt for example data
        with open(os.path.join(day_dir, 'test_input.txt'), 'w') as f:
            f.write("# Paste example input from AoC problem here\n")
        
        # Copy and update solution file with correct day number
        with open('day0/solution.py', 'r') as f:
            solution_content = f.read()
        solution_content = solution_content.replace('day0', f'day{day_number}')
        with open(os.path.join(day_dir, 'solution.py'), 'w') as f:
            f.write(solution_content)
        
        # Copy and update test file with correct day number
        with open('day0/test_0.py', 'r') as f:
            test_content = f.read()
        test_content = test_content.replace('day0', f'day{day_number}')
        with open(test_file, 'w') as f:
            f.write(test_content)
        
        print(f"Setup complete for {day_dir}")
    else:
        print(f"{day_dir} already exists")

# Example usage
setup_new_day(3)

# uv run --env-file .env automation.py