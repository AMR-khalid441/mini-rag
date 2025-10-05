from .BaseController import BaseController
from fastapi import UploadFile, Depends
from helper.config import Settings, get_settings
from models import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1048576  # 1 MB in bytes

    async def validate_upload_file(self, file: UploadFile, app_settings: Settings = Depends(get_settings)):
        # Validate type
        if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        # Check file size
        contents = await file.read()
        size_in_bytes = len(contents)
        file.file.seek(0)

        if size_in_bytes > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value

        return True, ResponseSignal.FILE_UPLOAD_SUCCESS.value
