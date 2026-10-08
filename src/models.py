from pydantic import BaseModel, Field


class CodeSnippet(BaseModel):
    part_number: int = Field(
        ..., le=3, description="Only Parts 1, 2, and 3 are allowed"
    )
    summary: str
    code: str


class PageData(BaseModel):
    part_title: str
    snippets: list[CodeSnippet]
