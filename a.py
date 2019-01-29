class A:
    def a1(self):
        print("hello world")
class B(A):
    def a2(self):
        print("of")
class C(B,A):
    def a3(self):
        print("python")
c=C()
c.a1()
c.a2()
c.a3()
        
