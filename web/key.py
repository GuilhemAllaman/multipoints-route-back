class KeyManager:

    tokens = {
        'ors': {
            'counter': 0,
            'keys': [
                '5b3ce3597851110001cf6248825666083b1e45f79ea80b6d26f8b0a2'
            ]
        }
    }

    def token(self, service_name: str) -> str:
        service = self.tokens[service_name]
        key = service['keys'][service['counter']]
        service['counter'] = (service['counter'] + 1) % len(service['keys'])
        return key