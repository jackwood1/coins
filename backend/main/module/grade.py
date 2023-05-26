from marshmallow import Schema, fields


class Grade(object):
    def __init__(self, grade):
        self.grade = grade

    def __repr__(self):
        return '<Grade(name={self.grade!r})>'.format(self=self)


class GradeSchema(Schema):
    description = fields.Str()
    amount = fields.Number()
    created_at = fields.Date()
    type = fields.Str()