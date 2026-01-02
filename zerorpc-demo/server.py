import logging
import zerorpc


# Define a service class
class Calculator:
    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract two numbers."""
        return a - b

# Start the server
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        server = zerorpc.Server(Calculator())
        server.bind("tcp://0.0.0.0:4242")
        logging.info("Calculator server running on tcp://0.0.0.0:4242")
        server.run()
    except Exception as e:
        logging.exception("ZeroRPC server error: %s", e)

if __name__ == "__main__":
    main()
