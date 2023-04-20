import os
import re
import json

class MyCollection:
    def __init__(self, user):
        self.user = user
        self.set = set()
        self.filename = f"{user}.json"

    def add(self, key):
        self.set.add(key)

    def remove(self, key):
        self.set.remove(key)

    def find(self, key):
        print(key if key in self.set else "No such element")

    def list(self):
        for i in self.set:
            print(i)

    def grep(self, regex):
        res = list(filter(lambda x: re.match(regex, x), self.set))
        print(res if len(res) > 0 else "No such elements")
              
    def save(self):
        with open(self.filename, "w") as storage_file:
            json.dump(list(self.set), storage_file)

    def load(self):
        with open(self.filename, "r") as storage_file:
            self.set.update(json.load(storage_file))

    def switch(self, user):
        self.user = user
        self.filename = f"{user}.json"
        self.set = set()

