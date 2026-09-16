import argparse
import logging
from pathlib import Path
from datetime import datetime, timedelta

def setup_logger():
    """Configures logging to output to both a log file and the console."""
    logger = logging.getLogger("cleanup_tool")
    logger.setLevel(logging.INFO)

    # 1. Create a formatter defining the log layout
    log_format = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    # 2. File Handler: Appends logs permanently to a file
    file_handler = logging.FileHandler("cleanup.log", encoding="utf-8")
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # 3. Console Handler: Displays logs on screen in real-time
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    return logger

def clean_directory(target_folder, extensions, days_old, dry_run=False):
    folder = Path(target_folder)
    logger = logging.getLogger("cleanup_tool") # Retrieve our configured logger
    
    if not folder.exists():
        logger.error(f"The directory '{target_folder}' does not exist.")
        return

    cutoff_date = datetime.now() - timedelta(days=days_old)

    logger.info(f"Scanning directory: {folder.resolve()}")
    logger.info(f"Looking for types: {', '.join(extensions)}")
    logger.info(f"Target age: Older than {days_old} days (Before {cutoff_date.strftime('%Y-%m-%d')})")
    
    if dry_run:
        logger.warning("Running in DRY RUN mode. No files will be deleted.")

    for file_path in folder.glob("*.*"):
        if file_path.suffix in extensions:
            mtime = datetime.fromtimestamp(file_path.stat().st_mtime)
            
            if mtime < cutoff_date:
                if dry_run:
                    logger.info(f"[DRY RUN] Would delete (Age: {mtime.strftime('%Y-%m-%d')}): {file_path.name}")
                else:
                    try:
                        file_path.unlink()
                        logger.info(f"Deleted: {file_path.name}")
                    except PermissionError:
                        logger.warning(f"Skipped: Permission denied for {file_path.name}")
                    except Exception as e:
                        logger.error(f"Failed to delete {file_path.name}. Reason: {e}")

if __name__ == "__main__":
    # Initialize our dual-output logging system
    setup_logger()

    parser = argparse.ArgumentParser(
        description="A CLI tool to automatically clean up specific file types with logging."
    )
    parser.add_argument("-d", "--dir", required=True, help="The path to the directory to clean.")
    parser.add_argument("-e", "--ext", nargs="+", required=True, help="Extensions to target (e.g., .tmp .log).")
    parser.add_argument("--days", type=int, default=0, help="Only delete files older than this many days.")
    parser.add_argument("--dry-run", action="store_true", help="Run without deleting anything.")
    
    args = parser.parse_args()
    
    clean_directory(
        target_folder=args.dir, 
        extensions=args.ext, 
        days_old=args.days, 
        dry_run=args.dry_run
    )
