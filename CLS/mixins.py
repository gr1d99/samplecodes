class UserDetailsMixin(object):
    fname = None

    def get_first_name(self):
        first_name = super(UserDetailsMixin, self).get_first_name()
        if self.fname is None:
            raise Warning('Name not provided')
        first_name = self.fname
        return first_name


class MultipleUserMixin(object):
    name = ['fname', 'lname', 'mname']

    def get_names(self, **kwargs):
        name = super(MultipleUserMixin, self).get_name(**kwargs)
        name = self.name
        return name