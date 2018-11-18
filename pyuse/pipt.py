
from subprocess import Popen, PIPE

p = Popen(['pip', 'list'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, err = p.communicate(b"input data that is passed to subprocess' stdin")
rc = p.returncode

print(output.decode("utf-8"))

