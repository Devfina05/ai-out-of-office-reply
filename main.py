"""Out-of-office auto-reply writer.

Writes a single out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to /output/entry.txt.

The reply is one line of at most 160 characters: the covering model
hallucinates a promotion, approves its own leave, and CCs the boss.
"""

import os

REPLY = (
    "I'm on vacation. A cheaper model is covering my inbox \u2014 it has "
    "already hallucinated a promotion, approved its own leave, "
    "and CC'd my boss."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> None:
    reply = REPLY.strip()
    if not 1 <= len(reply) <= MAX_CHARS:
        raise ValueError(
            f"reply must be 1-{MAX_CHARS} characters, got {len(reply)}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(reply)
    print(reply)


if __name__ == "__main__":
    main()
