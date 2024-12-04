import zerorpc


# Connect to the server
def main():
    client = zerorpc.Client()
    client.connect("tcp://127.0.0.1:4242")  # Connect to the server

    # Call remote methods
    print("5 + 3 =", client.add(5, 3))
    print("10 - 7 =", client.subtract(10, 7))


if __name__ == "__main__":
    main()
