import sys

logImportanceAllowed = 5

def log(importance, *msg):
    if logImportanceAllowed >= importance:
        print(msg)
        sys.stdout.flush()