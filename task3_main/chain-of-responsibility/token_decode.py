import base64
import hmac
import hashlib
import json

class Token:
    def __init__(self,header : str,payload : str,signature : str):
        self.__header : str = header
        self.__payload : str = payload
        self.__signature : str = signature

    def __decode_header(self) -> str:
        __encoded_header_byte = self.__header.encode('utf-8')
        __decoded_header_byte = base64.b64decode(__encoded_header_byte + b'=' * (-len(__encoded_header_byte) % 4))
        __decoded_header = __decoded_header_byte.decode('utf-8')
        return __decoded_header

    def __decode_payload(self) -> str:
        __encoded_payload_byte = self.__payload.encode('utf-8')
        __decoded_payload_byte = base64.b64decode(__encoded_payload_byte + b'=' * (-len(__encoded_payload_byte) % 4))
        __decoded_payload = __decoded_payload_byte.decode('utf-8')
        return __decoded_payload


    def verify_signature(self):
        secret: str = "test"
        message: str = self.__header + '.' + self.__payload
        __signature: bytes = hmac.new(
            key=bytes(secret, 'utf-8'),
            msg=bytes(message, 'utf-8'),
            digestmod=hashlib.sha256
        ).digest()

        __verify: str = base64.urlsafe_b64encode(__signature).decode('utf-8').rstrip('=')

        if __verify == self.__signature:
            data = json.loads(self.__decode_payload())
            return data
        return None


