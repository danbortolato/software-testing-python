MENU_PROMPT = 'Enter a option: "C" to create a blog, "L" to list blogs, "R" to read one, "P" to create a post or "Q" to quit.'
blogs = dict()

def menu():

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'Q':
        if selection == 'C':
            ask_create_blog()
        elif selection == 'L':
            print_blogs()
        elif selection == 'R':
            ask_read_blogs()
        elif selection == 'P':
            ask_create_post()
        selection = input(MENU_PROMPT)
def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    pass

def ask_read_blogs():
    pass

def ask_create_post():
    pass
