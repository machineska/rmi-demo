import rpyc


# Define a service class
class CalculatorService(rpyc.Service):
    def on_connect(self, conn):
        print("Client connected.")

    def on_disconnect(self, conn):
        print("Client disconnected.")

    # Expose methods remotely
    def exposed_add(self, a, b):
        return a + b

    def exposed_subtract(self, a, b):
        return a - b

# Start the server
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer

    server = ThreadedServer(CalculatorService, port=18861)
    print("Calculator server is running on port 18861.")
    server.start()
