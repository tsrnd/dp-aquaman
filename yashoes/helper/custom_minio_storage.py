from django_minio.storage import MinioStorage
import mimetypes
from minio.error import InvalidXMLError, InvalidEndpointError,  NoSuchKey, NoSuchBucket
import os
from urllib3.exceptions import MaxRetryError
import datetime
class CustomMinioStorage(MinioStorage):

    def __init__(self, *args, **kwargs):
        super(CustomMinioStorage, self).__init__(*args, **kwargs)
        self._connection = None
    def _save(self, name, content):
        try:
            pathname, ext = os.path.splitext(str(name.encode('utf-8')))
            dir_path, file_name = os.path.split(pathname)
            hashed_name = "{0}/{1}{2}{3}".format(dir_path, datetime.datetime.now().strftime("%y%m%d_%H%M%S"), hash(content), ext)[2:-1]
            if hasattr(content, 'content_type'):
                content_type = content.content_type
            else:
                content_type = mimetypes.guess_type(name.encode('utf-8'))[0]
            if self.connection:
                if not self.connection.bucket_exists(self.bucket):
                    self.connection.make_bucket(self.bucket)
                try:
                    self.connection.put_object(
                        self.bucket, hashed_name, content, content.size, content_type=content_type
                    )
                except InvalidXMLError:
                    pass
                except MaxRetryError:
                    pass
        except Exception as e:
            return hashed_name
        return hashed_name
        