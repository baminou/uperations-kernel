


class Documentable:

    @classmethod
    def name(cls):
        return cls

    @classmethod
    def description(cls):
        return str(cls)