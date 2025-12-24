#!/usr/bin/python3
from markdownify import markdownify as md
import os

f0 = open(os.getcwd() + "/CS3780Fall2023.html", "r")
f1 = open(os.getcwd() + "/README.md", "w")
text = md(f0.read())
f1.write(text)
print(text)
f0.close()
f1.close() # <-
