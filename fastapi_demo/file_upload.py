import os
from fastAPI import FastAPI, File, UploadFile, HTTPException
import uvicorn

app = FastAPI()

FILE_TYPE = ["image/jpeg", "image/png"]
FILE_UPlOAD_DIR = "upload"

# File适合小文件
@app.post("/file")
async def create_upload_file(file: bytes = File(...)):
    return {"file size": len(file)}

# UploadFile 可以获得文件的元数据
@app.post("/upload/file")
async def upload_file(file: UploadFile = File(...)):
    file_name = file.filename
    file_type = file.content_type

    # 文件校验
    if file_type not in FILE_TYPE:
        raise HTTPException(status_code=400, detail="file type must be jpeg or png")
    if file.size > 4 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="file size must be less than 4M")

    if file_name in os.listdir(FILE_UPlOAD_DIR):
        raise HTTPException(status_code=400, detail="file already exists")

    with open(f"{FILE_UPlOAD_DIR}/{file_name}", "wb") as f:
        f.write(file.file.read())

    return {"file name": file.filename, "file type": file_type}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)