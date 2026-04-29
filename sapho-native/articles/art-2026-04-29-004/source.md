---
version: source-capture.v1
article_id: art-2026-04-29-004
ticket_id: ticket-import-art-2026-04-29-004
source_url: https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability/
canonical_url: https://github.blog/security/securing-the-git-push-pipeline-responding-to-a-critical-remote-code-execution-vulnerability
source_title: 'Securing the git push pipeline: Responding to a critical remote code
  execution vulnerability - The GitHub Blog'
capture_kind: html
http_status: 200
content_type: text/html
captured_at_utc: '2026-04-29T13:01:32Z'
linked_paper_urls: []
---
# Source Capture

## Title

Securing the git push pipeline: Responding to a critical remote code execution vulnerability - The GitHub Blog

## Body

Home / Security

Securing the git push pipeline: Responding to a critical remote code execution vulnerability

How we validated, fixed, and investigated a critical vulnerability in under two hours, and confirmed no exploitation.

Alexis Wales · @alexiswales

April 28, 2026
| 5 minutes

Share:

On March 4, 2026, we received a vulnerability report through our Bug Bounty program from researchers at Wiz describing a critical remote code execution vulnerability affecting github.com, GitHub Enterprise Cloud, GitHub Enterprise Cloud with Data Residency, GitHub Enterprise Cloud with Enterprise Managed Users, and GitHub Enterprise Server.

In less than two hours we had validated the finding, deployed a fix to github.com, and begun a forensic investigation that concluded there was no exploitation .

In this post, we want to share what happened, how we responded, and what we are doing to prevent similar issues in the future.

Receiving the bug bounty report

The bug bounty report described a way for any user with push access to a repository, including a repository they created themselves, to achieve arbitrary command execution on the GitHub server handling their git push operation. The attack required only a single command: git push with a crafted push option that leveraged an unsanitized character.

Our security team immediately began validating the bug bounty report. Within 40 minutes, we had reproduced the vulnerability internally and confirmed the severity. This was a critical issue that required immediate action.

Understanding the vulnerability

When a user pushes code to GitHub, the operation passes through multiple internal services. As part of this process, metadata about the push, such as the repository type and the environment it should be processed in, is passed between services using an internal protocol.

The vulnerability leveraged how user-supplied git push options were handled within this metadata. Push options are an intentional feature of git that allow clients to send key-value strings to the server during a push. However, the values provided by the user were incorporated into the internal metadata without sufficient sanitization. Because the internal metadata format used a delimiter character that could also appear in user input, an attacker could inject additional fields that the downstream service would interpret as trusted internal values.

By chaining several injected values together, the researchers demonstrated that an attacker could override the environment the push was processed in, bypass sandboxing protections that normally constrain hook execution, and ultimately execute arbitrary commands on the server.

Responding to the vulnerability

With the root cause identified on March, 4, 2026, at 5:45 p.m. UTC, our engineering team developed and deployed a fix to github.com at 7:00 p.m. UTC that same day. The fix ensures that user-supplied push option values are properly sanitized and can no longer influence internal metadata fields.

For GitHub Enterprise Server, we prepared patches across all supported releases (3.14.25, 3.15.20, 3.16.16, 3.17.13, 3.18.8, 3.19.4, 3.20.0, or later) and published CVE-2026-3854 . These are available today and we strongly recommend that all GHES customers upgrade immediately.

Investigating for exploitation

With the immediate fix in place on github.com, we moved to the pressing question of whether anyone else found and exploited this vulnerability before the researchers reported it.

A key property of this vulnerability gave us confidence in our ability to answer that question. The exploit forces the server to take a code path that is never used during normal operations on github.com. This is not something an attacker can avoid or suppress, as it is an inherent consequence of how the injection works.

We logged this path and queried our telemetry for any instance of this anomalous code path being executed. The results were clear:

Every occurrence mapped to the Wiz researchers’ own testing activity.

No other users or accounts triggered this code path.

No customer data was accessed, modified, or exfiltrated as a result of this vulnerability.

For GHES customers, exploitation would require an authenticated user with push access on your instance. We recommend reviewing your access logs out of an abundance of caution.

Defense in depth

Beyond fixing the immediate input sanitization issue, our investigation surfaced an additional finding worth sharing.

The exploit worked in part because the server had access to a code path that was not intended for the environment it was running in. This code path existed on disk as part of the server’s container image, even though it was only meant to be used in a different product configuration. An older deployment method had correctly excluded this code, but when the deployment model changed, the exclusion was not carried forward.

This is a useful reminder that defense in depth matters. The input sanitization fix is the primary remediation, but we have also removed the unnecessary code path from environments where it should not exist. Even if a similar injection vulnerability were discovered in the future, this additional hardening would limit what an attacker could do with it.

What you should do

GitHub Enterprise Cloud , GitHub Enterprise Cloud with Enterprise Managed Users , GitHub Enterprise Cloud with Data Residency , and github.com were patched on March 4, 2026. No action is required from users of any of these.

As mentioned previously, exploitation on GitHub Enterprise Server requires an authenticated user with push access on your instance. We recommend that you review /var/log/github-audit.log for push operations containing ; in push options. Updates are available in the following releases:

GitHub Enterprise Server 3.14.25 or later

GitHub Enterprise Server 3.15.20 or later

GitHub Enterprise Server 3.16.16 or later

GitHub Enterprise Server 3.17.13 or later

GitHub Enterprise Server 3.18.7 or later

GitHub Enterprise Server 3.19.4 or later

GitHub Enterprise Server 3.20.0 or later

We strongly recommend upgrading to the latest patch release as soon as possible. See the GHES release notes for details.

This vulnerability has been assigned CVE-2026-3854 .

Acknowledgments

This vulnerability was discovered and responsibly disclosed by researchers at Wiz . Their report was thorough, clearly demonstrated the impact, and enabled us to move quickly from validation to remediation. This finding will receive one of the highest rewards in the history of our Bug Bounty program , which has been a cornerstone of our security program for over a decade.

Tags:

CVE

GHES

Written by

Alexis Wales

@alexiswales

Alexis Wales is the Chief Information Security Officer of GitHub. She leads a team of security experts focused on safeguarding the GitHub platform, products and the open source community, empowering more than 150 million developers worldwide to build and deploy software securely on GitHub.

Alexis has 20 years of experience defending critical national and private sector networks, spanning positions with the Department of Defense and the Department of Homeland Security’s Cybersecurity and Infrastructure Security Agency (CISA). This experience sparked her passion for collaboration between the public and private sectors to solve the hardest security challenges that threaten the technology we use every day.
