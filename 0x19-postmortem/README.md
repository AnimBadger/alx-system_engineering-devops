## Issue summary:

- Duration of the outage: May 7, 2023, at 8:15 AM EDT - May 7, 2023, at 9:00 AM EDT
- Impact: Users trying to access the second web server were unable to do so during the outage.
- The service was shut down for all of the users trying to access it.
- The reason was a misconfigured firewall rule that was blocking incoming traffic.

## Timeline:

- 7th May 2023, 8:15 AM EDT A monitoring notice that revealed the second server was not responding to queries helped find the problem.
- Action took: The crew looked at the second server logs but discovered no difficulties.
- They discovered that queries were not getting to the second server after looking at the load balancer logs.
- Ineffective investigation/debugging strategies: The team spent some time looking over the server logs because they initially thought the second server might be the issue.
- Because the problem was with inbound traffic rather than the server itself, the investigation took a deceptive turn.
- The network engineering team was notified of the situation and asked to look into the network settings.
- The issue was fixed once the network engineering team found and fixed the incorrectly set firewall rule that was obstructing inbound traffic to the second server.

## Root cause and resolution:

- An incorrectly set up firewall rule that was preventing incoming traffic to this server was the main culprit.
- The problem was resolved once the network engineering team located and corrected the incorrect firewall rule.

## Corrective and preventative measures:

- The team will perform routine network configuration inspections to make sure that firewall rules are correctly implemented in order to stop similar problems from occurring in the future.
- Tasks to address the issue include:
 - Reviewing all servers' firewall rules to make sure they are configured properly
 - Putting in place extra traffic monitoring to find any other configuration errors or anomalies
 - Reviewing incident response processes to make sure that errors are found and fixed right away.


