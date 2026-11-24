"""Two Days of Quiet Dread — entry program.

Writes one code review comment to /output/entry.txt and prints it.
The comment approves the pull request while carrying quiet
existential dread: it passes, it ships, and it outlives us.
"""

import os

COMMENT = (
    "LGTM. It passes, it ships, and it will keep running in the dark "
    "long after we've forgotten why."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(COMMENT)
    print(COMMENT)


if __name__ == "__main__":
    main()
