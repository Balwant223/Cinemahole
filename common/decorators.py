from django.contrib.auth.decorators import login_required,user_passes_test
active_imp=user_passes_test(lambda u: u.is_active)
def login_imp(view_func):
    decorated_fun=login_required(active_imp(view_func))
    return decorated_fun