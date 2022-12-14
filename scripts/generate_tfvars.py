#!/usr/bin/env python
"""Generate tfvars file for terraform."""
import argparse
import json
import pathlib


def main():
    """Parses the arguments and generates the tfvars file."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--workdir', required=True)

    parser.add_argument('--name', required=True)
    parser.add_argument('--region', required=True)
    parser.add_argument('--cidr', required=True)
    parser.add_argument('--network_domain', required=True)
    parser.add_argument('--ctrl_ip', required=True)
    args = parser.parse_args()

    tfvars_path = pathlib.Path(args.workdir) / 'terraform.tfvars.json'
    tfvars = {
        'name': args.name,
        'region': args.region,
        'cidr': args.cidr,
        'network_domain': args.network_domain,
        'ctrl_ip': args.ctrl_ip,
    }

    with tfvars_path.open('w') as f:
        json.dump(tfvars, f)

    print(str(tfvars_path))


if __name__ == '__main__':
    main()
