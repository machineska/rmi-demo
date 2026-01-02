import logging
import grpc
import calculator_pb2
import calculator_pb2_grpc


# Connect to the server and call methods
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.Numbers(a=5, b=3))
        logging.info("5 + 3 = %s", response.result)
        response = stub.Subtract(calculator_pb2.Numbers(a=10, b=7))
        logging.info("10 - 7 = %s", response.result)
    except Exception as e:
        logging.exception("gRPC client error: %s", e)


if __name__ == '__main__':
    main()
