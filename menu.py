from database import Database
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user=input("Enter your author name:")
        self.user_blog=None
        if self._user_has_account():
            print ("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()
        pass

    def _user_has_account(self):
        # should return True or Fslse
        blog=Database.find_one('blogs',{'author':self.user})
        if blog is not None:
        # create an object
            self.user_blog=Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title=input("Enter blog title")
        description=input("Enter your description")
        blog=Blog(author=self.user,
                  title=title,
                  description=description)
        blog.save_to_mongo()
        self.user_blog=blog




        # ask user for author name
        # check if they've already got an account
        # if not, prompt them to create one

    def run_menu(self):
        read_or_write=input("Do you want to read(R) or write(W) blogs?")
        if read_or_write=="R":
            # list blogs in the databse
            self._list_blogs()
            self._view_blog()
            # display blogs in the database


        elif read_or_write=="W":
            # if they do, prompt a new post inside the blog
            self.user_blog.new_post()

            # if not, prompt to create a new blog

        else:
            print ("Thank you for blogging!")

        pass

    def _list_blogs(self):
        blogs=Database.find(collection='blogs',query={})
        for blog in blogs:
            print ("ID:{},Title:{},Author:{}".format(blog['id'],
                                                     blog['title'],
                                                     blog['author']))
    def _view_blog(self):
        blog_to_see=input("Enter the ID of the blog you'd like to read:")
        blog=Blog.from_mongo(blog_to_see)
        posts=blog.get_posts()
        for post in posts:
            print ("Data{},title{}\n\n{}".format(post['created_date'],post['title'],post['content']))




