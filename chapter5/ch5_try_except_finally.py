class Bird:
    def fly(self):
        raise NotImplemented


class Eagle(Bird):
    pass


eagle = Eagle()
eagle.fly()
