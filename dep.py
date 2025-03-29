import sys

def main():
    # Check if there are enough command-line arguments
    if len(sys.argv) < 4:
        print("Please provide at least 3 arguments.")
        return

    s1 = sys.argv[1]
    s2 = sys.argv[2]
    s3 = sys.argv[3]

    print("name", s1)
    print("roll no", s2)
    print("department", s3)

if __name__ == "__main__":
    main()

