#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.html')
output_from_parsed_template = template.render(my_string="Wheeeee!",
                                              my_list=[0, 1, 2, 3, 4, 5])
print(output_from_parsed_template)

# to save the results
# with open("my_rendered_file.html", "wb") as fh:
#    fh.write(output_from_parsed_template)
