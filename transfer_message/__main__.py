def main(args):
    # When the console_scripts entry point is used it passes no arguments
    if args is None:
        import sys
        args = sys.argv[1:]
    print("Hello World")

if __name__ == "__main__":
    main()
