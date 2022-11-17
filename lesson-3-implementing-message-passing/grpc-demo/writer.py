import grpc
import order_pb2
import order_pb2_grpc

"""
Sample implementation of a writer that can be used to write messages to gRPC.
"""

print("Sending sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = order_pb2_grpc.OrderServiceStub(channel)

# Update this with desired payload
order = order_pb2.OrderMessage(
    id="1",
    created_by="mbehadir",
    status="PROCESSING",
    created_at="2021-07-16 19:17:20.536991",
    equipment=["KEYBOARD", "MOUSE"]
)


response = stub.Create(order)