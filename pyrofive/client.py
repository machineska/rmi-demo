import logging
import Pyro5.api


# Connect to the remote object
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        calculator = Pyro5.api.Proxy("PYRONAME:example.calculator")
        logging.info("5 + 3 = %s", calculator.add(5, 3))
        logging.info("10 - 7 = %s", calculator.subtract(10, 7))
    except Exception as e:
        logging.exception("Pyro5 client error: %s", e)


if __name__ == "__main__":
    main()
