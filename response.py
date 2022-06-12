import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("ipc://temp")

while True:
  request = socket.recv()
  print("Recieved:", request.decode())
  response = "RESPONSE"
  socket.send(response.encode())
  print("Sent:", response,"\n")
