import xmlrpc.client


def main():
    # Connect to the server
    proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

    # Call remote methods
    print("5 + 3 =", proxy.add(5, 3))
    print("10 - 7 =", proxy.subtract(10, 7))


if __name__ == "__main__":
    main()
