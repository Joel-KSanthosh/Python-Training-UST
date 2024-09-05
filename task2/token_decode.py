import base64
import hmac
import hashlib

class Token:
    def __init__(self,header,payload,signature) -> None: # noqa
        self.__header = header
        self.__payload = payload
        self.__signature = signature

    def __decode_header(self) -> str:
        __encoded_header_byte = self.__header.encode('utf-8')
        __decoded_header_byte = base64.b64decode(__encoded_header_byte + b'=' * (-len(__encoded_header_byte)%4))
        __decoded_header = __decoded_header_byte.decode('utf-8')
        return __decoded_header

    def __decode_payload(self) -> str:
        __encoded_payload_byte = self.__payload.encode('utf-8')
        __decoded_payload_byte = base64.b64decode(__encoded_payload_byte + b'=' * (-len(__encoded_payload_byte)%4))
        __decoded_payload = __decoded_payload_byte.decode('utf-8')
        return __decoded_payload

    def verify_signature(self) -> None:
        secret = "newsed"
        message = self.__header + '.' + self.__payload
        __signature = hmac.new(
            key = bytes(secret,'utf-8'),
            msg = bytes(message,'utf-8'),
            digestmod = hashlib.sha256
        ).digest()

        __verify = base64.urlsafe_b64encode(__signature).decode('utf-8').rstrip('=')

        if __verify == self.__signature:
            print("Signature Verification Successful")
            print(f"Decoded header = {self.__decode_header()}")
            print(f"Decoded payload = {self.__decode_payload()}")
        else:
            print("Signature Verification Failed")

if __name__ == '__main__':
    header,payload,signature = list(input("Enter the token : ").split("."))
    t = Token(header,payload,signature)
    t.verify_signature()
    
    
    