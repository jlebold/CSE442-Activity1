import hello
import agree

hello.hello()
hello.hello2()
agree.strongly_agree_with("EVERYONE")


# Run through every single last thing in the hello module, and try to execute it >:)
for thing in dir(hello):
    try:
        thing()
        print("Successfully executed thing: %s" % str(thing))
    except TypeError:
        print("Could not execute thing: %s. (TypeError)" % str(thing))




























hello.helloMemeBoi()
hello.goodbye()









hello.benchmark()

>>>>>>> e4b89b5ff3d29dc36a52fa1cf0ad4e7734c22693
