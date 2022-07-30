import base64


def image_encoding(path):
    with open(path, "rb") as image_file:
        read = image_file.read()
        encoded_string = base64.b64encode(read)
    return encoded_string


def image_decoding(code):
    path = input("Enter the path to save the file: ")
    with open(path, "wb") as fh:
        fh.write(base64.decodebytes(code))
    fh.close()


def text_encoding(text):
    text = text.encode("ascii")
    base64_bytes = base64.b64encode(text)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def text_decoding(encode_text):
    base64_bytes = encode_text.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    return sample_string

