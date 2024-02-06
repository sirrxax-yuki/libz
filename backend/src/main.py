import os
import sys

sys.path.append(os.path.dirname(__file__))

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api.schemas.delete import DeleteKnowledgeRequest, DeleteKnowledgeResponse
from api.schemas.health import HealthCheckResponse
from api.schemas.list import ListKnowledgeRequest, ListKnowledgeResponse
from api.schemas.post import PostKnowledgeRequest, PostKnowledgeResponse
from api.schemas.search import SearchKnowledgeRequest, SearchKnowledgeResponse
from controller.knowledge import KnowledgeController
from models.exception import LibzException
from logs import logger
from time import time


app = FastAPI()

@app.exception_handler(Exception)
async def exceptionHandler(_: Request, exception: Exception):
    if isinstance(exception, LibzException):
        return JSONResponse(status_code=exception.status, content={
            "code": exception.code,
            "message": exception.message,
        })
    else:
        return JSONResponse(status_code=500, content={
            "code": 9999,
            "message": str(exception),
        })

@app.get("/health")
async def health():
    return HealthCheckResponse()

@app.post("/search", response_model=SearchKnowledgeResponse)
async def search(request_body: SearchKnowledgeRequest):
    controller = KnowledgeController()
    response = SearchKnowledgeResponse()
    start = time()
    response.results = controller.fetch_knowledge(
        request_body.user,
        request_body.keyword,
    )
    logger.info(f"fetch_knowledge: {round(time() - start, 3)} sec.")
    return response

@app.post("/post", response_model=PostKnowledgeResponse)
async def post(request_body: PostKnowledgeRequest):
    controller = KnowledgeController()
    response = PostKnowledgeResponse()
    response.knowledge_id = controller.insert_knowledge(
        request_body.user,
        request_body.keywords,
        request_body.knowledge,
        request_body.knowledge_type,
        request_body.private,
    )
    return response

@app.post("/list", response_model=ListKnowledgeResponse)
async def list(request_body: ListKnowledgeRequest):
    controller = KnowledgeController()
    response = ListKnowledgeResponse()
    start = time()
    response.results = controller.listup_knowledge(
        request_body.user,
    )
    logger.info(f"listup_knowledge: {round(time() - start, 3)} sec.")
    return response

@app.delete("/delete", response_model=DeleteKnowledgeResponse)
async def delete(request_body: DeleteKnowledgeRequest):
    controller = KnowledgeController()
    response = DeleteKnowledgeResponse()
    response.update = controller.delete_knowledge(
        request_body.user,
        request_body.knowledge_id,
    )
    return response
