# TODO: validate paramters
# TODO: handle subprocess command errors
# TODO: change if elif else to switch case
# or allow to identify its own .pcap file

import subprocess
from argparse import ArgumentParser

def create_parser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("-i", "--interface")
    parser.add_argument("-t", "--task")
    return parser

def generate_traffic(interface: str, task: str) -> None:
    commands = []
    if task == "icmp": commands = "tcpreplay -v --mbps=0.005 -i ./data/icmp-test.pcap".split()
    elif task == "http": commands = "tcpreplay -v --mbps=0.03 -i eth0 ./data/mx-1.pcap".split()
    elif task == "task_6": commands = "tcpreplay -v --mbps=0.03 -i eth0 ./data/mx-1.pcap".split()
    elif task == "task_7": commands = "tcpreplay -v --mbps=0.03 -i eth0 ./data/mx-1.pcap".split()
    elif task == "task_10_ips_icmp": commands = "tcpreplay -v --mbps=0.007 -i eth0 ./data/44m.pcap".split()
    elif task == "task_10_ips_torrent": commands = "tcpreplay -v --mbps=0.009 -i eth0 ./data/torrent.pcap".split()
    else: raise RuntimeError("Unknown task")

    reply = subprocess.run(
        commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )
    if reply.returncode == 0:
        print(True, reply.stdout)
    else:
        print(False, reply.stderr)

def main() -> None:
    parser = create_parser()
    args = parser.parse_args()
    generate_traffic(args.interface, args.task)

if __name__ == "__main__":
    main()
