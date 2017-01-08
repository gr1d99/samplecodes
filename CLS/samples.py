from CLS.mixins import UserDetailsMixin


class User(object):
    first_name = None
    last_name = None

    def get_first_name(self):
        return self.first_name

    def print_user_details(self):
        return self.first_name, self.last_name


class MyUser(UserDetailsMixin, User):
    fname = 'Hacker'
    """
    test objects
    """