from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc


# Implement the service
class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calculator_pb2.Result(result=result)

    def Subtract(self, request, context):
        result = request.a - request.b
        return calculator_pb2.Result(result=result)


# Start the gRPC server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:50051')
    print("Calculator server is running on port 50051.")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
