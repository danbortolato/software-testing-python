MENU_PROMPT = 'Enter a option: "C" to create a blog, "L" to list blogs, "R" to read one, "P" to create a post or "Q" to quit.'
blogs = dict()

def menu():

    print_blogs()
    selection = input(MENU_PROMPT)

def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
