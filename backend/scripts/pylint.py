from os import system


def start_linting() -> None:
    system('pylint -j$(nproc) $(git ls-files "*.py")')
