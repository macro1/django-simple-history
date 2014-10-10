class NonRelTestRouter(object):

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'nonrel':
            return 'non_rel'
    db_for_read = db_for_write

    def allow_syncdb(self, db, model):
        if model._meta.app_label == 'nonrel':
            return 'non_rel' == db
        return 'default' == db
