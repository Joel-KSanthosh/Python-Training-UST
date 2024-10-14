from venv import logger

from token_decode import Token
from checker import NameAndIsActive,NameAndIsInActive,NoNameAndActiveOrInactive,UnknownPerson
from handler import Handler
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)


class Main:
    logger = logging.getLogger(__name__)
    token_list = [
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm9obiBEb2UiLCJzdGF0dXMiOiJhY3RpdmUifQ.80bUlri4iAG2wChNcPgpmIo0p_M0b6IReaYXeEZkKuo",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSm9lbCIsInN0YXR1cyI6ImFjdGl2ZSJ9.qn9KjY4M6AzW3cTRIdQ5UQWGejFdvJaogvNYf8Gmeiw",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQXJ0aHVyZSIsInN0YXR1cyI6ImFjdGl2ZSJ9.84pJ1KuQubc1xQiQTAM6lAGOP7fJza-qO1Z0ULBs3Oo",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiSmsiLCJzdGF0dXMiOiJpbmFjdGl2ZSJ9.HAcBYhNKngltUgQkTq885DYWiQLHma7sfFM6YBTAhTo",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJpbmFjdGl2ZSJ9.KXBG_JiGOQux1fIUSZqzS9g-mbBHoL2GFhwrk6GgmLc",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJhY3RpdmUifQ.n1B2IZ5yLGHMLEIiDNxeaEMpTayX-18JqLfR33HzBHM",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.P4Lqll22jQQJ1eMJikvNg5HKG-cKB0hUZA9BZFIG7Jk",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiIifQ.gtT3UqBjEP9bm2wmHEnxSeeM5UmmyjUk1XnW2v1Ab1I",
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiIiwic3RhdHVzIjoiaW5hY3RpdmUifQ.d8rh9w0L2tyoaz3lkNFmyJaLXMPqABdV13madscq4gM"
        ]


    def start(self,handler : Handler):
        for i in self.token_list:
            header,payload,signature = i.split('.')
            decoder = Token(header,payload,signature)
            request = decoder.verify_signature()
            logger.info(request)
            result = handler.handle(request)
            print(result)


    def setup(self):
        checker1 = NameAndIsActive()
        checker2 = NameAndIsInActive()
        checker3 = NoNameAndActiveOrInactive()
        checker4 = UnknownPerson()
        checker1.set_next(checker2).set_next(checker3).set_next(checker4)
        self.start(checker1)



if __name__ == '__main__':
    main = Main()
    main.setup()