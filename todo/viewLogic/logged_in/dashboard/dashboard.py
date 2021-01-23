# display username and to-do list
from flask.globals import session
from flask.templating import render_template
from .main_list import add_itemForm
from .list_options import Add_ListForm, Chooselist_dropdown
from ....db.helpers.userDbHelper import getUser_byUsername_asDict
from ....db.helpers.listDbHelper import get_list_by_id, get_users_lists_as_list_tuples
from ....db.helpers.tasksDbHelper import get_list_tasks

def dashboard_request_handler(request):
    username = request.args.get("username")
    if request.method == 'GET':
        return render_dashboard(username)

def render_dashboard(username):
    main_list_title, main_list_tasks = prepare_dashboard_user_info(username)
    chooselist_dropdown = Chooselist_dropdown()
    chooselist_dropdown.list_choice.choices = get_users_lists_as_list_tuples(session['user']['id'])
    return render_template(
        'logged_in/main_dashboard.html',
        main_list=main_list_title,
        main_list_tasks=main_list_tasks,
        username=username,
        Add_ListForm=Add_ListForm(),
        chooselist_dropdown=chooselist_dropdown,
        add_itemForm=add_itemForm()
    )

def prepare_dashboard_user_info(username):
    session['user'] = getUser_byUsername_asDict(username)
    main_list_id = session['user']['main_list_id']
    print(main_list_id)
    main_list_tasks = get_list_tasks(main_list_id)
    main_list = get_list_by_id(main_list_id)
    return main_list, main_list_tasks