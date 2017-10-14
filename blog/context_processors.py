# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     context_processors.py  
   Description :  
   Author :       Uzoma
   date：          2017/4/14
-------------------------------------------------
   Change Activity:
                   2017/4/14: 
-------------------------------------------------
"""
__author__ = 'Uzoma'

from blog.models import Category, Article, Tag, Comment


def sidebar(request):
    category_list = Category.objects.all()

    article_rank = Article.objects.all().order_by('-view')[0:6]

    tag_list = Tag.objects.all()

    comment = Comment.objects.all().order_by('-create_time')[0:6]

    return {
        'category_list': category_list,
        'article_rank': article_rank,
        'tag_list': tag_list,
        'comment_list': comment

    }


if __name__ == '__main__':
    pass
