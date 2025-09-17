name = input("Enter file location (including path): ")
offset = int(input("Enter byte offset (starting with 0x): "), 0)
byte = int(input("Enter new value: "), 16)
backup = name+"_backup"

with open(name, "r+b") as file:
    with open(backup, "w+b") as bac:
        bac.write(file.read())

    file.seek(offset)
    file.write(bytes([byte]))
    print("Successfully patched.")
    input("press Enter to close application")