import sys
import random
import secrets
import string
import json


def generate_pw(length):
    deadbolt = []
    for _x in range(0, length):
        if random.randrange(1, 8) == 1:
            deadbolt.append(secrets.choice(string.ascii_uppercase))
        elif random.randrange(1, 10) == 1:
            deadbolt.append(secrets.choice(string.digits))
        else:
            deadbolt.append(secrets.choice(string.ascii_lowercase))
    deadbolt = ''.join(deadbolt)
    if length <= 10:
        cut = int(length / 2)
        deadbolt = deadbolt[:cut] + '-' + deadbolt[cut:-1]
    elif 10 <= length <= 32:
        cut = int(length / 3)
        deadbolt = deadbolt[:cut] + '-' + deadbolt[cut:cut * 2] + '-' + deadbolt[(cut * 2):-2]
    else:
        cut = int(length / 4)
        deadbolt = deadbolt[:cut] + '-' + deadbolt[cut:cut * 2] + '-' + deadbolt[cut * 2:cut * 3] + '-' + deadbolt[cut * 3:-3]
    alfred_output(deadbolt)
    
def alfred_output(deadbolt):
    response = json.dumps({"items": [{'title': deadbolt, 'subtitle': f"Length: {len(deadbolt)} characters", 'arg': deadbolt}]})
    sys.stdout.write(response)


if __name__ == '__main__':
    length = sys.argv[1]
    if length.isdigit():
        generate_pw(int(length))
    else:
        generate_pw(length=20)
