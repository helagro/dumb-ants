import sys

DEBUG_LEVEL = 5

logImportanceAllowed = 5

def log(*msg):
    print(msg, flush=True)
    sys.stdout.flush()