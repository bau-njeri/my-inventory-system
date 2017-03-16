"""
Usage:
    inv_app add_item <iid> <name> <description> <total_amt> <cost> <dateadd> <status>
    inv_app remove_item <item_iid>
    inv_app List <item_list>
    inv_app List <--export ><filename>
    inv_app itemlist <filename>
    inv_app checkout <item_iid>
    inv_app checkin <item_iid>
    inv_app view <iid>
    inv_app search <iid>..
    
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import sys
import cmd
from docopt import docopt, DocoptExit

from inventory_project import add_item, remove_item, item_list, checkout, checkin, item_view, search 



 
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def  display_title_bar ():

    os.system("cls")
    print("\t**********************************************")  
    print("\t---------        Welcome To        -----------")
    print("\t---     Inventory management system        ---")
    print("\t**********************************************") 


class get_user_choice(cmd.Cmd):
    prompt = "What would you like to do? "

    @docopt_cmd
    def do_add_item(self, arg):
        """Usage: add_item <iid,name> <description> <total_amt> <cost> <dateadd> <status>"""
        ID= arg['<iid>']
        name= arg['<name>']
        description= arg['<description>']
        total_amt=arg['<total_amt']
        cost=arg['<cost']
        status= arg['<status']
        add_item(ID, name, description, total_amt, cost, status)
        
        


    @docopt_cmd
    def do_remove_item(self, arg):
        """Usage: remove_item <item_iid>"""
        item_iid=arg['<item_iid>']
        print (item_iid)

    @docopt_cmd
    def do_list(self, arg):
       """Usage:List<filename>"""
       file_name = arg['<filename>']
       print (file_name)
       
    @docopt_cmd
    def do_checkout(self, arg):
       """"Usage:List <item_list>"""
       status=arg['<item_iid>']
       print (status)
    @docopt_cmd
    def do_checkin(self, arg):
       """Usage:checkin <item_iid>"""
       status=arg['<i>']
       print (item_list)
    @docopt_cmd
    def do_view(self, arg):
       """Usage: view <iid>"""
       view_item=arg['<iid>']
       print (view_item)
    @docopt_cmd
    def do_search(self, arg):
       """Usage: search <iid>"""
       search=arg['<iid>']
       print (search)     
       def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)
 