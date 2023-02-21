#!/usr/bin/env python
import argparse
import json
import logging
import os
import pathlib
import requests
from pprint import pformat

log = logging.getLogger(__name__)


class AviatrixError(Exception):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workdir', required=True)

    parser.add_argument(
        "--account-name", help="Cloud Account Name in AVX Controller", required=True
    )
    parser.add_argument('--ctrl_ip', required=True)
    parser.add_argument('--vpc-name', required=True)
    parser.add_argument('--vpc-id', required=True)
    parser.add_argument('--region', required=True)
    parser.add_argument('--cidr', required=True)
    parser.add_argument('--cloud', required=True)
    parser.add_argument('--network_domain', required=True)
    parser.add_argument('--transit_gw_name', required=True)

    args = parser.parse_args()
    avx_ip, avx_user, avx_pass = get_avx_details()

    # Login to controller
    ctrl_api, cid = controller_login(avx_ip, avx_user, avx_pass)

    # Check if account exists
    assert check_account_exists(args.account_name, ctrl_api, cid)

    # Check if network domain exists
    if not check_network_domain_exists(args.network_domain, ctrl_api, cid):
        # Check destination CIDRs are valid and connected.
        pass

    # Generate spoke gateway config file.
    config = {
        "cloud": args.cloud,
        "account_name": args.account_name,
        "transit_gw_name": args.transit_gw_name,
        "vpc_id": args.vpc_id,
        "vpc_name": args.vpc_name,
        "cidr": args.cidr,
        "region": args.region,
        "network_domain": args.network_domain,
        "ctrl_ip": args.ctrl_ip,
    }

    # Export to json
    config_path = pathlib.Path(args.workdir) / 'config.json'
    with config_path.open("w") as f:
        json.dump(config, f)

    print(str(config_path))


def get_avx_details():
    """Get Aviatrix login details from environment."""
    avx_password = os.environ.get("AVIATRIX_PASSWORD")
    avx_user = os.environ.get("AVIATRIX_USERNAME")
    avx_ip = os.environ.get("AVIATRIX_CONTROLLER_IP")
    return avx_ip, avx_user, avx_password


def controller_login(ctrl_ip, username, password):
    log.debug("Controller IP: '%s'", ctrl_ip)
    log.debug("Username: '%s'", username)
    controller_api_url = "https://" + str(ctrl_ip) + "/v1/api"
    log.debug("Controller API URL: '%s'", controller_api_url)

    log.info("Logging in as %s", username)
    r = requests.post(
        controller_api_url,
        data={"action": "login", "username": username, "password": password},
        verify=False,
    )
    log.debug("login response: \n%s", pformat(r.json()))
    try:
        return controller_api_url, r.json()["CID"]
    except Exception as exc:
        log.exception(
            "Login failed. Please check Aviatrix Controller IP, username and password."
        )
        raise AviatrixError(
            f"Failed to login to controller.\nUsername: {username}"
            f"\nController IP: {ctrl_ip}"
        ) from exc

def check_account_exists(account_name, controller_api_url, cid):
    """Check if account exists AVX controller"""
    log.info("Getting list of accounts on controller.")
    response = requests.post(
        controller_api_url,
        data={"action": "list_accounts", "CID": cid, "aws_iam_role_based": True},
        verify=False,
    )
    log.debug("list_accounts response:\n%s", pformat(response.json()))
    account_list = response.json()["results"]["account_list"]
    log.debug("Account List:\n%s", pformat(account_list))
    return account_name in account_list


def check_network_domain_exists(network_domain, controller_api_url, cid):
    """Check if network domain exists on AVX controller"""
    log.info("Getting list of network domains on controller.")
    response = requests.post(
        controller_api_url,
        data={"action": "list_network_domains", "CID": cid},
        verify=False,
    )
    log.debug("list_network_domains response:\n%s", pformat(response.json()))
    network_domain_list = response.json()["results"]["network_domain_list"]
    log.debug("Network Domain List:\n%s", pformat(network_domain_list))
    return network_domain in network_domain_list


if __name__ == "__main__":
    main()
