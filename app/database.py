from app.context import AppContext
from datetime import datetime, timedelta
import dateutil.parser


async def authentication(context: AppContext, login, password):
    script = f"select login from employee where login = '{login}' and password = '{password}'"
    if len(await context.db.fetch(script)) > 0:
        return True
    else:
        return False


async def get_employee_info(context: AppContext, login):
    script = f"select name, surname, lastname from employee where login = '{login}'"
    employee = (await context.db.fetch(script))[0]
    return {'name': employee['name'], 'surname': employee['surname'], 'lastname': employee['lastname']}


async def get_public_key(context: AppContext, login):
    script = f"select public_key from employee where login = '{login}'"
    employee = (await context.db.fetch(script))[0]
    return {'public_key': employee['public_key']}


async def get_private_key(context: AppContext, login):
    script = f"select private_key from employee where login = '{login}'"
    employee = (await context.db.fetch(script))[0]
    return {'private_key': employee['private_key']}


async def employee_has_wallet(context: AppContext, login):
    script = f"select private_key, public_key from employee where login = '{login}'"
    if len(await context.db.fetch(script)) > 0:
        return True
    else:
        return False


async def get_employee_achievements(context: AppContext, login):
    achievements = await find_employee_achievements(context, login)
    answer = {}
    if len(achievements) > 0:
        for achieve in achievements:
            answer.update({achieve: await describe_achievements(context, achieve)})
    return answer


async def get_employee_role(context: AppContext, login):
    script = f"select role from employee where login = '{login}'"
    return {'role': (await context.db.fetch(script))[0]['role']}


async def get_all_rating(context: AppContext):
    script = f"""
                 select e.login, sum(a.achieve_points) as score
                 from employee e
                 inner join employee_achievements ea on ea.employee_login = e.login
                 inner join all_achievements a on a.id = ea.achieve_id
                 group by e.login
                 order by sum(a.achieve_points) desc
             """
    rating = await context.db.fetch(script)

    answer = {}
    place = 0
    if len(rating) > 0:
        for employee in rating:
            place += 1
            answer.update({place: {'login': employee['login'], 'score': employee['score']}})

    return answer


async def get_department_rating(context: AppContext, department):
    script = f"""
                 select e.login, sum(a.achieve_points) as score
                 from employee e
                 inner join employee_achievements ea on ea.employee_login = e.login
                 inner join all_achievements a on a.id = ea.achieve_id
                 where e.department = '{department}'
                 group by e.login
                 order by sum(a.achieve_points) desc
             """
    rating = await context.db.fetch(script)
    answer = {}
    place = 0
    if len(rating) > 0:
        for employee in rating:
            place += 1
            answer.update({place: {'login': employee['login'], 'score': employee['score']}})

    return answer


async def get_personal_rating(context: AppContext, login):
    script = f"""
                 select e.login, sum(a.achieve_points) as score
                 from employee e
                 inner join employee_achievements ea on ea.employee_login = e.login
                 inner join all_achievements a on a.id = ea.achieve_id
                 group by e.login
                 order by sum(a.achieve_points) desc
             """

    rating = await context.db.fetch(script)
    answer = {}
    place = 0
    if len(rating) > 0:
        for employee in rating:
            place += 1
            if login == employee['login']:
                return {'place': place, 'score': employee['score']}

    return answer


async def get_personal_rating_in_department(context: AppContext, login, department):
    script = f"""
                 select e.login, sum(a.achieve_points) as score
                 from employee e
                 inner join employee_achievements ea on ea.employee_login = e.login
                 inner join all_achievements a on a.id = ea.achieve_id
                 where e.department = '{department}'
                 group by e.login
                 order by sum(a.achieve_points)
             """
    rating = (await context.db.fetch(script))[0]

    answer = {}
    place = 0
    if len(rating) > 0:
        for employee in rating:
            place += 1
            if login == employee['login']:
                return {'place': place}

    return answer


async def create_wallet(context: AppContext, login, private_key, public_key):
    script = f"update employee set public_key= '{public_key}', private_key = '{private_key}' where login = '{login}'"
    await context.db.fetch(script)


async def get_wallet(context: AppContext, login):
    script = f"select public_key, private_key from employee where login = '{login}'"
    data = await context.db.fetch(script)
    wallet = data[0] if len(data) > 0 else []
    return {'publicKey': wallet[0], 'privateKey': wallet[1]}


async def get_employee_tasks(context: AppContext, login):
    script = f"""select id, description, award, administrator_login, progress from task 
                 where employee_login = '{login}'"""
    tasks = await context.db.fetch(script)
    answer = {}
    if len(tasks) > 0:
        for task in tasks:
            answer.update(
                {
                    task['id']: {
                        'description': task['description'],
                        'award': task['award'],
                        'administrator_login': task['administrator_login'],
                        'progress': task['progress']
                    }
                }
            )
    return answer


async def get_count_of_employee_tasks(context: AppContext, login):
    script = f"""select count(id) from task 
                 where employee_login = '{login}'
                 group by employee_login"""
    count = await context.db.fetch(script)
    return {'count': count if len(count) > 0 else 0}


async def find_employee_achievements(context: AppContext, login):
    script = f"select achieve_id from employee_achievements where employee_login = '{login['login']}'"
    achievements = await context.db.fetch(script)
    achievements_array = []
    if len(achievements) > 0:
        for achieve in achievements:
            achievements_array.append(achieve[0]['achieve_id'])
    return achievements_array


async def employee_in_database(context: AppContext, login):
    script = f"select login from employee where login = '{login}'"
    if len(await context.db.fetch(script)) > 0:
        return True
    else:
        return False


async def describe_achievements(context: AppContext, achieve):
    script = f"select name, description, achieve_points from all_achievements where id = '{achieve}'"
    data = await context.db.fetch(script)
    return {'name': data[0]['name'], 'description': data[0]['description'], 'achieve_points': data['achieve_points']}
