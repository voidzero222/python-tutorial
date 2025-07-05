import argparse
from pathlib import Path

__version__ = ""


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

    parser.add_argument(
        "-V",
        "--version",
        action = "version",
        help = "The version.",
        version = "%(prog)s {version}".format(version = __version__),
    )
    
    parser.set_defaults(func = parser.print_help)
    
    args = parser.parse_args()
    
    url :str = args.url 
    output_dir :Path = Path(args.output_directory).absolute().resolve()
    version :str = args.version
    
if __name__ == "__main__":
    main()
