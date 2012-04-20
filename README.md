# ec2ddns

Python utlity to register an EC2 instance's hostname in Route 53.

## TODO

- Use `~/.boto` credentials or user-data directly if not provided by CLI args.
- Better logging.
- Restrict record types to A|CNAME when deleting conflicting records?
- Store SSH fingerprints in DNS.
- Better permissions or logic for deletion of other records:
    - If another machine legitimately has that hostname.
    - Malicious deletion of another instance's record.
