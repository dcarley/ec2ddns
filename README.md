# ec2ddns

Python utlity to register an EC2 instance's hostname in Route 53.

## Usage

Register an instance:

    /usr/bin/python /usr/sbin/ec2ddns.py -k ${AWS_KEY} -s ${AWS_SECRET} ${DESIRE_HOSTNAME} ${PUBLIC_HOSTNAME}

Unregister an instance:

    /usr/bin/python /usr/sbin/ec2ddns.py -k ${AWS_KEY} -s ${AWS_SECRET} ${DESIRE_HOSTNAME} --delete

## IAM policy

Create a new IAM user and policy using Fog:

``` ruby
require 'fog'
require 'pp'

@username   = "ec2ddns"
@zone_id    = "XXX"

iam     = Fog::AWS::IAM.new()
user    = iam.create_user(@username)
keys    = iam.create_access_key("UserName" => @username)

pp keys.body["AccessKey"]
access_key_id       = keys.body["AccessKey"]["AccessKeyId"]
secret_access_key   = keys.body["AccessKey"]["SecretAccessKey"]

policy_statement = {
   "Statement" => [
      {
         "Effect" => "Allow",
         "Action" => ["route53:ListHostedZones"],
         "Resource" => "*"
      },
      {
         "Effect" => "Allow",
         "Action" => ["route53:GetHostedZone", "route53:ListResourceRecordSets", "route53:ChangeResourceRecordSets"],
         "Resource" => "arn:aws:route53:::hostedzone/" + @zone_id
      },
      {
         "Effect" => "Allow",
         "Action" => ["route53:GetChange"],
         "Resource" => "arn:aws:route53:::change/*"
      }
   ]
}

iam.put_user_policy(@username, @username, policy_statement)
```

## TODO

- Use `~/.boto` credentials or user-data directly if not provided by CLI args.
- Better logging.
- Restrict record types to A|CNAME when deleting conflicting records?
- Store SSH fingerprints in DNS.
- Better permissions or logic for deletion of other records:
    - If another machine legitimately has that hostname.
    - Malicious deletion of another instance's record.
