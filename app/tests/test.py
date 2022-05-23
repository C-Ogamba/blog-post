import unittest 
from app.models import User, Comment, Article, Post, Subscriber

class PostTest(unittest.TestCase):   
    def setUp(self):        
        self.post = Post("Cindy", "life is fun, code is even better")
    def test_instance(self):        
        self.assertTrue(isinstance(self.post, Post))

class UserTest(unittest.TestCase):    
    def setUp(self):        
        self.new_user = User("Cindy", "cin.kemu@gmail.com", "cindy")
    def test_instance(self):        
        self.assertTrue(isinstance(self.new_user, User))

class SubscriberTest(unittest.TestCase):    
    def setUp(self):        
        self.new_subscriber = Subscriber(email="cin.kemu@gmail.com")
    def test_instance(self):        
        self.assertTrue(isinstance(self.new_subscriber, Subscriber))

class ArticleTest(unittest.TestCase):    
    def setUp(self):        
        self.new_article = Article(title="sample title", filename="sample path", content="sample content", date="2022-5-15")
    def test_instance(self):        
        self.assertTrue(isinstance(self.new_article, Article))

class CommentTest(unittest.TestCase):    
    def setUp(self):        
        self.new_comment = Comment(comment="this is a sample comment", user_id=1)
    def test_instance(self):        
        self.assertTrue(isinstance(self.new_comment, Comment))

if __name__== '__main__':    
    unittest.main()