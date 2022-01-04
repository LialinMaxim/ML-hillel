import logging
import pickle
import json
import pprint
import logging as log
#
# LEVEL = 40  # Error
log.basicConfig(format='%(asctime)s: %(module)s: %(levelname)s: %(message)s', level=logging.ERROR)

a = "abc"
b = 10554
c = 10, 1547, "sdfhbvhs"

data = [a, b, c]

str_var = pickle.dumps(data)
object_str = pickle.loads(str_var)
log.info("Data loaded ...")

# with open("pickle.conf", 'w') as file:
#     pickle.dump(data, file)

with open("pickle.conf", 'rb') as file:
    object = pickle.load(file)

str_json = """[10, 20, "hello", {
    "10": "Jane", 
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}]"""

x = json.loads(str_json)[-1]
x[10] = "abc"


with open("json.conf", 'w', encoding='utf8') as file:
    json.dump(x, file, indent=3)

try:
    with open("json_dump.conf", 'r', encoding='utf8') as file:
        object = json.load(file)
        # print("Debug msg:")
        # pprint.pprint(object)
except FileNotFoundError:
    # print("File json_dump.conf not found!")
    log.warning("File json_dump.conf not found!")

try:
    with open("jsond.conf", 'r', encoding='utf8') as file:
        object = json.load(file)
except FileNotFoundError as exec:
    # print("Critical issue", exec)
    log.critical(exec)
    exit(1)

# print("Debug msg:")
# pprint.pprint(object)
log.debug(object)

log.info('Done!')






