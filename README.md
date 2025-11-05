🖼️ Multi Image Downloader
==========================

A robust Python script that downloads one or more images from user-provided URLs.It ensures **safety, efficiency, and reliability** by validating HTTP headers, avoiding duplicate downloads, and handling errors gracefully.

🚀 Features
-----------

✅ **Multiple URL support** – Download several images in one run (comma-separated input).
✅ **Automatic folder creation** – Saves all images into a Fetched\_Images directory.
✅ **Duplicate detection** – Uses MD5 hashing to prevent saving the same image twice.
✅ **Safe content verification** – Downloads only files that are confirmed to be images.
✅ **Error handling** – Gracefully manages invalid URLs, timeouts, and connection failures.
✅ **Header checks** – Validates Content-Type and Content-Length before saving files.

🧩 Requirements
---------------

Make sure you have **Python 3.7+** installed and the **requests** library:

```bash
pip install requests
```

📂 Project Structure

```bash
multi_image_downloader/
│
├── downloader.py        # Main script
├── README.md            # Project documentation
└── Fetched_Images/      # Folder where downloaded images are stored
```

🖥️ Usage

1. Run the script:

```bash
python3 downloader.py
```

2. Enter one or more image URLs, separated by commas:

```shell
Enter image URLs (comma-separated):
> https://example.com/cat.jpg, https://example.com/dog.png
```

3. The script will:

- Create a Fetched_Images folder if it doesn’t exist

- Download each image safely

- Skip duplicates or invalid files

- Print the save location for each successful download

⚙️ How It Works
1. Directory Management

If `Fetched_Images/` doesn’t exist, the script creates it automatically.

2. Safe File Naming

Extracts filenames from URLs; if none exist, generates a safe MD5-based filename.

3. HTTP Header Validation

Before saving, the script checks:

- `Content-Type`: must begin with `"image/"`

- `Content-Length`: optional safeguard, skips files larger than 10MB

4. Duplicate Detection

Each file’s content is hashed (MD5).
If an image’s hash matches one already downloaded, it’s skipped automatically.

5. Exception Handling

Handles the following gracefully:

- Invalid URLs

- Network errors

- Timeouts

- HTTP errors (e.g. 404, 403)

- Unknown exceptions

🔒 Safety Precautions

When downloading from unknown sources:

- Always validate MIME types (as done in this script).

- Avoid downloading extremely large files.

- Avoid executing or opening files directly after downloading.

- Consider running the script in a sandboxed environment if needed.

🧠 Example Output

```bash
Enter image URLs (comma-separated):
> https://example.com/cat.jpg, https://example.com/dog.jpg, https://example.com/cat.jpg

🔗 Fetching: https://example.com/cat.jpg
✅ Saved as: Fetched_Images/cat.jpg

🔗 Fetching: https://example.com/dog.jpg
✅ Saved as: Fetched_Images/dog.jpg

🔗 Fetching: https://example.com/cat.jpg
⚠️ Duplicate image detected, skipping download.

```

📜 License

This project is open-source and available under the MIT License.
You are free to use, modify, and distribute it for personal or commercial use.

👨‍💻 Author

Richard Orido
Built as a challenge to implement safe, concurrent image fetching in Python.
