from aiohttp import web

from app.context import AppContext
import app.api.validation_check as check
from app import database as dbo
from blockchain_api import blockchain_api


async def post_request_content(request: web.Request):
    try:
        text = await request.json()
        return text
    except:
        return None


async def authentication_handle(request: web.Request, context: AppContext) -> web.Response:
    try:
        data = await post_request_content(request)
        if data is None:
            raise KeyError
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
    except KeyError:
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
        if data is None:
            raise KeyError
        login = data['login']
        if await dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_achievements(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def transfer_ruble(request: web.Request, context: AppContext) -> web.Response:
    try:
        from_login = request.match_info['from_login']
        to_login = request.match_info['to_login']
        amount = request.match_info['amount']
        if from_login is None or to_login is None or amount is None:
            raise KeyError
        if await dbo.employee_in_database(context, from_login) and await dbo.employee_in_database(context, to_login):
            if await dbo.employee_has_wallet(context, from_login) and await dbo.employee_has_wallet(context, to_login):
                from_private_key = await dbo.get_private_key(context, from_login)
                to_public_key = await dbo.get_public_key(context, to_login)
                blockchain_api.transfer_ruble(from_private_key, to_public_key, amount)
                return web.json_response(
                    {
                        "code": 200,
                        "message": "Transaction was successful"
                    },
                    status=200
                )
            return web.json_response(
                {
                    "code": 400,
                    "message": "Employee hasn't wallet"
                },
                status=400
            )
        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def transfer_nft(request: web.Request, context: AppContext) -> web.Response:
    try:
        from_login = request.match_info['from_login']
        to_login = request.match_info['to_login']
        token_id = request.match_info['token_id']
        if from_login is None or to_login is None or token_id is None:
            raise KeyError
        if await dbo.employee_in_database(context, from_login) and await dbo.employee_in_database(context, to_login):
            if await dbo.employee_has_wallet(context, from_login) and await dbo.employee_has_wallet(context, to_login):
                from_private_key = await dbo.get_private_key(context, from_login)
                to_public_key = await dbo.get_public_key(context, to_login)
                blockchain_api.transfer_nft(from_private_key, to_public_key, token_id)
                return web.json_response(
                    {
                        "code": 200,
                        "message": "Transaction was successful"
                    },
                    status=200
                )
            return web.json_response(
                {
                    "code": 400,
                    "message": "Employee hasn't wallet"
                },
                status=400
            )
        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def employee_info(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if login is None:
            raise KeyError
        if await dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_info(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_tasks(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if login is None:
            raise KeyError
        if await dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_tasks(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_count_of_tasks(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if login is None:
            raise KeyError
        if await dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_count_of_employee_tasks(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def create_wallet(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']

        if await dbo.employee_in_database(context, login):

            wallet = await blockchain_api.gen_wallet()

            private_key = wallet[0]
            public_key = wallet[1]
            await dbo.create_wallet(context, login, private_key, public_key)
            return web.json_response(
                {
                    'privateKey': private_key,
                    'publicKey': public_key
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
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_wallet(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if await dbo.employee_in_database(context, login):
            return web.json_response(
                await dbo.get_wallet(context, login),
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
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_wallet_balance(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if await dbo.employee_in_database(context, login):
            public_key = await dbo.get_public_key(context, login)
            return web.json_response(
                blockchain_api.get_wallet_balance(public_key['public_key']),
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
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_wallet_history(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if await dbo.employee_in_database(context, login):
            public_key = await dbo.get_public_key(context, login)
            return web.json_response(
                blockchain_api.get_wallet_history(public_key['public_key']),
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
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_wallet_nft_balance(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if await dbo.employee_in_database(context, login):
            public_key = await dbo.get_public_key(context, login)
            wallet_nft_balance = blockchain_api.get_wallet_nft_balance(public_key.get('public_key', None))
            return web.json_response(
                wallet_nft_balance,
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
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_employee_role(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if await dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_role(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_employee_status(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        if await dbo.employee_in_database(context, login):

            return web.json_response(await dbo.get_employee_status(context, login), status=200)

        else:
            return web.json_response(
                {
                    "code": 404,
                    "message": "Employee not found"
                },
                status=404
            )
    except KeyError:
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

async def get_shop(request: web.Request, context: AppContext) -> web.Response:
    try:
        return web.json_response(await dbo.get_shop(context))
    except SyntaxError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
async def get_greenhouse(request: web.Request, context: AppContext) -> web.Response:
    try:
        return web.json_response(await dbo.get_greenhouse(context))
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
        department = request.match_info['data']
        return web.json_response(await dbo.get_department_rating(context, department))
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


async def get_personal_rating(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.match_info['data']
        return web.json_response(await dbo.get_personal_rating(context, login))
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )


# TODO: Протестить, по-моему там не читается вход
async def get_personal_rating_in_department(request: web.Request, context: AppContext) -> web.Response:
    try:
        login = request.rel_url.query['login']
        department = request.rel_url.query['department']
        return web.json_response(await dbo.get_personal_rating_in_department(context, login, department))
    except KeyError:
        return web.json_response(
            {
                "code": 400,
                "message": "Validation Failed"
            },
            status=400
        )
