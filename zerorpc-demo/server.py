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
    server = zerorpc.Server(Calculator())  # Bind the Calculator class to the server
    server.bind("tcp://0.0.0.0:4242")  # Listen on port 4242
    print("Calculator server running on tcp://0.0.0.0:4242")
    server.run()

if __name__ == "__main__":
    main()
