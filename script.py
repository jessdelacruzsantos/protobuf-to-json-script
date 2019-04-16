import sys
import subprocess
import json

if len(sys.argv) < 1:
    print (sys.argv)
    sys.exit()
else :
    fileLocation = sys.argv[0]

result = subprocess.call(['protobuf-jsonschema','test.proto'])


print(result)
