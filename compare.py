# Provide the URLs of the builds instead of the job name
build_url1 = "http://140.211.11.144:8080/job/Maven_test/1/"
build_url2 = "http://140.211.11.144:8080/job/Maven_test/2/"

# No need to check if the job exists

# No need to check if builds exist

# Retrieve console output directly using the build URLs
console_output1 = get_build_console_output_url(build_url1).splitlines()
console_output2 = get_build_console_output_url(build_url2).splitlines()

# Rest of the code remains the same

tests_run_lines1 = [line for line in console_output1 if line.startswith("Tests run")]
tests_run_lines2 = [line for line in console_output2 if line.startswith("Tests run")]

for line1, line2 in zip(tests_run_lines1, tests_run_lines2):
    print("In build 1, I got this:", line1)
    print("In build 2, I got this:", line2)
