#!/usr/bin/env python
"""Jinja conf file generator POC."""

from jinja2 import Environment, FileSystemLoader
# import yaml

# def conf_file(conf_file_path):
#     with open(conf_file_path) as conf_fh
#     return yaml.safe_load(conf_fh)


def config_gen(conf_file, conf_data):
    """Read the template and render config."""
    # set up the template dir and set trim_block to remove extra whitespace
    t_path = Environment(
            loader=FileSystemLoader('./templates/'),
            trim_blocks=True)
    template = t_path.get_template(conf_file + '.j2')
    return template.render(conf_data=conf_data)


def main():
    conf_data = {
            'a_list': [1, 2, 3, 4, 5],
            'b_dict': {
                'one': '#1',
                'two': '#2',
                'three': '#3',
                },
            'c_nested': {
                'header_1': {
                    'sub1a': '1a',
                    'sub1b': '1b',
                    },
                'header_2': {
                    'sub2a': '2a',
                    'sub2b': '2b',
                    'sub2c': '2c',
                    },
                'header_3': {
                    'sub3a': '3a'
                    }
                },
            'd_empty': None,
            }

    # print conf_data
    rendered_t = config_gen(conf_file='test.conf', conf_data=conf_data)
    print(rendered_t)


if __name__ == "__main__":
    main()
