from github_grabber import json_data


class MetaUpdater(type):
    def __new__(cls, basename, basics, dict):
        json_data.update({'__getattr__': cls.__getattr__})
        return super().__new__(cls, basename, basics, json_data)

    def __getattr__(self, item):
        assert self.__dict__.get(item), "Not implemented attribute"


class HeroLoader(metaclass=MetaUpdater):
    CLASS_VAR = 10

    def __init__(self):
        self.__class__.attr2 = 2
        # self.__dict__.update(data)


hero = HeroLoader()
print(hero.age)
pass
