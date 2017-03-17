"""
Usage:
    inv_app add_item         
    inv_app remove_item 
    inv_app list_items
    inv_app checkout 
    inv_app checkin 
    inv_app item_log 
    inv_app search
    inv_app total_assets 
    inv_app value_by_category
    inv_app item_value
    inv_app list_items [--export=<filename>]
    inv_app quit
    inv_app (-i | --interactive)
    inv_app (-h | --help)
    
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit. 
    --export=<filename>  Export filename
"""

import sys, os
import cmd
from docopt import docopt, DocoptExit
from invapp import add_item, remove_item, item_list, checkout, checkin, item_log,item_value, search,value_by_category,total_assets
from invapp import display_title_bar


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn




class Inventory(cmd.Cmd):
    intro = display_title_bar()
    prompt = 'IMS>>>'
    file = None

    @docopt_cmd
    def do_add_item(self, arg):
        """Usage: add_item"""
        add_item()
    
    @docopt_cmd
    def do_remove_item(self, arg):
        """Usage: remove_item """
        remove_item()
        
    @docopt_cmd
    def do_checkout(self, arg):
       """"Usage: checkout """
       checkout()

    @docopt_cmd
    def do_checkin(self, arg):
       """Usage:checkin """
       checkin()

    @docopt_cmd
    def do_item_log(self, arg):
       """Usage: item_log """
       item_log()

    @docopt_cmd
    def do_search(self, arg):
       """Usage: search """
       search()
             
    @docopt_cmd
    def do_total_assets(self,arg):
        """Usage: total_assets"""
        total_assets()

    @docopt_cmd
    def do_value_by_category(self,arg):
        """Usage: item_value_category"""
        value_by_category()

    @docopt_cmd
    def do_item_value(self,arg):
        """Usage: item_value"""
        item_value()   
        
    @docopt_cmd
    def do_list_items(self, arg):
        """Usage: list_items [--export=<filename>]"""
        item_list()

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        Inventory().cmdloop()
    except KeyboardInterrupt:
        print("Exiting App")
