

def spam():
    print("Hello from spam()")

# 'private' function
def _ham():
    print("HAM HAM HAM")

def toast():
    print("Hello from toast()")
    _ham()

