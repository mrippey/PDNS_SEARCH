import argparse
import dnsdb2
from dotenv import load_dotenv
import logging    
import os
import sys
from time import sleep

load_dotenv() 

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%dT%H:%M:%S',
                    filename='passive_dns_lookup.log',
                    filemode='w')


def dnsdb_request_setup(ip):
  """Setup and name variables for DNSDB API Client.

client = dnsdb2.Client()
results = client.summarize_rdata_ip()
"""

    dnsdb_key = os.getenv("DNSDB_KEY")
    client = dnsdb2.Client(dnsdb_key)
    results = next(client.summarize_rdata_ip(ip))
    return results


def single_fetch_dnsdb_results(target):
  """Get results for a single IP address, used with the '--ip' arg.

get_num_hosts = result of dnsdb_request_setup()
The 'num_results' key holds the number of hosts associated with an IP address.
"""
  

    get_num_hosts = dnsdb_request_setup(ip=target)

    if get_num_hosts['num_results'] < 100:
        return f'IP: {target} has a low number of hosts, you may want to block'
    else:
        return f'IP: {target} has a large number of hosts, block with caution'


def multiple_fetch_dnsdb_results(target):
  """Get results for a file of IP addresses, used with the '--file' arg.

Still a work in progress.
"""

    with open(target, 'r') as f:
        data = f.readlines()
        get_multi_hosts = dnsdb_request_setup(ip=data)
        if len(get_multi_hosts) > 4:
            sleep(10)
        for x in get_multi_hosts:
            if x['num_results'] < 100:
                return f'IP: {target} has a low number of hosts, you may want to block \n'
    
            return f'IP: {target} has a large number of hosts, block with caution'


def parse_args():
    parser = argparse.ArgumentParser(description='Args')
    parser.add_argument('-f', '--file', help='path to file of IP addresses')
    parser.add_argument('-i', '--ip', help='Specifiy single IP address to lookup')

    args = parser.parse_args()

    return args 


def main():
    args = parse_args()
    if args.ip:
        print(single_fetch_dnsdb_results(args.ip))
    if args.file:
        print(multiple_fetch_dnsdb_results(args.file))
    else:
        print("Couldn't understand your request, try again")
        sys.exit(1)
    

if __name__ == '__main__':
    main()
