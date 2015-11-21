from remindr.entities import Item, User


users = dict()


class UserRepository(object):
    def read_one(uuid):
        return users.get(uuid)

    def read_many():
        return users.values()

    def write(user):
        users[str(user.uuid)] = user


class ItemRepository(object):
    def write(user, item):
        user.items.append(item)
