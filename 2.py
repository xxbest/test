def count():
    def f(j):
            def g():
                    return j*j
            return g
    fs = []
    for i in range(1,4):
            fs.append(g()) #f(i)立即被执行，变量i的当前值被传入f()
    return fs
	
f1,f2,f3 = count()

print(f1())