from typing import Optional, List

EVENT_TYPE_CREATED: str = ...
EVENT_TYPE_MODIFIED: str = ...
EVENT_TYPE_DELETED: str = ...
EVENT_TYPE_MOVED: str = ...


class FileSystemEvent:
    event_type: str
    is_directory: bool
    src_path: str

    def __init__(self, src_path: str) -> None: ...


class FileSystemMovedEvent(FileSystemEvent):
    dest_path: str


class FileSystemEventHandler:
    def dispatch(self, event: FileSystemEvent) -> None: ...
    def on_any_event(self, event: FileSystemEvent) -> None: ...
    def on_created(self, event: FileSystemEvent) -> None: ...
    def on_deleted(self, event: FileSystemEvent) -> None: ...
    def on_modified(self, event: FileSystemEvent) -> None: ...
    def on_moved(self, event: FileSystemEvent) -> None: ...


class PatternMatchingEventHandler(FileSystemEventHandler):
    case_sensitive: bool
    ignore_directories: bool
    ignore_patterns: List[str]
    patterns: List[str]

    def __init__(self, patterns: Optional[List[str]]=None, ignore_patterns: Optional[List[str]]=None, ignore_directories: bool=False, case_sensitive: bool=False) -> None: ...
    def dispatch(self, event: FileSystemEvent) -> None: ...
