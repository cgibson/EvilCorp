#!/usr/bin/python
from project.util import grammary

lang = grammary.Language("../static/lang/eviltitlelang.json")
print lang.build()
