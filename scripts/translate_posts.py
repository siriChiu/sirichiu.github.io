#!/usr/bin/env python3
"""
DeepL Translation Script for Hugo Blog Posts

This script translates Hugo markdown posts from Chinese to English using the DeepL API.
It preserves the markdown formatting and frontmatter structure.

Usage:
    1. Set the DEEPL_AUTH_KEY environment variable:
       Windows (PowerShell): $env:DEEPL_AUTH_KEY = "your-api-key"
       Linux/Mac: export DEEPL_AUTH_KEY="your-api-key"
    
    2. Run the script:
       python scripts/translate_posts.py
       
    Options:
       --force    Re-translate all posts, even if .en.md already exists
       --dry-run  Show what would be translated without making changes
"""

import os
import sys
import argparse
import requests
import yaml
import re
from pathlib import Path

# Fix Windows console encoding for Unicode characters
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Configuration
CONTENT_DIR = Path("content/posts")
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"  # Use api.deepl.com for Pro accounts

def get_api_key():
    """Get DeepL API key from environment variable."""
    api_key = os.environ.get("DEEPL_AUTH_KEY")
    if not api_key:
        print("❌ Error: DEEPL_AUTH_KEY environment variable not set.")
        print("\nPlease set it with:")
        print('  Windows (PowerShell): $env:DEEPL_AUTH_KEY = "your-api-key"')
        print('  Linux/Mac: export DEEPL_AUTH_KEY="your-api-key"')
        sys.exit(1)
    return api_key


def translate_text(text, api_key, target_lang="EN"):
    """
    Translates text using DeepL API.
    
    Args:
        text: The text to translate
        api_key: DeepL API key
        target_lang: Target language code (default: EN for English)
    
    Returns:
        Translated text or original text if translation fails
    """
    if not text or not text.strip():
        return ""
    
    try:
        response = requests.post(
            DEEPL_API_URL,
            data={
                "auth_key": api_key,
                "text": text,
                "source_lang": "ZH",  # Chinese source
                "target_lang": target_lang,
                "preserve_formatting": "1",  # Preserve markdown formatting
            },
            timeout=60  # 60 second timeout
        )
        response.raise_for_status()
        result = response.json()
        
        if "translations" in result and len(result["translations"]) > 0:
            return result["translations"][0]["text"]
        else:
            print(f"  ⚠️ Unexpected API response: {result}")
            return text
            
    except requests.exceptions.Timeout:
        print(f"  ⚠️ Translation timeout - text may be too long")
        return text
    except requests.exceptions.RequestException as e:
        print(f"  ❌ API Error: {e}")
        return text
    except Exception as e:
        print(f"  ❌ Error translating text: {e}")
        return text


