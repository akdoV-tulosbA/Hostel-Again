from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=False,signature=False)

auth.settings.extra_fields['auth_user']= [
  Field('address'),
  Field('city'),
  Field('zip'),
  Field('phone')]

db.define_table('newspaper',
                Field('choice_of_newspaper', requires=IS_IN_SET(['The Times of India', 'The Hindu'])),
                Field('subscription_type', requires=IS_IN_SET(['Yearly', 'Monthly'])),
                Field('subscriber', 'reference auth_user', writable=False))


auth.define_tables(username=True)
