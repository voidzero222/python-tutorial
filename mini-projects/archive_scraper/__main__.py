import argparse
from pathlib import Path


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
        "--output_directory",
        action = "store",
        default = "/home/Videos",
        help = "The directory for the files to be scraped to.",
        dest = "output_directory",
    )

    parser.set_defaults(func = parser.print_help)
    
    args = parser.parse_args()
    
    url: str = args.url 
    output_dir :Path = Path(args.output_directory).absolute().resolve()
    
if __name__ == "__main__":
    main()
