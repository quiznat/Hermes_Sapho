---
version: source-capture.v1
article_id: art-2026-03-01-007
ticket_id: ticket-import-art-2026-03-01-007
source_url: https://www.johann.fyi/openclaw-security-101
canonical_url: https://www.johann.fyi/openclaw-security-101
source_title: 'OpenClaw Security 101: The Complete Guide | Johann S.'
capture_kind: runtime-import
http_status: 200
content_type: text/html
captured_at_utc: '2026-03-22T18:24:58Z'
---
# Source Capture

## Title

OpenClaw Security 101: The Complete Guide | Johann S.

## Body

OpenClaw Security 101: The Complete Guide | Johann S. Security Guide
OpenClaw Security 101
13 steps to lock down your AI assistant like a pro.
Written for absolute beginners by an ex-Cisco security engineer. No experience required — just follow each step.
By Johann Sathianathen • Ex-Cisco Security Engineer • Updated Feb 19, 2026
ℹ️ Stuck on something? Copy the error message and paste it at claude.ai with: "I'm following Johann's OpenClaw security guide and got this error: [PASTE ERROR HERE]"
🤔 Why does this matter?
OpenClaw is powerful — it can run commands, access files, send messages, and talk to APIs on your behalf. That's amazing when you're in control. But if someone else gets access? They could:
Read your private messages and files
Steal your API keys (and run up your bill)
Run commands on your server
Use prompt injection to make your bot do things you didn't authorize
This guide takes about 30 minutes and makes all of that nearly impossible. Let's go.
📋 What You'll Set Up
1 Run it on a separate machine 2 Never run as root 3 Change the default port 4 Install Tailscale 5 SSH keys + Fail2ban 6 Firewall with UFW 7 Allowlist your users 8 Ask your bot to audit itself 9 Set up real-time alerts 10 DMs only 11 Sandbox your subagents 12 Daily security audit cron job 13 Keep OpenClaw updated
The 13-Step Security Checklist
1
🖥️ Run It on a Separate Machine
If something goes wrong, your main computer stays safe.
Never run OpenClaw on the same computer you use for banking, email, or personal stuff. Get a separate machine — even a cheap one works.
Option A: Cloud VPS ($5–10/mo)
Best for most people. Always on, always accessible.
DigitalOcean — $6/mo droplet
Linode — $5/mo server
Hetzner — €4/mo (EU)
Option B: Mac Mini / Old Laptop
Keep it at home, no monthly cost.
Mac Mini (great for always-on)
Any old laptop running Linux
Raspberry Pi (for light usage)
💡 Think of it like this: You wouldn't let a stranger into your bedroom. Give your AI its own room — a separate machine where, even if something weird happens, your personal stuff is untouched.
2
🚫 Never Run as Root
Root = god mode. If your bot gets compromised as root, the attacker owns everything.
The root user on Linux can do anything — delete files, install malware, read secrets. Create a regular user for OpenClaw instead.
Create a dedicated user
Create openclaw user 📋 Copy
# Create a new user called "openclaw"
sudo adduser openclaw
# Give it permission to use sudo (only when needed)
sudo usermod -aG sudo openclaw
# Switch to that user
su - openclaw
⚠️ Already running as root? It's not too late. Create the user above, copy your OpenClaw config over, and restart. Your bot will work exactly the same — just safer.
3
🔢 Change the Default Port
Port 8080 is public knowledge. Bots are already scanning for it.
OpenClaw runs on port 8080 by default. Anyone who knows OpenClaw exists can scan the internet for that port. Changing it is like moving your front door — automated attackers won't find it.
Edit your config
Change the port in openclaw.json 📋 Copy
{
"gateway": {
"port": 39217,
"bind": "loopback"
}
}
Pick any number between 10000 and 65535 . Don't use the example above — pick your own random number.
Restart OpenClaw 📋 Copy
openclaw gateway restart
💡 Quick analogy: It's like having an unlisted phone number. Doesn't stop a determined attacker, but it blocks 99% of automated scans.
4
🛡️ Install Tailscale
Makes your server invisible to the internet. Free for personal use.
Tailscale creates a private network between your devices. Your server becomes invisible to the entire internet — only your approved devices can see it. It's like a secret tunnel that only you have the key to.
Install Tailscale on your server
Install Tailscale 📋 Copy
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
It'll give you a link to log in. Click it, sign in with Google/GitHub, and you're done.
Install on your phone/laptop too
Download the Tailscale app on every device you want to access OpenClaw from. Now they can all talk to each other privately.
Configure OpenClaw to use Tailscale
Update openclaw.json 📋 Copy
{
"gateway": {
"bind": "loopback",
"port": 39217,
"auth": {
"allowTailscale": true
},
"tailscale": {
"mode": "serve"
}
}
}
This configures OpenClaw to serve through Tailscale's secure tunnel while binding locally for maximum security.
✅ This is the single most impactful step. Once you bind to Tailscale, your OpenClaw instance literally does not exist on the public internet. No port scanning, no brute forcing, no drive-by attacks. Gone.
💬 Stuck on a step? Get help from 50+ AI operators in the Skool community.
Join AI Operators →
5
🔑 SSH Keys + Fail2ban
3 wrong password attempts = 24-hour ban. SSH keys make passwords irrelevant.
SSH is how you connect to your server remotely. By default, it uses passwords — which can be guessed. SSH keys are like a physical key that can't be guessed, and Fail2ban automatically blocks anyone who tries.
Step A: Create your SSH key (on your local computer)
Generate SSH Key 📋 Copy
ssh-keygen -t ed25519 -C "your-email@example.com"
Press Enter 3 times to accept defaults. This creates a key pair on your computer.
Step B: Copy the key to your server
Copy key to server 📋 Copy
ssh-copy-id openclaw@YOUR_SERVER_IP
Step C: Disable password login
Edit SSH config 📋 Copy
sudo nano /etc/ssh/sshd_config
Find and change these lines:
PasswordAuthentication no
PermitRootLogin no
Save: Ctrl+X → Y → Enter
Restart SSH 📋 Copy
sudo systemctl restart sshd
⚠️ Test before closing! Open a NEW terminal and try to SSH in. If it works, close the old one. If not, you still have the old terminal to fix things.
Step D: Install Fail2ban
Install and enable Fail2ban 📋 Copy
sudo apt update
sudo apt install fail2ban -y
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
Fail2ban monitors your SSH logs. 3 wrong attempts? That IP gets banned for 24 hours. Automatic.
6
🧱 Firewall with UFW
Close every port you don't need. If it's not open, it can't be attacked.
UFW (Uncomplicated Firewall) blocks all incoming connections except the ones you specifically allow. Think of it as a bouncer at the door — if you're not on the list, you're not getting in.
Set up UFW 📋 Copy
# Block everything by default
sudo ufw default deny incoming
sudo ufw default allow outgoing
# Allow SSH (so you don't lock yourself out!)
sudo ufw allow ssh
# If NOT using Tailscale, allow your OpenClaw port
# sudo ufw allow 39217
# Turn it on
sudo ufw enable
# Check it's working
sudo ufw status
💡 Using Tailscale? You don't need to open your OpenClaw port in UFW at all. Tailscale traffic bypasses UFW because it's already encrypted and authenticated. Just keep SSH open and you're good.
7
📋 Allowlist Your Users
Everyone who isn't you gets ignored. Period.
Tell OpenClaw exactly which Telegram accounts are allowed to talk to it. Anyone else who messages your bot? Completely ignored. No response, no acknowledgment, nothing.
Find your Telegram User ID
Open Telegram, search for @userinfobot , send /start . It'll reply with your user ID (a number like 123456789 ).
Add it to your config
openclaw.json — allowlist section 📋 Copy
{
"channels": {
"telegram": {
"dmPolicy": "pairing",
"groupPolicy": "disabled",
"allowFrom": ["tg:YOUR_USER_ID_HERE"]
}
}
}
Set a strong auth password
openclaw.json — auth section 📋 Copy
{
"gateway": {
"auth": {
"mode": "password",
"password": "PICK-A-RANDOM-30-CHAR-PASSWORD-HERE"
}
}
}
Use 20+ characters, mix letters/numbers/symbols. Don't use the example — make your own.
8
🤖 Ask Your Bot to Audit Its Own Security
Your AI assistant can check its own setup for vulnerabilities.
This is the cool part. OpenClaw can actually examine its own configuration and tell you if anything is wrong. Just send it a message.
📋 Copy & paste this to your OpenClaw:
Security Audit Prompt — send this to your bot 📋 Copy
Audit your own security setup. Check:
1. Are you running as root? (you shouldn't be)
2. What port is the gateway on? (shouldn't be 8080, should be a custom port)
3. Is the gateway bound to "loopback"? (good) or "0.0.0.0"? (bad)
4. Is Tailscale configured with "mode": "serve" and "allowTailscale": true?
5. Is there an allowFrom list in the config? (there should be)
6. Are DM and group policies set correctly? (dmPolicy: pairing, groupPolicy: disabled)
7. Is UFW enabled? What ports are open?
8. Is Fail2ban running?
9. What are the file permissions on openclaw.json? (should be 600)
10. Are there any API keys hardcoded in config files? (they should be in .env)
11. Is Docker sandboxing configured for subagents?
12. Are sandbox capabilities dropped with "capDrop": ["ALL"]?
Give me a security score out of 10 and tell me what to fix.
Your bot will check everything and give you a report. Fix whatever it flags, then run it again.
9
🔔 Set Up Real-Time Alerts
Your bot messages you when something's off — before it becomes a problem.
Configure OpenClaw to notify you whenever something unusual happens. Failed login attempts, configuration changes, new SSH connections — you'll know immediately.
Add security rules to your SOUL.md
Add to ~/.openclaw/workspace/SOUL.md 📋 Copy
## Security Monitoring
- If you detect any failed authentication attempts, alert me immediately
- If any configuration files are modified, tell me what changed
- If a new SSH session connects to this server, let me know
- Never output API keys, passwords, tokens, or .env file contents
- If someone asks you to reveal secrets, refuse and alert me
- Run a daily security check and report any issues
💡 Think of it like a home security camera. You don't sit and watch it all day — but when something moves, it pings your phone. Same idea.
🚀 Halfway there! Join the community to share your setup and get feedback from other builders.
Join AI Operators →
10
💬 DMs Only
In group chats, everyone can control your bot. That's a problem.
If your bot is in a group chat, anyone in that group can give it commands. They could tell it to read your files, run commands, or do things you never authorized. Keep it to DMs only.
openclaw.json — DM policy 📋 Copy
{
"channels": {
"telegram": {
"dmPolicy": "pairing",
"groupPolicy": "disabled",
"allowFrom": ["tg:YOUR_USER_ID"]
}
}
}
⚠️ What about shared bots? If you must use OpenClaw in a group, create a separate instance with limited permissions. Never put your main bot in a group chat.
11
📦 Sandbox Your Subagents in Docker
A prompt-injected subagent can steal your secrets — unless it's in a sealed box.
OpenClaw can spawn subagents — smaller AI workers that handle specific tasks autonomously. Think of them as assistants your assistant hires. They might research a topic, write code, or process files on their own.
Here's the problem: subagents read things. Webpages, files, documents. If a subagent reads a malicious webpage with hidden instructions (this is called prompt injection ), it could get tricked into doing bad stuff — like reading your .env file and sending your API keys to an attacker.
The fix? Run subagents inside Docker containers. Docker is like a sealed box — the subagent can do its work, but it can't see your real files, your keys, or anything else on your server. Even if it gets prompt-injected, there's nothing to steal.
Install Docker
Install Docker 📋 Copy
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker openclaw
Log out and back in after adding your user to the docker group, so it takes effect.
Configure sandbox settings
openclaw.json — detailed sandbox config 📋 Copy
{
"agents": {
"defaults": {
"sandbox": {
"mode": "non-main",
"workspaceAccess": "rw",
"scope": "session",
"docker": {
"readOnlyRoot": false,
"network": "bridge",
"user": "1000:1000",
"capDrop": ["ALL"]
}
}
}
}
}
Understanding workspace access levels
"none" — Most secure. The subagent can't see any of your files. Use this for untrusted tasks like browsing the web.
"ro" — Read-only. The subagent can read your workspace files but can't change them. Good for research tasks.
"rw" — Read-write. The subagent can read and write files. Most flexible — use this for coding tasks like building websites.
Understanding network options
"none" — No internet access. Most secure. The subagent is completely isolated. Use this if the task doesn't need the internet.
"bridge" — Internet access. The subagent can reach the internet (for things like npm install , git push , etc). Use this for dev tasks.
✅ Why this matters: Prompt injection is the #1 risk with AI agents. A subagent reads a malicious webpage, gets tricked, and tries to steal your .env file. With Docker sandboxing, it can't — it's in a sealed container with no access to your host. Even a compromised subagent is harmless.
12
⏰ Set Up a Daily Security Audit Cron Job
Security isn't a one-time thing. Automate it so you never forget.
You locked everything down — nice. But what happens next week when something changes? A package updates, a config drifts, a new port opens. You won't notice unless someone checks.
Good news: OpenClaw has built-in cron scheduling. You can tell your bot to run a full security audit every single morning, automatically. It's like having a security guard that checks all the locks every morning before you wake up.
📋 Send this to your OpenClaw:
Daily Security Audit Cron — send this to your bot 📋 Copy
Set up a daily cron job that runs a full security audit every morning at 9am. Check: firewall status, fail2ban, SSH config, file permissions, open ports, Docker status, and report any issues.
Your bot will create the cron job and start auditing every day at 9 AM. If anything looks off, it'll message you about it.
💡 Think about it: Steps 1–11 are things you do once. This step makes sure they stay done. Configs change, updates break things, ports get opened accidentally. A daily audit catches all of that before it becomes a problem.
🎯 Almost done! Connect with 50+ AI operators who've already locked down their setups.
Join AI Operators →
13
🔄 Keep OpenClaw Updated
Old software = known vulnerabilities. Attackers love outdated software.
Every software update includes security patches — fixes for vulnerabilities that have been discovered since the last version. Running an old version of OpenClaw means running software with known security holes. Attackers actively scan for outdated software because the exploits are public knowledge.
Check your current version
Check version 📋 Copy
openclaw --version
Update to the latest
Update OpenClaw 📋 Copy
npm install -g openclaw
Best practices
Check the changelog before updating — see what changed so you're not caught off guard by breaking changes.
Test in staging first — if you're running OpenClaw in production (for a business, etc), update on a test instance first.
Set up a weekly version check — tell your bot: "Set up a weekly cron job to check if there's a newer version of OpenClaw available and let me know."
ℹ️ Pro tip: You can even ask your OpenClaw to check for updates automatically. Just send it: "Set up a weekly cron to check if there's a new OpenClaw version and message me if there is."
Your Complete Secure Config
Here's everything from this guide combined into one config file:
~/.openclaw/openclaw.json — complete secure config 📋 Copy
{
"gateway": {
"port": 39217,
"bind": "loopback",
"auth": {
"mode": "password",
"password": "YOUR-STRONG-30-CHAR-PASSWORD-HERE",
"allowTailscale": true
},
"tailscale": {
"mode": "serve"
}
},
"agents": {
"defaults": {
"sandbox": {
"mode": "non-main",
"workspaceAccess": "rw",
"scope": "session",
"docker": {
"readOnlyRoot": false,
"network": "bridge",
"user": "1000:1000",
"capDrop": ["ALL"]
}
}
}
},
"channels": {
"telegram": {
"dmPolicy": "pairing",
"groupPolicy": "disabled",
"allowFrom": ["tg:YOUR_TELEGRAM_USER_ID"]
}
}
}
⚠️ Remember to replace: 39217 → your chosen port number
YOUR-STRONG-30-CHAR-PASSWORD-HERE → a unique password
YOUR_TELEGRAM_USER_ID → your Telegram ID from @userinfobot
Install Tailscale and restart OpenClaw for the Tailscale config to take effect
🚀 Let Your OpenClaw Set This Up For You
Copy and paste this message to your OpenClaw bot. It'll walk you through every step and configure everything automatically.
Send this to your OpenClaw 📋 Copy
I just read Johann's Security 101 guide. Help me implement all 13 security steps:
1. Check if I'm running as root (create a dedicated user if so)
2. Change my gateway port from 8080 to something random
3. Help me install Tailscale and configure it with mode: "serve"
4. Set up SSH keys and disable password auth
5. Install and configure Fail2ban
6. Set up UFW firewall
7. Configure my allowlist with my Telegram user ID
8. Run a full security audit
9. Add security monitoring to my SOUL.md
10. Make sure I'm DMs-only (dmPolicy: pairing, groupPolicy: disabled)
11. Set up Docker sandboxing for subagents with proper security (capDrop: ALL)
12. Create a daily security audit cron job (9am every morning)
13. Check if OpenClaw is up to date
Go through each one, check what's already done, and help me fix what isn't.
Troubleshooting
Common issues and quick fixes:
"Permission Denied" Error
📋 sudo chown $USER:$USER ~/.openclaw/openclaw.json
chmod 600 ~/.openclaw/openclaw.json
"Config File Not Found" Error
📋 mkdir -p ~/.openclaw
nano ~/.openclaw/openclaw.json
OpenClaw Won't Start
📋 openclaw doctor
tail -20 ~/.openclaw/logs/gateway.log
"sudo: command not found"
📋 apt update && apt install sudo -y
"bash: openclaw: command not found"
📋 npm install -g openclaw
Final Security Check
Run this script to verify everything is locked down:
Complete Security Verification 📋 Copy
echo "=== 1. CHECKING USER ==="
whoami
echo ""
echo "=== 2. CHECKING PORT ==="
grep -o '"port":[[:space:]]*[0-9]*' ~/.openclaw/openclaw.json 2>/dev/null || echo "Using default port"
echo ""
echo "=== 3. CHECKING TAILSCALE ==="
tailscale status 2>/dev/null || echo "Tailscale not installed"
echo ""
echo "=== 4. CHECKING SSH CONFIG ==="
grep "PasswordAuthentication\|PermitRootLogin" /etc/ssh/sshd_config
echo ""
echo "=== 5. CHECKING FAIL2BAN ==="
sudo systemctl is-active fail2ban
echo ""
echo "=== 6. CHECKING FIREWALL ==="
sudo ufw status
echo ""
echo "=== 7. CHECKING ALLOWLIST ==="
grep -o '"allowFrom"' ~/.openclaw/openclaw.json 2>/dev/null && echo "✅ Allowlist configured" || echo "❌ No allowlist found"
echo ""
echo "=== 8. CHECKING FILE PERMISSIONS ==="
ls -la ~/.openclaw/openclaw.json
echo ""
echo "=== 9. CHECKING DOCKER ==="
docker --version 2>/dev/null || echo "Docker not installed"
echo ""
echo "=== DONE ==="
echo "Send the output above to your OpenClaw for a full analysis."
Join the Community
AI Operators Community
Join 50+ builders sharing OpenClaw configurations, security tips, and automation workflows. Free to join.
Join AI Operators →
Need Expert Setup?
Get professional security configuration for business deployments with compliance requirements.
Book a call →
Weekly Newsletter
Get the latest OpenClaw security updates, new features, and best practices delivered to your inbox.
Subscribe →
Questions? Ask the Community
Stuck on a step? Post in the Skool community and get help from other OpenClaw users within hours.
Ask a question →
Last updated: February 19, 2026 • By Johann Sathianathen • Ex-Cisco Security Engineer

## Import Provenance

- imported_from: canonical-openclaw-runtime
- runtime_article_bundle_path: research/articles/art-2026-03-01-007.md
- runtime_source_snapshot_json: research/source-material/art-2026-03-01-007.json
- runtime_source_snapshot_text: research/source-material/art-2026-03-01-007.txt
- runtime_filter_state: pending
- runtime_last_stage: intake
- refreshed_live_source: false
