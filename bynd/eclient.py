import errno
import select
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 1234))
sock.setblocking(0)  # non-blocking socket

data = 'foobar\n' * 1024 * 1024
data_size = len(data)
print ('Bytes to send: ', len(data))

total_sent = 0
while len(data):
    try:
        sent = sock.send(str.encode(data, 'utf-8'))
        total_sent += sent
        data = data[sent:]
        print ('Sending data')
    except socket.error as e:
        if e.errno != errno.EAGAIN:
            raise e
        print ('Blocking with', len(data), 'remaining')
        select.select([], [sock], [])  # This blocks until

assert total_sent == data_size  # True

"""
# select() expects three arguments #
- list of file descriptors to watch for reading,
- list of file descriptors to watch for writing,
- list of file descriptors to watch for errors.
- Timeout can be passed as an optional 4th argument which can be used
  to prevent select() from blocking indefinitely.

It returns a subset of all the three lists passed in the same order
i.e. all the file descriptors that are ready for reading, writing or have caused some error.
"""
