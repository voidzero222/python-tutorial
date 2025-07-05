import argparse
from pathlib import Path
import sys

from .scraper import scrape_archive  # type: ignore

__version__ = (0, 1, 0)
version_string = ".".join(map(str, __version__))


def main() -> None:
    parser = argparse.ArgumentParser(
        prog = "archive_scraper",
        description = "Scrape audio files from an archive.org URL.",
    )
    
    parser.add_argument(
        "url",
        action = "store",
        type = str,
        help = "The URL to the archive.org webpage you wish to scrape from.",
    )
    
    parser.add_argument(
        "-o",
        "--output-directory",
        action = "store",
        default = Path.home() / "Music",
        help = "The directory for the files to be scraped to.",
        dest = "output_directory",
    )

    parser.add_argument(
        "-v",
        "--version",
        action = "version",
        help = "The program version.",
        version = "%(prog)s v{version}".format(version=version_string),
    )
    
    parser.set_defaults(func=parser.print_help)
    
    args = parser.parse_args()
    
    url: str = args.url
    output_dir = Path(args.output_directory).absolute().resolve()
    
    if not url.startswith("https://archive.org"):
        print(f"{url} is not a valid URL, try again.")
        sys.exit(1)
        
    try:
        scrape_archive(url, output_dir)
    except FileNotFoundError:
        print(f"{output_dir} is an invalid directory, try again.")
        sys.exit(2)
    except (PermissionError, OSError):
        print(f"No write permissions for: {output_dir}. Try again.")
        sys.exit(3)

if __name__ == "__main__":
    main()
