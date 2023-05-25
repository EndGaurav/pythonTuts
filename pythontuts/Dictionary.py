# Dictionary is nothing but like a object in js.
# key:value
# case sensitive.
from builtins import print

d1 = {
    "fname": "gaurav",
    "lname": "jethuri",
    "age": {
        "teenager": 16,
        "Adult": 23,
        "men": 35
    }
}
print(d1["fname"])

# Adding key value in dictionary
# d1["divyansh"] = "thakur"
# d1["AKash"] = "Yadav"
# print(d1)

# Deleting key
# del d1["AKash"]
# print(d1)

# Accessing key from the dictionary
# print(d1["age"]["teenager"]);

# some function of the dictionary
# d2 = d1.copy()
# del d2["age"]
# print(d2)
# print(d1)
# d1.pop("lname")
# print(d1)
# d1.update({"hobby": "scrolling"})

# print(d1.keys())
# print(d1.items())