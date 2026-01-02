import logging
import Pyro5.api


# Define a class to expose remotely
@Pyro5.api.expose
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


# Start the Pyro server
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        daemon = Pyro5.api.Daemon()
        ns = Pyro5.api.locate_ns()
        uri = daemon.register(Calculator)
        ns.register("example.calculator", uri)
        logging.info("Calculator server is ready.")
        daemon.requestLoop()
    except Exception as e:
        logging.exception("Pyro5 server error: %s", e)


if __name__ == "__main__":
    main()
