from fastapi import APIRouter, Depends, UploadFile, File, status
from fastapi.responses import JSONResponse
from helper.config import get_settings, Settings
from controllers import DataController

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(
    project_id: str,
    file: UploadFile = File(...),
    app_settings: Settings = Depends(get_settings)
):
    controller = DataController()
    is_valid, result_signal = await controller.validate_upload_file(file=file, app_settings=app_settings)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}
        )
    return {"signal": result_signal}
