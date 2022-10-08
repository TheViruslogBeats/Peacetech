from aiohttp import web

from app.context import AppContext
import app.api.validation_check as check
from app import database as dbo
from blockchain_api import blockchain_api


async def post_request_content(request: web.Request):
    text = await request.json()
    return text


async def authentication_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = await post_request_content(request)
        login = data['login']
        password = data['password']
        if await dbo.authentication(context, login, password):
            return web.json_response(
                {
                    "code": 200,
                    "message": "Authentication was successful"
                },
                status=200
            )
        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_employee_achievements(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        login = data['login']
        if dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_achievements(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def create_wallet(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        login = data['login']
        if dbo.employee_in_database(context, login):

            wallet = await blockchain_api.gen_wallet()

            return web.json_response(
                {
                    'privateKey': wallet[0],
                    'publicKey': wallet[1]
                },
                status=200
            )

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_employee_role(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        login = data['login']
        if dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_achievements(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_wallet(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        login = data['login']
        if dbo.employee_in_database(context, login):

            return web.json_response(
                {
                    # TODO: А ПОКА НАМ НЕЧЕГО ВЕРНУТЬ
                },
                status=200
            )

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_all_rating(request: web.Request, context: AppContext) -> web.Response:
    try:
        return web.json_response(await dbo.get_all_rating(context))
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_department_rating(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        department = data['department']
        return web.json_response(await dbo.get_department_rating(context, department))
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_personal_rating(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        login = data['login']
        return web.json_response(await dbo.get_personal_rating(context, login))
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_personal_rating_in_department(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        login = data['login']
        department = data['department']
        return web.json_response(await dbo.get_personal_rating_in_department(context, login, department))
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


"""
async def import_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = await post_request_content(request)
        if check.check_json(data):
            if await dbo.import_items(context, data):
                return web.json_response(
                    {
                        "code": 200,
                        "message": "Import was successful"
                    },
                    status=200
                )
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
async def delete_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        date = request.rel_url.query['date']
        if check.check_item_id(data) and check.datetime_valid(date):
            if await dbo.already_in_the_database(context, data):
                if await dbo.delete_element(context, data, date):
                    return web.json_response(
                        {
                            "code": 200,
                            "message": "The data was successfully deleted"
                        },
                        status=200
                    )
            else:
                return web.json_response(
                    {
                        "code": 404,
                        "message": "File not found"
                    },
                    status=404
                )
        else:
            return web.json_response(
                {
                    "code": 400,
                    "message": "Validation Failed"
                },
                status=400
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
async def get_nodes_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = request.match_info['data']
        if check.check_item_id(data):
            if await dbo.already_in_the_database(context, data):
                print('already_in_the_database')
                return web.json_response(
                    await dbo.get_nodes(context, data)
                )
            else:
                return web.json_response(
                    {
                        "code": 404,
                        "message": "File not found"
                    },
                    status=404
                )
        else:
            return web.json_response(
                {
                    "code": 400,
                    "message": "Validation Failed"
                },
                status=400
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
async def get_updates_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        date = request.rel_url.query['date']
        if check.datetime_valid(date):
            return web.json_response(await dbo.get_items_updated_in_last_day(context, date))
        else:
            return web.json_response(
                {
                    "code": 400,
                    "message": "Validation Failed"
                },
                status=400
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
async def get_node_history_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        item_id = request.match_info['id']
        date_start = request.rel_url.query['dateStart']
        date_end = request.rel_url.query['dateEnd']
        if check.datetime_valid(date_start) and check.datetime_valid(date_end):
            return web.json_response(await dbo.get_item_history(context, item_id, date_start, date_end))
        else:
            return web.json_response(
                {
                    "code": 400,
                    "message": "Validation Failed"
                },
                status=400
            )
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
"""
