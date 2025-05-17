"""Autograding script for student homework."""

import os
import subprocess


def test_homework():
    """Test Word Count"""

    if not os.path.exists("homework/src/"):
        raise Exception("homework/src/ directory does not exist")

    if not os.path.exists("homework/src/_internals/"):
        raise Exception("homework/src/_internals/ directory does not exist")

    if not os.path.exists("homework/src/_internals/parse_args_mixin.py"):
        raise Exception("homework/src/_internals/parse_args_mixin.py does not exist")

    if not os.path.exists("homework/src/_internals/read_all_lines_mixin.py"):
        raise Exception("homework/src/_internals/read_all_lines_mixin.py does not exist")

    if not os.path.exists("homework/src/_internals/preprocess_lines_mixin.py"):
        raise Exception("homework/src/_internals/preprocess_lines_mixin.py does not exist")

    if not os.path.exists("homework/src/_internals/split_into_words_mixin.py"):
        raise Exception("homework/src/_internals/split_into_words_mixin.py does not exist")

    if not os.path.exists("homework/src/_internals/count_words_mixin.py"):
        raise Exception("homework/src/_internals/count_words_mixin.py does not exist")

    if not os.path.exists("homework/src/_internals/write_count_words_mixin.py"):
        raise Exception("homework/src/_internals/write_count_words_mixin.py does not exist")

    if not os.path.exists("homework/src/main.py"):
        raise Exception("homework/src/main.py does not exist")

    try:
        subprocess.run(
            ["python3", "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    if not os.path.exists("data/output/"):
        raise Exception("'data/output/' directory does not exist")

    results_file = "data/output/results.tsv"
    if not os.path.exists(results_file):
        raise Exception(f"'{results_file}' file does not exist")

    with open(results_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        result = {}
        for line in lines:
            key, value = line.strip().split("\t")
            result[key] = int(value)

    assert result.get("analytics", 0) == 5, "Incorrect count for 'analytics'"
    assert result.get("business", 0) == 7, "Incorrect count for 'business'"
    assert result.get("by", 0) == 3, "Incorrect count for 'by'"
    assert result.get("algorithms", 0) == 2, "Incorrect count for 'algorithms'"
    assert result.get("analysis", 0) == 4, "Incorrect count for 'analysis'"
