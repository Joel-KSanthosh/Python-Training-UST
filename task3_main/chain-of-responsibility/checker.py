from handler import AbstractHandler


class NameAndIsActive(AbstractHandler):
    def handle(self, request : dict) -> str:
        try:
            if request.get('name') and request.get('status') == 'active':
                return f'{request.get("name")} is available'
        except KeyError:
            pass
        return super().handle(request)


class NameAndIsInActive(AbstractHandler):
    def handle(self, request: dict) -> str:
        try:
            if request.get('name') and request.get('status') == 'inactive':
                return f'{request.get("name")} is unavailable'
        except KeyError:
             pass
        return super().handle(request)


class NoNameAndActiveOrInactive(AbstractHandler):
    def handle(self, request : dict) -> str:
        try:
            if request.get('status') == 'active' or request.get('status') == 'inactive':
                return f'There is some error in the system'
        except KeyError:
            pass
        return super().handle(request)


class UnknownPerson(AbstractHandler):
    def handle(self, request) -> str:
        return f'Unknown Person is requesting access'

