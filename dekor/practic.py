def fun_dekor(fn):
    print("Start")
    fn()
    print("Finish")

@fun_dekor
def fun():
    print("1")

@fun_dekor
def fun_2():
    print("2")




