#!/usr/bin/env python
"""Jinja conf file generator POC."""

import json
from jinja2 import Environment, FileSystemLoader

FILENAME = "../../resume/resume.json"


def render_resume(resume_file, resume_data):
    """Read the template and render config."""
    # set up the template dir and set trim_block to remove extra whitespace
    j_env = Environment(
            loader=FileSystemLoader('./templates/'),
            trim_blocks=True)
    j_env.filters['is_list'] = is_list
    j_env.filters['make_title'] = make_title
    template = j_env.get_template(resume_file + '.j2')
    return template.render(resume_data=resume_data)


def is_list(value):
    return isinstance(value, list)


def make_title(value):
    return value.replace('_', ' ').title()


def load_resume(filename=FILENAME):
    with open(filename, 'r') as f:
        resume_dict = json.load(f)
    # print resume_dict
    return resume_dict


def main():

    resume_data = load_resume()
    rendered_t = render_resume(resume_file='resume.md',
                               resume_data=resume_data)
    print(rendered_t)


if __name__ == "__main__":
    main()
