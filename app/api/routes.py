from aiohttp import web
from app.api import handles
from app.context import AppContext
import aiohttp_cors


# Нужно для того чтобы сразу принимать и запрос и контекст
def wrap_handler(handler, context):
    async def wrapper(request):
        print(request)
        return await handler(request, context)

    return wrapper


def setup_routes(app: web.Application, ctx: AppContext) -> None:
    app.router.add_post(
        '/authentication',
        wrap_handler(
            handles.authentication_handle,
            ctx,
        ),
    )
    app.router.add_get(
        '/employee_info/{data}',
        wrap_handler(
            handles.employee_info,
            ctx,
        ),
    )
    app.router.add_post(
        '/transfer_ruble',
        wrap_handler(
            handles.transfer_ruble,
            ctx,
        ),
    )
    app.router.add_post(
        '/transfer_nft',
        wrap_handler(
            handles.transfer_nft,
            ctx,
        ),
    )
    app.router.add_post(
        '/get_employee_achievements',
        wrap_handler(
            handles.get_employee_achievements,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_wallet_nft_balance/{data}',
        wrap_handler(
            handles.get_wallet_nft_balance,
            ctx,
        ),
    )
    app.router.add_get(
        '/create_wallet/{data}',
        wrap_handler(
            handles.create_wallet,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_wallet/{data}',
        wrap_handler(
            handles.get_wallet,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_employee_role/{data}',
        wrap_handler(
            handles.get_employee_role,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_employee_status/{data}',
        wrap_handler(
            handles.get_employee_status,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_all_rating',
        wrap_handler(
            handles.get_all_rating,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_shop',
        wrap_handler(
            handles.get_shop,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_greenhouse',
        wrap_handler(
            handles.get_greenhouse,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_department_rating/{data}',
        wrap_handler(
            handles.get_department_rating,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_personal_rating/{data}',
        wrap_handler(
            handles.get_personal_rating,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_personal_rating_in_department/{data}',
        wrap_handler(
            handles.get_personal_rating_in_department,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_wallet_balance/{data}',
        wrap_handler(
            handles.get_wallet_balance,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_wallet_history/{data}',
        wrap_handler(
            handles.get_wallet_balance,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_tasks/{data}',
        wrap_handler(
            handles.get_tasks,
            ctx,
        ),
    )
    app.router.add_get(
        '/get_count_of_tasks/{data}',
        wrap_handler(
            handles.get_count_of_tasks,
            ctx,
        ),
    )
    # get_wallet_balance
    # Configure default CORS settings.
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
    })

    # Configure CORS on all routes.
    for route in list(app.router.routes()):
        cors.add(route)
