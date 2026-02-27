#!/usr/bin/python3
from . import cli_system


def load_mapping(path):
    """
    Load mapping file into dict using strict ' = ' delimiter.
    """

    mapping = {}

    with open(path, "r") as f:
        for line in f:
            line = line.rstrip("\n")

            if not line.strip():
                continue

            if " = " not in line:
                cli_system.error(f"invalid line in mapping: '{line}'")
                return None

            key, value = line.split(" = ", 1)

            if key == "":
                cli_system.error(f"invalid key in mapping: '{line}'")
                return None

            if value == "":
                cli_system.error(f"invalid value in mapping: '{line}'")
                return None

            mapping[key] = value

    return mapping


def encrypt(text: str, mapping: dict):
    """
    Encrypt text using mapping.
    """

    if mapping is None:
        return None

    unsupported = sorted(set(ch for ch in text if ch not in mapping))
    if unsupported:
        cli_system.error(
            f"text contains characters not supported by mapping: {', '.join(unsupported)}"
        )
        return None

    return "".join(mapping[ch] for ch in text)


def decrypt(text: str, mapping: dict):
    """
    Decrypt text using mapping.
    """

    if mapping is None:
        return None

    rev_mapping = {v: k for k, v in mapping.items()}

    lengths = {len(v) for v in mapping.values()}
    if len(lengths) != 1:
        cli_system.error("invalid mapping: all encoded values must be same length")
        return None

    token_len = lengths.pop()

    if len(text) % token_len != 0:
        cli_system.error("encrypted text chunk length is invalid for this mapping")
        return None

    decrypted_chars = []
    unsupported_chunks = []

    for i in range(0, len(text), token_len):
        chunk = text[i:i + token_len]

        if chunk in rev_mapping:
            decrypted_chars.append(rev_mapping[chunk])
        else:
            unsupported_chunks.append(chunk)

    if unsupported_chunks:
        cli_system.error(
            f"encrypted text contains unsupported chunks: {', '.join(unsupported_chunks)}"
        )
        return None

    return "".join(decrypted_chars)
