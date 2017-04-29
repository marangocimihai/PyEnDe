#!/usr/bin/python
# -*- coding: utf-8 -*-

class Entity():
    def __init__(self, name, content, is_encrypted):
        self.name = name
        self.content = content
        self.is_encrypted = is_encrypted

    def get_title(self):
        return self.name

    def get_content(self):
        return self.content

    def set_title(self, name):
        self.name = name

    def set_content(self, content):
        self.content = content

    def get_is_encrypted(self):
        return self.is_encrypted

    def set_is_encrypted(self, is_encrypted):
        self.is_encrypted = is_encrypted