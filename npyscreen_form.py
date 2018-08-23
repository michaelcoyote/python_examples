#!/usr/bin/env python
# A simple npyscreen example more or less from
# the documentation

import npyscreen


class myTestForm(npyscreen.Form):
    """Looks like we extend the Form class."""
    def post_edit(self):
        self.parentASpp.setNextForm(None)

    def create(self):
        self.my_name = self.add(npyscreen.TitleText, name='Name')
        self.my_dept = self.add(npyscreen.TitleSelectOne,
                                scroll_exit=True,
                                max_height=3,
                                name='Department',
                                values=['Department 1',
                                        'Department 2',
                                        'Department 3'])
        self.my_date = self.add(npyscreen.TitleDateCombo,
                                name='Date Employed')

    def on_ok(self):
        print ('name: {}\ndepartment: {}\ndqate: {}\n'.format(
                   self.my_name.value,
                   self.my_dept.value,
                   self.my_date.value)
               )


class MyApp(npyscreen.NPSAppManaged):
    """Now we make the forms an app."""
    def onStart(self):
        self.addForm('MAIN',
                     myTestForm,
                     name='new person')
        # insert more forms here


def main():
    testapp = MyApp()
    testapp.run()


if __name__ == '__main__':
    main()
