# -*- coding:utf-8 -*-
from blog.models import Author,Article,Tag
import random
import os,django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django2.settings")
# django.setup()

author_list=['张三','李四','王五','赵六']
article_list=['python 教程','sql 教程','django 教程','java 教程']

def create_authors():
    for author_name in author_list:
        author,created=Author.objects.get_or_create(name=author_name)
        author.qq=''.join(str(random.choice(range(10))) for _ in range(9))
        author.addr='addr_%s'%(random.randrange(1,3))
        author.email='%s@blog.com'%(author.name)
        author.save()

def create_article_tags():
    for article_title in article_list:
        tag_name=article_title.split(' ',1)[0]
        tag,created=Tag.objects.get_or_create(name=tag_name)

        random_author=random.choice(Author.objects.all())

        for i in range(1,21):
            title='%s_%s'%(article_title,i)
            article,created=Article.objects.get_or_create(
                title=title,defaults={
                    'author':random_author,
                    'content':'%s 正文'%title,
                    'score':random.randrange(70,101)
                }
            )
            article.tags.add(tag)

def main():
    create_authors()
    create_article_tags()
if __name__ == '__main__':
    main()
    print('Done')