import urllib
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods import posts
import xmlrpclib
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import os


class CustomWpxmlrpc:
    def post_article(self, wordpress_link, wordpress_id, wordpress_pass, articletitle, articlecategories,
                     articlecontent, articletags, imagelink=None):
        if imagelink:
            self.path = os.getcwd() + "\\00000001.jpg"
            self.articlePhotoUrl = imagelink
            self.wpUrl = wordpress_link
            self.wpUserName = wordpress_id
            self.wpPassword = wordpress_pass
            # Download File
            f = open(self.path, 'wb')
            f.write(urllib.urlopen(self.articlePhotoUrl).read())
            f.close()
            # Upload to WordPress
            client = Client(self.wpUrl, self.wpUserName, self.wpPassword)
            filename = self.path
            # prepare metadata
            data = {
                'name': 'picture.jpg', 'type': 'image/jpg',
            }

            # read the binary file and let the XMLRPC library encode it into base64
            with open(filename, 'rb') as img:
                data['bits'] = xmlrpc_client.Binary(img.read())
            response = client.call(media.UploadFile(data))
            attachment_id = response['id']
            # Post
            post = WordPressPost()
            post.title = articletitle
            post.content = articlecontent
            post.terms_names = {'post_tag': articletags, 'category': articlecategories}
            post.post_status = 'publish'
            post.thumbnail = attachment_id
            post.id = client.call(posts.NewPost(post))
            print 'Post Successfully posted. Its Id is: ', post.id
        else:
            self.wpUrl = wordpress_link
            self.wpUserName = wordpress_id
            self.wpPassword = wordpress_pass
            # Upload to WordPress
            client = Client(self.wpUrl, self.wpUserName, self.wpPassword)
            # Post
            post = WordPressPost()
            post.title = articletitle
            post.content = articlecontent
            post.terms_names = {'post_tag': articletags, 'category': articlecategories}
            post.post_status = 'publish'
            post.id = client.call(posts.NewPost(post))
            print 'Post Successfully posted. Its Id is: ', post.id

xmlrpc_object = CustomWpxmlrpc()
