import jenkins

host = "http://140.211.11.144:8080"
username = "robin_jain"
password = "Robin@0206"

server = jenkins.Jenkins(host, username=username, password=password)

job_name = "Maven_test"
build_number1 = 1
build_number2 = 2

job_exist = server.job_exists(job_name)

if job_exist:
    build1_exists = server.get_build_info(job_name, build_number1)
    build2_exists = server.get_build_info(job_name, build_number2)
    
    if build1_exists and build2_exists:
        console_output1 = server.get_build_console_output(job_name, build_number1).splitlines()
        console_output2 = server.get_build_console_output(job_name, build_number2).splitlines()
        
        tests_run_lines1 = [line for line in console_output1 if line.startswith("Tests run")]
        tests_run_lines2 = [line for line in console_output2 if line.startswith("Tests run")]
        
        for line1, line2 in zip(tests_run_lines1, tests_run_lines2):
            print("In build", build_number1, "I got this:", line1)
            print("In build", build_number2, "I got this:", line2)
    else:
        if not build1_exists:
            print(f"Build {build_number1} not found for job {job_name}.")
        if not build2_exists:
            print(f"Build {build_number2} not found for job {job_name}.")
else:
    print("Job not found!")
