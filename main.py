import os

LINE = "The thunderstorm at 2 a.m. drove my hissing cat into my lap, and she stayed, purring, till the rain stopped."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()