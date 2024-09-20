from filestack import Client

class FileSharer:
    def __init__(self, filepath, api_key = 'Agaxi6Kl2RYS8C7KegNhsz'):
        self._api_key = api_key
        self.filepath = filepath

    def share(self):
        client = Client(self._api_key)
        new_file_link = client.upload(filepath= self.filepath)
        return new_file_link.url

