from os import system


def autoclean() -> None:
    system('rm -rf .pytest_cache')
    system('find . -name __pycache__ -exec rm -rf {} \;')  # noqa: W605
