import base64


class Encoder:
    def _encode_data(self, data : str):
        data_bytes = data.encode("ascii")
        data_base64_bytes = base64.b64encode(data_bytes)
        return data_base64_bytes.decode("ascii")

    def _decode_data(self, data):
        data_bytes = data.encode("ascii")
        data_ascii = base64.b64decode(data_bytes)
        return data_ascii.decode("ascii")