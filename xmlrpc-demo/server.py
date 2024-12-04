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
    server = SimpleXMLRPCServer(("localhost", 9000))
    print("XML-RPC Server is running on port 9000...")

    # Register functions
    server.register_function(add, "add")
    server.register_function(subtract, "subtract")

    # Run the server
    server.serve_forever()


if __name__ == "__main__":
    main()
