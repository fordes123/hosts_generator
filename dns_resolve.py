import dns.message
import dns.edns
import dns.query
import ipaddress
import argparse
from tqdm import tqdm


def convert_cidr(cidr):
    ipv4 = ipaddress.IPv4Network(cidr)
    address = ipv4.network_address.packed
    mask = ipv4.netmask.packed
    return address + mask


def resolve(domain):
    opt = dns.edns.GenericOption(dns.edns.ECS, convert_cidr(CIDR))
    request = dns.message.make_query(domain, 'A')
    request.use_edns(edns=True, options=[opt])
    response = dns.query.https(request, DOH_SERVER)
    for answer in response.answer:
        if answer.rdtype == dns.rdatatype.A:
            for item in answer.items:
                return item.address


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--cidr', default='127.0.0.0/8', help='CIDR for the target area')
    parser.add_argument('-s', '--server', default='https://dns.google/dns-query', help='DoH Server (Must support ECS)')
    parser.add_argument('-o', '--output', default='./hosts', help='output file')
    parser.add_argument('-d', '--domains', default='./domains.txt', help='domain list file')
    return parser.parse_args()


global OUTPUT_FILE
global CIDR
global DOH_SERVER
if __name__ == "__main__":
    args = parse_args()
    CIDR = args.cidr if args.cidr else '127.0.0.0/8'
    DOH_SERVER = args.server if args.server else 'https://dns.google/dns-query'
    OUTPUT_FILE = args.output if args.output else './hosts'
    INPUT_FILE = args.domains if args.domains else './domains.txt'

    with open(INPUT_FILE, 'r') as f:
        DOMAINS = f.read().splitlines()
        with open(OUTPUT_FILE, "w") as hosts_file:
            pbar = tqdm(total=len(DOMAINS), desc='Progress', leave=True, ncols=100, unit_scale=True)
            for domain in DOMAINS:
                try:
                    ipv4 = resolve(domain)
                    if ipv4 is not None:
                        hosts_file.write(f"{ipv4:{15}}\t{domain}\n")
                except ValueError as e:
                    print(e)
                pbar.update(1)
            pbar.close()
