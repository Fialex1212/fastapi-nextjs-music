from fastapi import APIRouter, Request, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import httpx

router = APIRouter()
USER_SERVICE_URL = "http://user-service:8001"


@router.api_route("/users/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def proxy_user_service(path: str, request: Request):
    """Generic proxy for most /users/* routes"""
    try:
        async with httpx.AsyncClient() as client:
            url = f"{USER_SERVICE_URL}/users/{path}"
            method = request.method
            headers = dict(request.headers)

            body = await request.body()

            response = await client.request(
                method,
                url,
                headers=headers,
                content=body,
                params=request.query_params,
            )

        return JSONResponse(content=response.json(), status_code=response.status_code)

    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"User service unreachable: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)


@router.put("/users/{user_id}/avatar")
async def proxy_update_avatar(user_id: int, file: UploadFile = File(...)):
    """Special handling for file uploads"""
    try:
        async with httpx.AsyncClient() as client:
            files = {
                "file": (file.filename, await file.read(), file.content_type)
            }

            response = await client.put(
                f"{USER_SERVICE_URL}/users/{user_id}/avatar",
                files=files,
            )

        return JSONResponse(content=response.json(), status_code=response.status_code)

    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"User service unreachable: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)


@router.delete("/users/{user_id}/avatar")
async def proxy_delete_avatar(user_id: int):
    """Special route for avatar deletion"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                f"{USER_SERVICE_URL}/users/{user_id}/avatar"
            )

        return JSONResponse(content=response.json(), status_code=response.status_code)

    except httpx.RequestError as e:
        raise HTTPException(status_code=502, detail=f"User service unreachable: {str(e)}")
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=e.response.text)
