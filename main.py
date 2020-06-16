import firebase_admin
from firebase_admin import auth
import click


@click.group()
def main():
    pass

def print_style(text, fg='white', bg='black', blink=False, bold=False):
    return click.echo(click.style((f'{text}'), fg=fg, bg=bg, blink=blink, bold=bold))

@main.command()
def users():
    """ to get all users"""
    page = auth.list_users()
    for user in page.users:
        user_email = user.email if hasattr(user, 'email') else None
        user_displayName = user.displayName if hasattr(user, 'displayName') else None
        text = f'{user.uid}, - , {user_email} - {user_displayName}'
        print_style(text)

@main.command()
@click.option('--uid', prompt='userId' ,help='firebase userid')
def user(uid):
    """get single user based on uid"""
    print('uid received: %s' % (uid))
    user = auth.get_user(uid)
    
    print('user: {0}'.format(user.__dict__))
    for k,v in user.__dict__['_data'].items():
        text = f'{k} -  {v}'
        print_style(text)

@main.command()
@click.option('--id', prompt="select a function to execute", type=click.IntRange(1,2))
def menu(id):
    """temporary menu to start the app"""
    if id == 1:
        return users()
    elif id == 2:
        return user()
    else:
        return 'unknown option'


# user(sys.argv[1])
if __name__ == '__main__':
    # initialize firebase connection
    default_app = firebase_admin.initialize_app()
    funcs = ['users', 'user']
    y = 0
    for x in funcs:
        y += 1
        text = f'[{y}] -  {x}'
        print_style(text, fg='cyan')
    menu()