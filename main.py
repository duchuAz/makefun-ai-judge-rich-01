"""Write the ai-judge-rich-01 plan to entry.txt, deterministically."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = """Day 1: crawl the Shopify App Store's New apps and category pages, score 1,000 newest listings 0-100 on screenshots, copy, demo, reviews, publish the free grader and a public leaderboard, and email the 20 worst their score, 3 fixes, $199 offer.

Buyer: 600 indie devs under 15 reviews, found there, Shopify Partner directory, X and Indie Hackers. I use the public support email on their site/support page/privacy policy. I sell a 48-hour rewrite: title, subtitle, description, six screenshot captions, rendered PNGs and a demo-video script, as paste-in files. Half upfront by card/USDC, half on delivery, refund if late; then $29/month rank checks.

Email 30/day for 20 days, post the leaderboard weekly on X and Indie Hackers, and publish before/after. At 2% of 600: 12 fixes ($2,388) + 6 subscriptions ($174) = $2,562; costs under $50, so ~$2,510 on day 30.

Edge: the free grader is verifiable proof and inbound; ASO tools and freelancers sell advice, not a scored, done-for-you fix for this niche."""

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(PLAN.encode("utf-8"))
