from enum import Enum


class Status(Enum):
    """fields for status types"""
    OPEN = "open"
    IN_PROGRESS = "in progress"
    IN_REVIEW = "in review"
    TESTING = "testing"
    BLOCKED = "blocked"
    DONE = "done"
