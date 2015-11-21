import json, logging
from datetime import datetime
from uuid import uuid4

from tornado.escape import json_decode
from tornado.web import RequestHandler

from remindr.entities import Item, User
from remindr.repositories import ItemRepository, UserRepository


logger = logging.getLogger("main")


class MainHandler(RequestHandler):
    def get(self):
        self.write("Helloz, world")


class UsersHandler(RequestHandler):
    def get(self):
        self.write({
            'users': [u.to_primitive() for u in UserRepository.read_many()]
        })

    def post(self):
        user = User({
            'uuid': uuid4()
        })
        UserRepository.write(user)
        self.write({'user': user.to_primitive()})


class UserHandler(RequestHandler):
    def get(self, uuid):
        self.write({
            'user': UserRepository.read_one(uuid).to_primitive()
        })

class ItemHandler(RequestHandler):
    def post(self):
        params = json_decode(self.request.body)
        lat = params.get('lat')
        lng = params.get('lng')
        name = params.get('name')
        created_at = params.get('created_at', datetime.utcnow())
        user_uuid = params.get('user_uuid')

        user = UserRepository.read_one(user_uuid)
        item = Item({
            'uuid': uuid4(),
            'name': name,
            'location': [lat, lng],
            'created_at': created_at
        })

        ItemRepository.write(user, item)
        self.write({
            'item': item.to_primitive()
        })
