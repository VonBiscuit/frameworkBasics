
class A:

    def __init__(st, b):
        st.b = b

    def display(st):
        print(st.b)


a = A("test")
a.display()
A.display(a)