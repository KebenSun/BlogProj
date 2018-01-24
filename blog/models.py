from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=100, verbose_name='分类名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100, verbose_name='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Post(models.Model):
    """
    文章
    """

    # 文章标题
    title = models.CharField(verbose_name='标题', max_length=70)

    # 文章正文
    body = models.TextField(verbose_name='正文')

    # 创建时间和更新时间
    created_time = models.DateTimeField(verbose_name='发布时间')
    modified_time = models.DateTimeField(verbose_name='修改时间')

    # 封面图片
    cover_pic = models.ImageField(verbose_name="封面图片", upload_to='post', default='post/post_default.jpg')

    # 摘要
    excerpt = models.CharField(verbose_name='摘要', max_length=200, blank=True)

    # 分类与标签外键
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')

    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    # 阅读量
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客'
        ordering = ['-created_time', 'title']

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                ])
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        super(Post, self).save(*args, **kwargs)
