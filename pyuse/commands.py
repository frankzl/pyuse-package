from subprocess import Popen, PIPE

python_versions = ["python2",
        "python2.1",
        "python2.2",
        "python2.3",
        "python2.4",
        "python2.5",
        "python2.6",
        "python2.7",
        "python2.8",
        "python2.9",
        "python3",
        "python3.1",
        "python3.2",
        "python3.3",
        "python3.4",
        "python3.5",
        "python3.6",
        "python3.7",
        ]

def execute(command):
    commands = command.split(' ')
    p = Popen(commands, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # rc = p.returncode
    return (output.decode("utf-8"))

def exists(python_version):
    output = execute("which " + python_version)
    path = (output.split("\n")[0])
    if "/" in path:
        return path
    return None

def get_versions():
    versions = []
    for version in python_versions:
        path = exists(version)
        if path != None:
            versions.append(path)
    return versions

# execute("pip list")
# print(execute("which python2"))
print(get_versions())
