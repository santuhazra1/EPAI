import common.validators as validators
import common.models as models
import common.models

validators.is_json('{}')
validators.is_numeric(10)
validators.is_date('123')
validators.boolean.is_boolean('true')


# for k in validators.__dict__.keys():
#     print(k)


print('\n**** models ****\n')

for k in models.__dict__.keys():
    print(k)

new_post = common.models.posts.Post()
new_user = common.models.users.User()
