#!/usr/bin/python
# -*- coding: utf-8 -*-

from ujson import loads
from tornado.gen import coroutine

from holmes.models import Delimiter, User
from holmes.handlers import BaseHandler


class LimiterHandler(BaseHandler):
    @coroutine
    def get(self):
        limiters = Delimiter.get_all(self.db)

        result = []

        for limit in limiters:
            current_value = yield self.cache.get_limit_usage('limit-for-%s' % limit.url)

            result.append({
                'id': limit.id,
                'url': limit.url,
                'currentValue': current_value or 0
            })

        self.write_json(result)

    @coroutine
    def post(self):
        access_token = self.request.headers.get('X-AUTH-HOLMES', None)

        if access_token is None:
            self.set_status(403)
            self.write_json({'reason': 'Empty access token'})
            return

        result = yield User.authenticate(
            access_token,
            self.application.http_client.fetch,
            self.db,
            self.application.config
        )

        if result and result.get('user', None) is None:
            self.set_status(403)
            self.write_json({'reason': 'Not authorized user.'})
            return

        post_data = loads(self.request.body)
        url = post_data.get('url', None)
        value = post_data.get('value', None)

        if not url and not value:
            self.set_status(400)
            self.write_json({'reason': 'Not url or value'})
            return

        result = Delimiter.add_or_update_delimiter(self.db, url, value)

        self.write_json(result)
