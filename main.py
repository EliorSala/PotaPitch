from initializer import initialize


def main():
    facade = initialize()

    print("Starting facade")
    facade.start()


if __name__ == '__main__':
    main()
