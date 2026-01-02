import logging
import rpyc


# Define a service class
class CalculatorService(rpyc.Service):
    def on_connect(self, conn):
        logging.info("Client connected.")

    def on_disconnect(self, conn):
        logging.info("Client disconnected.")

    # Expose methods remotely
    def exposed_add(self, a, b):
        return a + b

    def exposed_subtract(self, a, b):
        return a - b

# Start the server
if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        server = ThreadedServer(CalculatorService, port=18861)
        logging.info("Calculator server is running on port 18861.")
        server.start()
    except Exception as e:
        logging.exception("RPyC server error: %s", e)
