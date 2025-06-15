from pydantic import BaseModel


class ApplicationInfoGit(BaseModel):
    hash: str = None
    branch: str = None


class ApplicationInfo(BaseModel):
    project: str = None
    version: str = None
    datetime: str
    environment: str
    git: ApplicationInfoGit
