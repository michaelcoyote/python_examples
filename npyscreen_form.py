#!/usr/bin/env python
# A simple npyscreen example more or less from
# the documentation

import npyscreen
import sys


# npyscreen testing.  It's kind of a mess
# https://npyscreen.readthedocs.io/

class testInput(npyscreen.ActionForm):
    """Looks like we extend the ActionForm class.

    The action form class gives us on_ok and on_cancel"""
    def activate(self):
        self.edit()
        # This sets the NEXT_ACTIVE_FORM attribute which tells the app class
        # where to go next
        self.parentApp.setNextForm('Display')

    def create(self):
        self.name = self.add(npyscreen.TitleText, name='name')
        self.dept = self.add(npyscreen.TitleSelectOne,
                             scroll_exit=True,
                             max_height=3,
                             name='department',
                             values=['dept 1',
                                     'dept 2',
                                     'dept 3'])
        self.date = self.add(npyscreen.TitleDateCombo,
                             name='date')

    def on_ok(self):
        """Pass on the values to the next form."""
        display = self.parentApp.getForm('Display')
        display.name.value = self.name.value
        display.dept.value = self.dept.value
        display.date.value = self.date.value
        self.parentApp.switchForm('Display')

    def on_cancel(self):
        self.editing = True
        self.parentApp.setNextForm()


class testOutput(npyscreen.ActionForm):
    def activate(self):
        self.edit()

    def create(self):
        self.name = self.add(npyscreen.TitleFixedText, name='name')
        self.dept = self.add(npyscreen.TitleFixedText, name='department')
        self.date = self.add(npyscreen.TitleFixedText, name='date')

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        sys.exit()

    def on_ok(self):
        # Print doesn't seem to work here.
        print('name: {}\ndepartment: {}\ndqate: {}\n'.format(
            self.name.value,
            self.dept.value,
            self.date.value)
              )
        # the exit_application function doesn't do much but sys.exit does
        # self.exit_application
        sys.exit(0)

    def on_cancel(self):
        """Take us back to the previous form."""
        self.parentApp.switchFormPrevious()


class MyApp(npyscreen.NPSAppManaged):
    """Now we make the forms an app."""
    def onStart(self):
        # Set a theme
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        # add main and display forms
        self.addForm('MAIN',
                     testInput,
                     name='enter new person info here')
        self.addForm('Display',
                     testOutput,
                     name='display the person\'s info')
        # insert more forms here


def main():
    testapp = MyApp()
    testapp.run()


if __name__ == '__main__':
    main()
