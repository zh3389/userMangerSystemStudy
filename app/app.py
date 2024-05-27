from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, HTTPException

from app.db import User, create_db_and_tables
from app.schemas import UserCreate, UserRead, UserUpdate
from app.users import auth_backend, current_active_user, fastapi_users
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    一个上下文管理器，用于处理FastAPI应用程序的使用寿命。
    它创建了必要的数据库和表。
    参数：
        - app: FastAPI - 要使用的FastAPI实例。
    """
    # 如果您设置了像Alembic这样的迁移系统，则不需要
    await create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
# 配置 CORS
origins = [
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
返回给定身份验证后端的身份验证路由器。
：param backend:身份验证后端实例。
是否需要验证用户。默认为False。
"""
app.include_router(fastapi_users.get_auth_router(auth_backend),
                   prefix="/auth/jwt",
                   tags=["auth"])

"""
返回一个带有注册路由的路由器。
：param UserRead：公共用户的Pydantic架构。
：param UserCreate：用于创建用户的Pydantic架构。
"""
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
                   prefix="/auth",
                   tags=["auth"],
                   )

"""
返回重置密码过程路由器。
"""
app.include_router(fastapi_users.get_reset_password_router(),
                   prefix="/auth",
                   tags=["auth"],
                   )

"""
返回一个带有电子邮件验证路由的路由器。
：param UserRead：公共用户的Pydantic架构。
"""
app.include_router(fastapi_users.get_verify_router(UserRead),
                   prefix="/auth",
                   tags=["auth"],
                   )

"""
返回一个带有路由的路由器来管理用户。
：param UserRead：公共用户的Pydantic架构。
：param UserUpdate：用于更新用户的Pydantic架构。
"""
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate),
                   prefix="/users",
                   tags=["users"],
                   )


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    """
    一种处理对经过身份验证的路由的请求的函数。

    参数：
    - user: user，从当前活动的用户依赖关系中获取的用户对象。

    返回：
    - dict：包含用户电子邮件信息的词典。
    """
    return {"message": f"Hello {user.email}!"}

