#!/usr/bin/env python3
"""
Generate styled blog post build files from template + WordPress content.
Strips Gutenberg block comments, wraps in styled template.
"""
import json
import re
import html
import os
import urllib.request
import urllib.error
import base64

REPO = "/Users/willsullivan/Documents/GitHub/04_PacerAI_GTM/website-PacerAI"
TEMPLATE_PATH = f"{REPO}/src/blog/post-template.html"
OUTPUT_DIR = f"{REPO}/src/blog/posts"

# Blog post metadata
POSTS = [
    {
        "id": 288,
        "title": "Why ARR Waterfall Models Matter for SaaS Growth",
        "title_short": "ARR Waterfall Models",
        "category": "ARR Snowballs",
        "date": "January 27, 2026",
        "date_iso": "2026-01-27",
    },
    {
        "id": 264,
        "title": "Using AI to Enable RevOps (Without Breaking Your GTM)",
        "title_short": "AI for RevOps",
        "category": "RevOps",
        "date": "January 20, 2026",
        "date_iso": "2026-01-20",
    },
    {
        "id": 244,
        "title": "ARR Snowball Analysis: Find Your Expansion Drivers",
        "title_short": "Expansion Drivers",
        "category": "ARR Snowballs",
        "date": "January 12, 2026",
        "date_iso": "2026-01-12",
    },
    {
        "id": 236,
        "title": "Prevent Churn in High-Value Accounts with ARR Snowball",
        "title_short": "Churn Prevention",
        "category": "ARR Snowballs",
        "date": "January 12, 2026",
        "date_iso": "2026-01-12",
    },
    {
        "id": 227,
        "title": "What Is an ARR Snowball? Understanding Revenue Growth",
        "title_short": "What Is ARR Snowball",
        "category": "ARR Snowballs",
        "date": "January 12, 2026",
        "date_iso": "2026-01-12",
    },
]


def strip_gutenberg_comments(content):
    """Remove Gutenberg block comments like <!-- wp:paragraph --> etc."""
    content = re.sub(r'<!-- /?wp:\w+[^>]*-->\s*', '', content)
    # Also remove class attributes added by Gutenberg
    content = re.sub(r' class="wp-block-heading"', '', content)
    content = re.sub(r' class="wp-block-list"', '', content)
    content = re.sub(r' class="wp-block-separator has-alpha-channel-opacity"', '', content)
    content = re.sub(r' class="has-fixed-layout"', '', content)
    content = re.sub(r'<figure class="wp-block-table">(.*?)</figure>', r'\1', content, flags=re.DOTALL)
    return content.strip()


def fetch_post_content(post_id):
    """Fetch post content from WordPress REST API."""
    url = f"https://getpacerai.com/wp-json/wp/v2/posts/{post_id}"
    wp_user = "willsullivan5e7f50183a"
    wp_pass = os.environ.get("WP_APP_PASSWORD", "")

    if not wp_pass:
        # Try reading from local cache files
        cache_file = f"{REPO}/src/blog/posts/cache-{post_id}.json"
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                data = json.load(f)
                return data.get('content', {}).get('rendered', '')
        print(f"  WARNING: No WP_APP_PASSWORD set and no cache for post {post_id}")
        return None

    credentials = base64.b64encode(f"{wp_user}:{wp_pass}".encode()).decode()
    req = urllib.request.Request(url)
    req.add_header("Authorization", f"Basic {credentials}")

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('content', {}).get('rendered', '')
    except urllib.error.URLError as e:
        print(f"  ERROR fetching post {post_id}: {e}")
        return None


def build_post(template, post_meta, content):
    """Replace template placeholders with post data."""
    # Strip Gutenberg comments from content
    clean_content = strip_gutenberg_comments(content)

    output = template
    output = output.replace("{{TITLE}}", post_meta["title"])
    output = output.replace("{{TITLE_SHORT}}", post_meta["title_short"])
    output = output.replace("{{CATEGORY}}", post_meta["category"])
    output = output.replace("{{DATE}}", post_meta["date"])
    output = output.replace("{{DATE_ISO}}", post_meta["date_iso"])
    output = output.replace("{{CONTENT}}", clean_content)

    return output


def main():
    # Read template
    with open(TEMPLATE_PATH, 'r') as f:
        template = f.read()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Pre-loaded content from MCP (hardcoded since we already fetched it)
    # We'll use the raw post_content we already have
    print("Building blog post files from template...")

    for post in POSTS:
        post_id = post["id"]
        print(f"\n  Building post {post_id}: {post['title_short']}...")

        # Read cached content file
        content_file = f"{OUTPUT_DIR}/content-{post_id}.html"
        if not os.path.exists(content_file):
            print(f"    Content file not found: {content_file}")
            print(f"    Run: save content files first")
            continue

        with open(content_file, 'r') as f:
            content = f.read()

        output = build_post(template, post, content)

        output_file = f"{OUTPUT_DIR}/{post_id}-build.html"
        with open(output_file, 'w') as f:
            f.write(output)

        print(f"    Saved: {output_file}")
        print(f"    Size: {len(output):,} chars")

    print("\nDone! Build files ready for deploy.")


if __name__ == "__main__":
    main()
