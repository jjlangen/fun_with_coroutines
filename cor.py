def test(x):
    while True:
        inputy = yield
        if x == inputy:
            print(inputy)

test("hi")
