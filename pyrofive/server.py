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
    daemon = Pyro5.api.Daemon()  # Start Pyro daemon
    ns = Pyro5.api.locate_ns()  # Locate the Pyro name server

    uri = daemon.register(Calculator)  # Register the Calculator class
    ns.register("example.calculator", uri)  # Register the object in the name server

    print("Calculator server is ready.")
    daemon.requestLoop()  # Start the event loop


if __name__ == "__main__":
    # run `python -m Pyro5.nameserver` then start this server
    main()
