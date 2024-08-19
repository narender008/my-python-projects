class bird:
    def info(self):
        print("this is main class info function")

    def flight(self):
        print("some birds fly some dont")


class sparrow(bird):
    def flight(self):
        print("sparrow fly and very small")


class ostrich(bird):
    def flight(self):
        print("ostrich dont fly and very large")


obj_bird = bird()
obj_bird.info()
obj_bird.flight()

obj_sparrow = sparrow()
obj_sparrow.info()
obj_sparrow.flight()
