import os
import requests
import hashlib
from urllib.parse import urlparse

def create_directory(dir_name="Fetched_Images"):
    """Create a directory if it doesn't exist."""
    os.makedirs(dir_name, exist_ok=True)
    return dir_name

def get_safe_filename(url):
    """Generate a filename from the URL, ensuring it’s safe and has an image extension."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename or '.' not in filename:
        filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"  # fallback unique name
    return filename

def hash_file(file_path):
    """Compute an MD5 hash of the file content."""
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def is_duplicate(content, downloaded_hashes):
    """Check if file content is already downloaded (based on hash)."""
    content_hash = hashlib.md5(content).hexdigest()
    return content_hash in downloaded_hashes, content_hash

def is_safe_content(response):
    """
    Check HTTP headers before saving the file.
    Ensures it's an image and not malicious data.
    """
    content_type = response.headers.get("Content-Type", "").lower()
    content_length = response.headers.get("Content-Length")

    # Only allow certain MIME types
    if not content_type.startswith("image/"):
        print(f"⚠️ Skipping: Unsupported content type '{content_type}'")
        return False

    # Optional precaution: skip files over 10MB
    if content_length and int(content_length) > 10 * 1024 * 1024:
        print(f"⚠️ Skipping: File too large ({int(content_length)/1024/1024:.2f} MB)")
        return False

    return True

def download_images(urls):
    folder = create_directory()
    downloaded_hashes = set()

    for url in urls:
        url = url.strip()
        if not url:
            continue

        print(f"\n🔗 Fetching: {url}")
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # Verify headers before saving
            if not is_safe_content(response):
                continue

            # Check for duplicate image content
            duplicate, content_hash = is_duplicate(response.content, downloaded_hashes)
            if duplicate:
                print("⚠️ Duplicate image detected, skipping download.")
                continue

            # Save the image
            filename = get_safe_filename(url)
            filepath = os.path.join(folder, filename)

            with open(filepath, "wb") as f:
                f.write(response.content)

            downloaded_hashes.add(content_hash)
            print(f"✅ Saved as: {filepath}")

        except requests.exceptions.MissingSchema:
            print("❌ Invalid URL format.")
        except requests.exceptions.ConnectionError:
            print("❌ Connection failed. Check your internet or the URL.")
        except requests.exceptions.Timeout:
            print("❌ Request timed out.")
        except requests.exceptions.HTTPError as e:
            print(f"❌ HTTP error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    # Prompt user for multiple URLs
    print("Enter image URLs (comma-separated):")
    user_input = input("> ")
    urls = [u.strip() for u in user_input.split(",") if u.strip()]
    
    if urls:
        download_images(urls)
    else:
        print("No URLs provided.")
