#!/usr/bin/python
from project.util import grammary

lang = grammary.Language("../static/lang/evillang.json")
print lang.build()
