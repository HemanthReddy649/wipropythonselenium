#subprocess module -
# execute external system commands
#Iteract with os processess
#capture output,error and return codes
#control the process execution

#run the os level commands - linux , macos , windows


import subprocess

#subprocess.run()-run command and wait
#subprocess.popen()-run process synchronusly
#subprocess.PIPE - capture the outpur
#subprocess.completeProcess - result
#subprocess.timeoutExpired-Time outexecption
#subprocess.calledprocessError - command failure

result = subprocess.run("dir", shell=True, capture_output=True,text=True)
print(result)

result = subprocess.run("ipconfig", shell=True, capture_output=True,text=True)
print(result)

result = subprocess.run("python --version", shell=True, capture_output=True,text=True)
print(result.stdout)
print(result.stderr)