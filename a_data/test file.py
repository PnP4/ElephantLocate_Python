
from nanomsg import Socket
s1 = Socket('PAIR')
s2 = Socket('PAIR')
s1.bind('inproc://bob')
s2.connect('inproc://bob')
s1.send(b'hello nanomsg')
print(s2.recv())
s1.close()
s2.close()