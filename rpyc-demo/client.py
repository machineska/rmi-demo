import logging
import rpyc

# Connect to the server
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    try:
        conn = rpyc.connect("localhost", 18861)
        logging.info("5 + 3 = %s", conn.root.add(5, 3))
        logging.info("10 - 7 = %s", conn.root.subtract(10, 7))
        conn.close()
    except Exception as e:
        logging.exception("RPyC client error: %s", e)
