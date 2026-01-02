import logging
import xmlrpc.client


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
        logging.info("5 + 3 = %s", proxy.add(5, 3))
        logging.info("10 - 7 = %s", proxy.subtract(10, 7))
    except Exception as e:
        logging.exception("XML-RPC client error: %s", e)


if __name__ == "__main__":
    main()
