

class A:
    def __init__(self) -> None:
        print("A")

class B:
    def __init__(self) -> None:
        print("B")

class C(A, B):
    def __init__(self) -> None:
        # super().__init__()
        print(super().__init__())

    def name(self):
        pass



x = C()

(C()).name()

C().name()