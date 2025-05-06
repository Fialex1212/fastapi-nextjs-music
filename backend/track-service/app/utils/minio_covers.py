from minio import Minio
import os
from fastapi import HTTPException
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class MinIOClient:
    def __init__(self):
        self.client = Minio(
            os.getenv("MINIO_ENDPOINT"),
            access_key=os.getenv("MINIO_ACCESS_KEY"),
            secret_key=os.getenv("MINIO_SECRET_KEY"),
            # secure=os.getenv("MINIO_SECURE", "false").lower() == "true"
            secure=False,
        )
        self.bucket = os.getenv("MINIO_COVER_BUCKET", "track-covers")
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        try:
            if not self.client.bucket_exists(self.bucket):
                self.client.make_bucket(self.bucket)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"MinIO bucket error: {str(e)}")

    def upload_track_cover(
        self, file, track_id: int, track_title: str, file_extension: str
    ):
        object_name = f"track_{track_id}_{track_title}{file_extension}"
        try:
            # Get file size by seeking to end
            file.seek(0, 2)
            file_size = file.tell()
            file.seek(0)

            # Upload with known size if possible
            if file_size > 0:
                self.client.put_object(
                    self.bucket,
                    object_name,
                    file,
                    length=file_size,
                    content_type=self._get_content_type(file_extension),
                )
            else:
                # For unknown size, use multipart upload with part size
                self.client.put_object(
                    self.bucket,
                    object_name,
                    file,
                    length=-1,  # Unknown size
                    part_size=10 * 1024 * 1024,  # 10MB part size
                    content_type=self._get_content_type(file_extension),
                )
            return object_name
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"MinIO upload error: {str(e)}")

    def _get_content_type(self, file_extension: str) -> str:
        return {
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".png": "image/png",
            ".webp": "image/webp",
        }.get(file_extension.lower(), "application/octet-stream")

    def get_track_cover_url(self, object_name: str):
        try:
            return self.client.presigned_get_object(
                self.bucket, object_name, expires=timedelta(seconds=3600)  # 1 hour
            )
        except ConnectionError as ex:
            raise HTTPException(status_code=503, detail="Storage service unavailable")
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail=f"MinIO URL error: {str(e)}")

    def delete_track_cover(self, object_name: str):
        try:
            self.client.remove_object(self.bucket, object_name)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"MinIO delete error: {str(e)}")


minio_cover_client = MinIOClient()
