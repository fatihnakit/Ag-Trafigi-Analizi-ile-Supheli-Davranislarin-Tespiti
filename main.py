
import argparse
from scapy.all import rdpcap, IP
from collections import Counter
import matplotlib.pyplot as plt

def analyze_pcap(file_path, output_path):
    packets = rdpcap(file_path)
    ip_counter = Counter()

    for pkt in packets:
        if IP in pkt:
            ip_counter[pkt[IP].src] += 1

    with open(output_path, "w") as f:
        for ip, count in ip_counter.most_common():
            f.write(f"{ip}: {count} packets\n")

    # Graph
    labels, values = zip(*ip_counter.most_common(10))
    plt.figure(figsize=(10,6))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.title("Top 10 IP by Packet Count")
    plt.tight_layout()
    plt.savefig("graphs/ip_packet_count.png")
    print("Analysis complete. Results saved.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to pcap file")
    parser.add_argument("--output", required=True, help="Path to output text file")
    args = parser.parse_args()
    analyze_pcap(args.input, args.output)
