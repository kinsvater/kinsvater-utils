import shutil
from pathlib import Path
from typing import Optional, Iterable


def copy_samples(source_dir: Path, destination_dir: Path, only_sub_directories: Optional[Iterable[str]] = None) -> None:
    """Make copies of original data.

    Some methods write/delete data as side effects. This is by intention but not ideal for testing purpose. Use this
    function to avoid changes on the original data.

    Note that the content of `destination_dir` will be deleted first.
    """
    if source_dir.absolute() == destination_dir.absolute():
        raise ValueError('Source and destination paths are not allowed to be the same.')

    # Delete destination if already exists to start from clean state:
    if destination_dir.exists():
        shutil.rmtree(destination_dir, ignore_errors=True)

    if only_sub_directories:
        for sub_dir in only_sub_directories:
            shutil.copytree(source_dir / sub_dir, destination_dir / sub_dir)
    else:
        shutil.copytree(source_dir, destination_dir)
