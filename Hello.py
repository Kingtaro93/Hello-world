import sys

def greet(name: str = "World") -> str:
    return "Hello, " + name + "!"


def main() -> int:
    target = sys.argv[1] if len(sys.argv) > 1 else "World"
    sys.stdout.write("Hello, " + target + "!\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
