import logging
from xmlrpc.server import SimpleXMLRPCServer


# Define methods
def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


# Set up the server
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        server = SimpleXMLRPCServer(("localhost", 9000))
        logging.info("XML-RPC Server is running on port 9000...")
        server.register_function(add, "add")
        server.register_function(subtract, "subtract")
        server.serve_forever()
    except Exception as e:
        logging.exception("XML-RPC server error: %s", e)


if __name__ == "__main__":
    main()
