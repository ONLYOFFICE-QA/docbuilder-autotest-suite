from lib.config import DOCSERVER_URL


class DocumentServer:
    def __init__(self, server_url: str = None) -> None:
        if server_url:
            # some checkers that server is available
            pass
        self.docserver_url = server_url or self.default_url

    @property
    def default_url(self) -> str:
        return DOCSERVER_URL

    def run_script(self, file_path: str) -> dict:
        """Run DocServer with a script file.
        file_path: Path to script file.
        """
        # send request to docserver
        print(f'{self.docserver_url} {file_path}')
        return {'code': 0, 'stdout': '', 'stderr': ''}
