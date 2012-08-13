# ec2ddns

Python utlity to register an EC2 instance's hostname in Route 53.

## Usage

Register an instance:

    /usr/bin/python /usr/sbin/ec2ddns.py -k ${AWS_KEY} -s ${AWS_SECRET} ${DESIRE_HOSTNAME} ${PUBLIC_HOSTNAME}

Unregister an instance:

    /usr/bin/python /usr/sbin/ec2ddns.py -k ${AWS_KEY} -s ${AWS_SECRET} ${DESIRE_HOSTNAME} --delete

## TODO

- Use `~/.boto` credentials or user-data directly if not provided by CLI args.
- Better logging.
- Restrict record types to A|CNAME when deleting conflicting records?
- Store SSH fingerprints in DNS.
- Better permissions or logic for deletion of other records:
    - If another machine legitimately has that hostname.
    - Malicious deletion of another instance's record.
