import logging
import zerorpc


# Connect to the server
def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        client = zerorpc.Client()
        client.connect("tcp://127.0.0.1:4242")
        logging.info("5 + 3 = %s", client.add(5, 3))
        logging.info("10 - 7 = %s", client.subtract(10, 7))
    except Exception as e:
        logging.exception("ZeroRPC client error: %s", e)


if __name__ == "__main__":
    main()
