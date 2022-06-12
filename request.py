import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("ipc://temp")

while True:
  request = "REQUEST"
  socket.send(request.encode())
  print("Sent:", request)
  response = socket.recv()
  print("Recieved:", response.decode(),"\n")
  time.sleep(1)
