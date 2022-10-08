from aiohttp import web
from app.api import handles
from app.context import AppContext


# Нужно для того чтобы сразу принимать и запрос и контекст
def wrap_handler(handler, context):
    async def wrapper(request):
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
    app.router.add_post(
        '/get_employee_achievements',
        wrap_handler(
            handles.get_employee_achievements,
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
        '/get_employee_role/{data}',
        wrap_handler(
            handles.get_employee_role,
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
        '/get_all_rating',
        wrap_handler(
            handles.get_all_rating,
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
    """
    app.router.add_post(
        '/imports',
        wrap_handler(
            handles.import_handle,
            ctx,
        ),
    )
    app.router.add_delete(
        r'/delete/{data}',
        wrap_handler(
            handles.delete_handle,
            ctx,
        ),
    )
    app.router.add_get(
        r'/nodes/{data}',
        wrap_handler(
            handles.get_nodes_handle,
            ctx,
        ),
    )
    app.router.add_get(
        r'/updates',
        wrap_handler(
            handles.get_updates_handle,
            ctx,
        ),
    )
    app.router.add_get(
        r'/node/{id}/history',
        wrap_handler(
            handles.get_node_history_handle,
            ctx,
        ),
    )
    """