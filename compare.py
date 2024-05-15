import requests

# Define Jenkins server details
host = "http://140.211.11.144:8080"

# Define job name and build numbers
job_name = "Maven_test"
build_number1 = 1
build_number2 = 2

# Construct URLs for console output of the specified builds
console_output_url1 = f"{host}/job/{job_name}/{build_number1}/consoleText"
console_output_url2 = f"{host}/job/{job_name}/{build_number2}/consoleText"

# Fetch console output for the first build
response1 = requests.get(console_output_url1, auth=(username, password))
if response1.status_code == 200:
    console_output1 = response1.text.splitlines()
else:
    print(f"Failed to fetch console output for build {build_number1}")

# Fetch console output for the second build
response2 = requests.get(console_output_url2, auth=(username, password))
if response2.status_code == 200:
    console_output2 = response2.text.splitlines()
else:
    print(f"Failed to fetch console output for build {build_number2}")

# Filter lines starting with "Tests run"
tests_run_lines1 = [line for line in console_output1 if line.startswith("Tests run")]
tests_run_lines2 = [line for line in console_output2 if line.startswith("Tests run")]

# Print comparison results
for line1, line2 in zip(tests_run_lines1, tests_run_lines2):
    print("In build", build_number1, "I got this:", line1)
    print("In build", build_number2, "I got this:", line2)
