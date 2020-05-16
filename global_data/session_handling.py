
file_handling = 'hello_world.txt'
f = open(file_handling, 'r')
print(f.read().splitlines())
f.close()
f = open('helloworld2.txt','w')
f.write('hello world 2')
f.close()
