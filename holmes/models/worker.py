#!/usr/bin/python
# -*- coding: utf-8 -*-


from motorengine import Document, UUIDField, DateTimeField, ReferenceField


class Worker(Document):
    __lazy__ = False

    uuid = UUIDField(required=True)
    last_ping = DateTimeField(auto_now_on_update=True)
    current_review = ReferenceField(reference_document_type='holmes.models.review.Review')

    def __str__(self):
        return "Worker %s" % str(self.uuid)

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "uuid": str(self.uuid),
            "last_ping": str(self.last_ping),
            "current_review": self.current_review and str(self.current_review.uuid) or None
        }
