from blog import Blog
from post import Post

MENU_PROMPT = 'Enter a option: "C" to create a blog, "L" to list blogs, "R" to read one, "P" to create a post or "Q" to quit.'
POST_TEMPLATE = '''
--- {} ---

{}

'''


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
            ask_read_blog()
        elif selection == 'P':
            ask_create_post()
        selection = input(MENU_PROMPT)
def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))

def ask_create_blog():
    title = input ('Enter your blog title: ')
    author = input('Enter your name: ')

    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the blog title to read: ')

    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    blog_name = input('Enter the blog title to write a post: ')
    title = input('Enter post title: ')
    content = input('Enter post content: ')

    blogs[blog_name].create_post(title, content)

