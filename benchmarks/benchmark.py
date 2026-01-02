import argparse
import time
import statistics
import xmlrpc.client
import zerorpc


def bench_xmlrpc(host="localhost", port=9000, iterations=100):
    proxy = xmlrpc.client.ServerProxy(f"http://{host}:{port}/")
    latencies = []
    for _ in range(iterations):
        t0 = time.perf_counter()
        proxy.add(5, 3)
        latencies.append(time.perf_counter() - t0)
    return latencies


def bench_zerorpc(host="127.0.0.1", port=4242, iterations=100):
    client = zerorpc.Client()
    client.connect(f"tcp://{host}:{port}")
    latencies = []
    for _ in range(iterations):
        t0 = time.perf_counter()
        client.add(5, 3)
        latencies.append(time.perf_counter() - t0)
    return latencies


def summarize(name, latencies):
    print(f"{name}: n={len(latencies)} avg={statistics.mean(latencies):.6f}s "
          f"p95={statistics.quantiles(latencies, n=20)[18]:.6f}s "
          f"max={max(latencies):.6f}s")


def main():
    parser = argparse.ArgumentParser(description="Benchmark sederhana untuk demo RPC.")
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument("--target", choices=["xmlrpc", "zerorpc", "all"], default="all")
    args = parser.parse_args()

    if args.target in ("xmlrpc", "all"):
        lats = bench_xmlrpc(iterations=args.iterations)
        summarize("XML-RPC", lats)
    if args.target in ("zerorpc", "all"):
        lats = bench_zerorpc(iterations=args.iterations)
        summarize("ZeroRPC", lats)


if __name__ == "__main__":
    main()