def parse_frontmatter(file_path):
    """
    Parses Hugo frontmatter (YAML) and content.
    
    Returns:
        tuple: (frontmatter_dict, body_content, success_flag)
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to capture YAML frontmatter (matches --- at start, content, ---)
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?", content, re.DOTALL)
    
    if match:
        fm_text = match.group(1)
        body = content[match.end():]
        try:
            fm = yaml.safe_load(fm_text)
            if fm is None:
                fm = {}
            return fm, body, True
        except yaml.YAMLError as e:
            print(f"  ⚠️ Error parsing YAML in {file_path}: {e}")
            return None, content, False
    else:
        # No frontmatter found
        return {}, content, True


def translate_frontmatter(fm, api_key):
    """
    Translate specific frontmatter fields.
    
    Args:
        fm: Frontmatter dictionary
        api_key: DeepL API key
    
    Returns:
        Translated frontmatter dictionary
    """
    translated_fm = fm.copy()
    
    # Translate title
    if "title" in translated_fm and translated_fm["title"]:
        print("    → Translating title...")
        translated_fm["title"] = translate_text(translated_fm["title"], api_key)
    
    # Translate description
    if "description" in translated_fm and translated_fm["description"]:
        print("    → Translating description...")
        translated_fm["description"] = translate_text(translated_fm["description"], api_key)
    
    # Note: tags and categories are usually kept in original language for SEO consistency
    # If you want to translate them, uncomment below:
    # if "tags" in translated_fm and isinstance(translated_fm["tags"], list):
    #     translated_fm["tags"] = [translate_text(tag, api_key) for tag in translated_fm["tags"]]
    
    return translated_fm


def translate_body(body, api_key):
    """
    Translate the body content while preserving markdown structure.
    
    For very long content, we split by paragraphs to avoid API limits.
    
    Args:
        body: Markdown body content
        api_key: DeepL API key
    
    Returns:
        Translated body content
    """
    if not body or not body.strip():
        return ""
    
    # Split by double newlines (paragraphs) to handle long content
    # But preserve code blocks and HTML
    
    # First, protect code blocks and HTML
    code_blocks = []
    html_blocks = []
    
    # Extract fenced code blocks (```...```)
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"<<<CODE_BLOCK_{len(code_blocks)-1}>>>"
    
    protected_body = re.sub(r"```[\s\S]*?```", save_code_block, body)
    
    # Extract inline code (`...`)
    inline_codes = []
    def save_inline_code(match):
        inline_codes.append(match.group(0))
        return f"<<<INLINE_CODE_{len(inline_codes)-1}>>>"
    
    protected_body = re.sub(r"`[^`]+`", save_inline_code, protected_body)
    
    # Extract HTML tags like <script>...</script>
    def save_html_block(match):
        html_blocks.append(match.group(0))
        return f"<<<HTML_BLOCK_{len(html_blocks)-1}>>>"
    
    protected_body = re.sub(r"<script[\s\S]*?</script>", save_html_block, protected_body)
    protected_body = re.sub(r"<style[\s\S]*?</style>", save_html_block, protected_body)
    
    # Preserve markdown image syntax
    images = []
    def save_image(match):
        images.append(match.group(0))
        return f"<<<IMAGE_{len(images)-1}>>>"
    
    protected_body = re.sub(r"!\[([^\]]*)\]\([^)]+\)", save_image, protected_body)
    
    # Now translate
    print("    → Translating body content...")
    translated_body = translate_text(protected_body, api_key)
    
    # Restore protected content
    for i, code in enumerate(code_blocks):
        translated_body = translated_body.replace(f"<<<CODE_BLOCK_{i}>>>", code)
    
    for i, code in enumerate(inline_codes):
        translated_body = translated_body.replace(f"<<<INLINE_CODE_{i}>>>", code)
    
    for i, html in enumerate(html_blocks):
        translated_body = translated_body.replace(f"<<<HTML_BLOCK_{i}>>>", html)
    
    for i, img in enumerate(images):
        translated_body = translated_body.replace(f"<<<IMAGE_{i}>>>", img)
    
    return translated_body


def write_translated_file(output_path, fm, body):
    """
    Write the translated content to a file.
    
    Args:
        output_path: Path to output file
        fm: Frontmatter dictionary
        body: Translated body content
    """
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(fm, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        f.write("---\n")
        f.write(body)


def main():
    parser = argparse.ArgumentParser(description="Translate Hugo blog posts using DeepL API")
    parser.add_argument("--force", action="store_true", help="Re-translate all posts, overwriting existing translations")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be translated without making changes")
    args = parser.parse_args()
    
    api_key = get_api_key()
    
    print("=" * 60)
    print("🌐 DeepL Translation Script for Hugo Blog")
    print("=" * 60)
    
    if args.dry_run:
        print("🔍 DRY RUN MODE - No files will be modified\n")
    
    if args.force:
        print("⚠️ FORCE MODE - Existing translations will be overwritten\n")
    
    print(f"📁 Scanning {CONTENT_DIR} for posts to translate...\n")
    
    if not CONTENT_DIR.exists():
        print(f"❌ Error: Directory {CONTENT_DIR} not found!")
        print("   Please run this script from the Hugo site root directory.")
        sys.exit(1)
    
    # Get all Chinese markdown files (excluding .en.md)
    chinese_posts = [
        f for f in CONTENT_DIR.glob("*.md")
        if not f.name.endswith(".en.md")
    ]
    
    if not chinese_posts:
        print("📭 No posts found to translate.")
        return
    
    print(f"📝 Found {len(chinese_posts)} Chinese post(s)\n")
    
    translated_count = 0
    skipped_count = 0
    error_count = 0
    
    for src_file in chinese_posts:
        base_name = src_file.stem
        en_file = src_file.parent / f"{base_name}.en.md"
        
        # Check if translation already exists
        if en_file.exists() and not args.force:
            print(f"⏭️  Skipping {src_file.name} (translation exists: {en_file.name})")
            skipped_count += 1
            continue
        
        print(f"🔄 Translating: {src_file.name}")
        
        if args.dry_run:
            print(f"   → Would create: {en_file.name}")
            translated_count += 1
            continue
        
        # Parse the source file
        fm, body, success = parse_frontmatter(src_file)
        
        if not success:
            print(f"   ❌ Failed to parse frontmatter, skipping...")
            error_count += 1
            continue
        
        try:
            # Translate frontmatter
            translated_fm = translate_frontmatter(fm, api_key)
            
            # Translate body
            translated_body = translate_body(body, api_key)
            
            # Write output file
            write_translated_file(en_file, translated_fm, translated_body)
            
            print(f"   ✅ Saved: {en_file.name}")
            translated_count += 1
            
        except Exception as e:
            print(f"   ❌ Error: {e}")
            error_count += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Translation Summary")
    print("=" * 60)
    print(f"   ✅ Translated: {translated_count}")
    print(f"   ⏭️  Skipped:    {skipped_count}")
    print(f"   ❌ Errors:     {error_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
