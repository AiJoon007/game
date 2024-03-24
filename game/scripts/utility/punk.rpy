#####################################
##     Created by briandeheus      ##
## https://github.com/briandeheus  ##
##    Implementation and changes   ##
##           LoafyLemon            ##
#####################################
init python:
    import binascii
    import struct
    import zlib

    class ImagePayload(NoRollback):

        CHUNK_TYPE_END = "IEND"
        CHUNK_TYPE_PUNK = "wtSi"
        MAX_BYTES = 2147483647
        SIGNATURE_BYTES = 8
        BYTES_IN_KB = 2014

        def __init__(self):
            pass

        def bytes_to_hex(self, b):
            return b.hex()

        def bytes_to_utf(self, b):
            return b.decode()

        def bytes_to_int(self, b):
            return int(self.bytes_to_hex(b), 16)

        def read_bytes(self, f, byte_count: int):
            return f.read(byte_count)

        def rewind_bytes(self, f, byte_count):
            f.seek(f.tell() - byte_count)

        def get_file_length(self, f):
            f.seek(0, os.SEEK_END)
            file_length = f.tell()
            f.seek(0)

            return file_length

        def read_chunk(self, f):
            chunk_size = self.read_bytes(f, 4)
            chunk_type = self.read_bytes(f, 4)
            chunk_content = self.read_bytes(f, self.bytes_to_int(chunk_size))
            chunk_crc = self.read_bytes(f, 4)

            return [chunk_size, chunk_type, chunk_content, chunk_crc]

        def inject_punk_chunk(self, f, content):
            chunk_size = len(content)

            if chunk_size > self.MAX_BYTES:
                raise ValueError(f"Cannot inject more than {self.MAX_BYTES} bytes")

            print(f"Injecting {self.CHUNK_TYPE_PUNK} chunk {chunk_size / self.BYTES_IN_KB} kb")

            # Create a byte array to store our chunk data in.
            tmp_bytes = bytearray()
            # First write the chunk type
            tmp_bytes.extend(self.CHUNK_TYPE_PUNK.encode())
            # Now write the bytes of whatever we're trying to hide
            tmp_bytes.extend(content)

            # Write the chunk size
            f.write(bytearray(struct.pack("!i", chunk_size)))

            # And the content
            f.write(tmp_bytes)

            crc = binascii.crc32(tmp_bytes)
            crc_bytes = crc.to_bytes(4, "big")
            print("Chunk CRC", self.bytes_to_hex(crc_bytes))
            f.write(crc_bytes)

            print("Chunk injected!")

        def list(self, input):
            path = os.path.join(config.gamedir, "outfits", input)

            with open(path, "rb") as input_file:

                input_file_length = self.get_file_length(input_file)
                input_file.read(self.SIGNATURE_BYTES)

                while True:
                    chunk_size, chunk_type, chunk_content, chunk_crc = self.read_chunk(input_file)
                    chunk_type_str = self.bytes_to_utf(chunk_type)
                    print(f"Chunk {chunk_type_str}, {self.bytes_to_int(chunk_size)} bytes")

                    if input_file.tell() >= input_file_length:
                        return

        def inject(self, input, output, content):
            input_path = os.path.join(config.gamedir, "outfits", input)
            output_path = os.path.join(config.gamedir, "outfits", output)
            content = zlib.compress(str(content).encode())

            with open(input_path, "rb") as input_file, open(output_path, "wb") as output_file:

                input_file_length = self.get_file_length(input_file)
                output_file.write(input_file.read(self.SIGNATURE_BYTES))

                while True:
                    chunk_size, chunk_type, chunk_content, chunk_crc = self.read_chunk(input_file)
                    chunk_type_str = self.bytes_to_utf(chunk_type)
                    print(f"Chunk {chunk_type_str}, {self.bytes_to_int(chunk_size)} bytes")

                    if chunk_type_str == self.CHUNK_TYPE_END:
                        self.inject_punk_chunk(output_file, content)

                    output_file.write(chunk_size)
                    output_file.write(chunk_type)
                    output_file.write(chunk_content)
                    output_file.write(chunk_crc)

                    if input_file.tell() >= input_file_length:
                        return

        def extract(self, input):
            print("Attempting to extract punked data from", input)
            path = os.path.join(config.gamedir, "outfits", input)

            with open(path, "rb") as input_file:

                input_file_length = self.get_file_length(input_file)
                input_file.read(self.SIGNATURE_BYTES)

                while True:
                    chunk_size, chunk_type, chunk_content, chunk_crc = self.read_chunk(input_file)
                    chunk_type_str = self.bytes_to_utf(chunk_type)

                    if chunk_type_str == self.CHUNK_TYPE_PUNK:
                        print("Found a punk chunk worth", self.bytes_to_int(chunk_size), "bytes")
                        return zlib.decompress(chunk_content).decode()

                    if input_file.tell() >= input_file_length:
                        print("No punked data found")
                        return
