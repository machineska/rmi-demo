import grpc
import calculator_pb2
import calculator_pb2_grpc


# Connect to the server and call methods
def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    # Call the Add method
    response = stub.Add(calculator_pb2.Numbers(a=5, b=3))
    print("5 + 3 =", response.result)

    # Call the Subtract method
    response = stub.Subtract(calculator_pb2.Numbers(a=10, b=7))
    print("10 - 7 =", response.result)


if __name__ == '__main__':
    main()
