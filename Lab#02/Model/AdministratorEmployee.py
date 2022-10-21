#!/usr/bin/python
#-*- coding: utf-8 -*-

from Employee import Employee

class AdministratorEmployee(Employee):
    def __init__(self):
        self.name = None
        self.dob = None
        self.empNo = None
        self.major = None

    def getName(self, empNo):
        pass

