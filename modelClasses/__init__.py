from extensions import db, bcrypt, login_manager

@login_manager.user_loader
def load_user(user_id):
    from modelClasses.User import User
    return User.query.get(int(user_id))