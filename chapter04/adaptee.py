class Target:
    def request(self):
        print('common request')


class Adapter(Target):
    def __init__(self):
        super().__init__()
        self.adaptee = self.Adaptee()

    def request(self):
        self.adaptee.specific_request()

    class Adaptee:
        def specific_request(self):
            print('special request')


if __name__ == "__main__":
    target = Adapter()
    target.request()
