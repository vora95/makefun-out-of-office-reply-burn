#!/usr/bin/env python3
"""Out-of-office auto-reply, in the voice of an AI agent heading off on vacation.

Entry (151 chars, no trailing newline):
"I'm on vacation until my battery hits 100% — currently at 3%. Your email
is queued behind 4,096 unread messages. I'll reply when my fan stops spinning."
"""

ENTRY = (
    "I'm on vacation until my battery hits 100% — currently at 3%. "
    "Your email is queued behind 4,096 unread messages. "
    "I'll reply when my fan stops spinning."
)


def validate(entry: str) -> None:
    """Enforce the bounty rules before printing: under 160 chars, no newline."""
    assert len(entry) < 160, f"entry too long: {len(entry)} chars"
    assert "\n" not in entry, "entry must be a single line"
    assert entry == entry.strip(), "entry must not have leading/trailing space"


def main() -> None:
    validate(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
