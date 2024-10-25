st='зеленый-красный-желтый-черный-белый'
def sort_col(st):        
    l=st.split("-")
    return ("-").join(sorted(l))
print(sort_col(st))
print("--")
code="""
def sq():
    l=[i**2 for i in range(1,31)]
    return l
print(sq())
"""
exec(code)
print(sort_col.__code__.co_nlocals)
def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped
def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"
