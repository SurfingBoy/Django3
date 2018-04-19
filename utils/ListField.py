# -*- coding:utf-8 -*-
from django.db import models
import ast

class ListField(models.TextField):
    # __metaclass__=models.SubfieldBase
    description='Stores a python list'

    def __init__(self,*arg,**kwargs):
        super(ListField, self).__init__(*arg,**kwargs)
    def to_python(self, value):
        if not value:
            value=[]
        if isinstance(value,list):
            return value
        return ast.literal_eval(value)
    def get_prep_value(self, value):
        if value is None:
            return value
        return str(value)
    def value_to_string(self, obj):
        value=self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)