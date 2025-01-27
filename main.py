import unpacker


def unpack(save_path):
    try:
        unpacker.main("unpack", save_path, "result")
        print("Save file unpacked")
    except:
        print("Save invalid")


def main():
    save = ""
    unpacker.main("unpack", save, "result")
    unpacker.main("repack", save, "result")


if __name__ == "__main__":
    main()
