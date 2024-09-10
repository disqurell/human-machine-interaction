from fastapi import APIRouter, Depends, Request, HTTPException, Query
from fastapi.responses import ORJSONResponse

from bl.security.apikey import api_key
from bl.goods import GoodsDomain
from bl.categories import CategoriesDomain

from models.http.good import UpdateBxIdMaster

router = APIRouter(
    prefix="/goods",
    tags=["goods"],
)


@router.get(
    "/props",
    dependencies=[Depends(api_key)],
)
async def get_paginated_props(
    request: Request,
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Max number of items to return"),
):
    """
    Get paginated props
    """
    props = await GoodsDomain().get_paginated_props(skip=skip, limit=limit)

    if not props:
        return ORJSONResponse(
            {
                "message": "props not found",
            },
            status_code=404,
        )

    return ORJSONResponse(
        {
            "props": props,
        },
        status_code=200,
    )


@router.get(
    "/master",
    dependencies=[Depends(api_key)],
)
async def get_paginated_goods(
    request: Request,
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Max number of items to return"),
):
    """
    Get paginated goods with specific fields and process them.
    """
    goods = await GoodsDomain().get_paginated_goods(skip=skip, limit=limit)

    if not goods:
        return ORJSONResponse(
            {
                "message": "Goods not found",
            },
            status_code=404,
        )

    return ORJSONResponse(
        {
            "goods": goods,
        },
        status_code=200,
    )


@router.get(
    "/master/new",
    dependencies=[Depends(api_key)],
)
async def get_paginated_goods_without_bxid(
    request: Request,
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Max number of items to return"),
):
    """
    Get paginated goods without bxid
    """
    goods = await GoodsDomain().get_paginated_goods_without_bxid(skip=skip, limit=limit)

    if not goods:
        return ORJSONResponse(
            {
                "message": "Goods not found",
            },
            status_code=404,
        )

    return ORJSONResponse(
        {
            "goods": goods,
        },
        status_code=200,
    )


@router.get(
    "/categories",
    dependencies=[Depends(api_key)],
)
async def get_categories(request: Request):
    """
    Get all categories
    """
    categories = await CategoriesDomain().get_all_local_categories()

    if not categories:
        return ORJSONResponse(
            {
                "message": "Categories not found",
            },
            status_code=404,
        )

    return ORJSONResponse(
        {
            "categories": categories,
        },
        status_code=200,
    )


@router.get(
    "/prices",
    dependencies=[Depends(api_key)],
)
async def get_prices(
    request: Request,
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Max number of items to return"),
):
    """
    Get prices
    """
    prices = await GoodsDomain().get_prices_with_pagination(skip=skip, limit=limit)

    if not prices:
        return ORJSONResponse(
            {
                "message": "prices not found",
            },
            status_code=404,
        )

    return ORJSONResponse(
        {
            "prices": prices,
        },
        status_code=200,
    )


@router.get(
    "/wg/slaves",
    dependencies=[Depends(api_key)],
)
async def get_wg_slaves(
    request: Request,
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, description="Max number of items to return"),
):
    """
    Get wg slaves
    """
    items = await GoodsDomain().get_wg_slaves(skip=skip, limit=limit)

    if not items:
        return ORJSONResponse(
            {
                "message": "items not found",
            },
            status_code=404,
        )

    return ORJSONResponse(
        {
            "items": items,
        },
        status_code=200,
    )


@router.patch(
    "/master/bxid",
    dependencies=[Depends(api_key)],
)
async def update_bx_id(request: Request, bxids: UpdateBxIdMaster):
    """
    Update bxid
    """
    result = await GoodsDomain().update_bxid(bxids=bxids)

    if not result:
        return ORJSONResponse(
            {
                "message": "Server error during updating bxids",
            },
            status_code=500,
        )

    if result.get("status") == "Some updated":
        return ORJSONResponse(
            {
                "status": result.get("status"),
                "not_updated_items": result.get("not_updated"),
            },
            status_code=200,
        )

    return ORJSONResponse(
        {
            "status": "successfully updated all bxids",
        },
        status_code=200,
    )
