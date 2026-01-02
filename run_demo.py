import argparse
import logging
import os
import subprocess
import sys


def resolve_paths():
    root = os.path.dirname(os.path.abspath(__file__))
    return {
        "grpc": os.path.join(root, "grpc-demo"),
        "xmlrpc": os.path.join(root, "xmlrpc-demo"),
        "rpyc": os.path.join(root, "rpyc-demo"),
        "zerorpc": os.path.join(root, "zerorpc-demo"),
        "pyro5": os.path.join(root, "pyrofive"),
        "graphql": os.path.join(root, "graphql_demo"),
    }


def run_command(cmd, cwd=None):
    logging.info("Menjalankan: %s", " ".join(cmd))
    try:
        subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        logging.error("Perintah gagal dengan kode %s", e.returncode)
        raise
    except Exception as e:
        logging.exception("Gagal menjalankan perintah: %s", e)
        raise


def run_grpc(role, paths):
    if role == "server":
        run_command([sys.executable, "server.py"], cwd=paths["grpc"])
    elif role == "client":
        run_command([sys.executable, "client.py"], cwd=paths["grpc"])
    else:
        raise ValueError("Role tidak didukung untuk gRPC")


def run_xmlrpc(role, paths):
    if role == "server":
        run_command([sys.executable, "server.py"], cwd=paths["xmlrpc"])
    elif role == "client":
        run_command([sys.executable, "client.py"], cwd=paths["xmlrpc"])
    else:
        raise ValueError("Role tidak didukung untuk XML-RPC")


def run_rpyc(role, paths):
    if role == "server":
        run_command([sys.executable, "server.py"], cwd=paths["rpyc"])
    elif role == "client":
        run_command([sys.executable, "client.py"], cwd=paths["rpyc"])
    else:
        raise ValueError("Role tidak didukung untuk RPyC")


def run_zerorpc(role, paths):
    if role == "server":
        run_command([sys.executable, "server.py"], cwd=paths["zerorpc"])
    elif role == "client":
        run_command([sys.executable, "client.py"], cwd=paths["zerorpc"])
    else:
        raise ValueError("Role tidak didukung untuk ZeroRPC")


def run_pyro5(role, paths):
    if role == "nameserver":
        run_command([sys.executable, "-m", "Pyro5.nameserver"])
    elif role == "server":
        run_command([sys.executable, "server.py"], cwd=paths["pyro5"])
    elif role == "client":
        run_command([sys.executable, "client.py"], cwd=paths["pyro5"])
    else:
        raise ValueError("Role tidak didukung untuk Pyro5")


def run_graphql(role, paths):
    if role == "server":
        run_command([sys.executable, "manage.py", "runserver"], cwd=paths["graphql"])
    else:
        raise ValueError("Role tidak didukung untuk GraphQL")


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    parser = argparse.ArgumentParser(description="Orkestrasi menjalankan demo RMI/RPC.")
    parser.add_argument("demo", choices=["grpc", "xmlrpc", "rpyc", "zerorpc", "pyro5", "graphql"])
    parser.add_argument("role", help="server|client|nameserver (khusus Pyro5)", nargs="?")
    args = parser.parse_args()

    paths = resolve_paths()
    dispatch = {
        "grpc": run_grpc,
        "xmlrpc": run_xmlrpc,
        "rpyc": run_rpyc,
        "zerorpc": run_zerorpc,
        "pyro5": run_pyro5,
        "graphql": run_graphql,
    }

    try:
        if args.demo == "graphql" and args.role is None:
            args.role = "server"
        if args.demo == "pyro5" and args.role is None:
            logging.info("Role default Pyro5 adalah 'server'.")
            args.role = "server"
        if args.role is None:
            raise SystemExit("Role perlu diisi: server|client|nameserver (Pyro5).")
        dispatch[args.demo](args.role, paths)
    except KeyError:
        raise SystemExit("Demo tidak dikenal.")
    except Exception as e:
        logging.error("Gagal menjalankan demo: %s", e)
        raise


if __name__ == "__main__":
    main()
