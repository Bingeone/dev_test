### django项目ORM模式

#### 查询的13个API接口

示例

+ all()

```python
# 查询所有的结果，结果是queryset类型

models.Book.objects.all()
```

+ filter(**kwargs)

> **exact**: 表示等于
>
> models.Book.objects.filter(id__exact=1)
>
> 简写为：
>
> models.Book.objects.filter(id=1)

```python
# 它包含了与给筛选条件的对象，结果也是queryset类型，可以被queryset类型数据调用，也可以直接通过objects控制器进行条用
models.Book.objects.filter(id=1)
models.Book.objects.all().filter(id=1)

# mysql 语法	select * from book where id=2 and publish="xxx"
models.Book.objects.all().filter(id=2, publish='人民出版社')
# 相当于
models.Book.objects.all().filter(**{'id':2, 'publish':'人民出版社'})
```

+ get(**kwargs)

```python
# 返回与所给筛选相匹配的对象，结果不是queryset类型，是行记录（模型类对象）对象，返回结果有且只有一个，如果符合筛选条件的对象超过一个或者没有都会抛出错误。捕获异常try

models.Book.objects.get(id=1)		# objects控制器---调用者
models.Book.objects.all().get(id=1)	# queryset数据类型---调用者

try:
    models.Book.objects.get(id=10)
except BookInf.DoesNotExist:
    print('查询失败')
```

+ exclude(**kwargs)

```python
# 排除的意思，它包含了与所有筛选条件不匹配的对象，不等于的操作，返回结果是queryset类型

models.Book.objects.exclude(id=1)
models.Book.objects.all().exclude(id=1)
```

+ order_by(*field)

```python
# queyset类型的数据来调用，返回值是queryset类型
models.Book.objects.order_by('-price')
models.Book.objects.all().order_by('-price', 'id')		# 多条件

# 在模型中定义字段类排序方法
class Meta:
    ordering = ['-id',]
```

> 注意：在models中定义class Mate 时，在views视图函数order_by("publish")可以覆盖掉id排序，这样子就可以进行distinct()筛选，即 models.Book.objects.all().order_by("publish").values("publish").distinct()

+ reverse()

```python
# queryset类型的数据来调用，对查询结果反向排序，返回值是queryset类型

models.Book.objects.reverse()
models.Book.objects.all().order_by('-id')reverse()
```

+ count()

```python
# queryset类型的数据来调用，返回数据库中匹配查询（Queryset）的对象数量

models.Book.objects.count()
models.Book.objects.all().count()
```

+ first()

```python
# queryset类型的数据来调用，返回第一条数据记录,返回值是模型对象

models.Book.objects.first()
models.Book.objects.all().first() #models.Book.objects.all()[0]
```

+ last()

```python
# queryset类型的数据来调用，返回最后一条数据记录,返回值是模型对象

models.Book.objects.last()
models.Book.objects.all().last() 		# queryset类型的数据不支持负数索引 如Book.objects.all()[-1]
```

+ exists()

```python
# queryset类型的数据调用，如果queryset包含数据，就返回True，否者False

obj_list=models.Book.object.exists()		# 判断该数据库是否存在数据
obj_list=models.Book.objects.filter(id=10).exists()

# select * from book where name="xxx";
if obj_list:	# 满足条件的所有数据进行一次查询，效率低
 
# select count(id) from book where name="xxx";
if obj_list.count()		# 按照查询结果对象的id值进行个数统计

# select id from book where name="xxx" limit1;		# 查询一条数据，不用扫描所有数据
if obj_list.exists()
```

+ values(*field)

```python
# queryset类型的数据调用，返回一个ValueQuerySet---一个特殊的Queryset，运行结果不是model的实例化对象，而是一个可迭代的字典序列

models.Book.objects.values()	# 默认获取所有字段的名称和值
models.Book.objects.all().values()
models.Book.objects.all().values('id','title')	#获取指定的字段内容
```

+ values_list(*field)

```python
# 与values相似，返回的是一个包含元组序列，values返回的是一个包含字典序列

models.Book.objects.all().values_list('id','title')	#获取指定的字段内容,结果以元组x
```

+ distinct()

```python
# values和values_list得到的queryset类型的数据来调用，从返回结果中剔除重复的记录

# 注意distinct方法一般要配合order_by()方法使用，即重新定义排序方法，方便去重
obj_list=models.Book.objects.all().order_by("publish").values("publish").distinct()

# 注意这种写法只适用于 PostgreSQL，对使用mysql中distinct()不支持写入字段内容
Entry.objects.order_by('pub_date').distinct('pub_date')
```

+ choices属性

```python
class Book(models.Model):
    ...
    sex_choices =(
    (1,"男性"),
    (0,"女性"),
    )
    sex=models.IntegerField(choices=sex_choices)
    
#获取含有choices属性的字典的方法
ret=models.Book.objects.get(id=5)
print(ret.sex)	# 获取键值 0或1
print(ret.get_sex_display()) #获取value n
```

+ auto_now_add 和 auto_now

```python
#auto_now_add---添加记录时，自动创建时间
#auto_now---添加记录时，自动创建时间，并且更新记录时也能自动更新为当前时间
#		--- auto_now 对update更新记录无效，无法自动修改为当前时间

#字段models
class Showtime(mdoels.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    brithday=models.DateTimeField(auto_now_add=True)
    bday=models.DateTimeField(auto_now=True)

#操作views
def timer(request):
	#models.Showtime.objects.all().update(name="张三")
	ret=models.Showtime.objects.get(id=1)
	rer.name="张三"
	ret.save()
	return HttpRsponese("ok")
```

#### url别名反向解析

```python
#urls.py 路径管理
path=('book_list', views.book_list, name='book_list')	#name为指定别名

#views.py 视图
from django.urls import reverse		#url别名反向解析

#return redirect('/book_list/')			#这样子路径被固定，urls.py中路径变化影响views.py中路径
return redirect(reverse('book_list'))	#对应上面name的别名值，解决路径变化问题
```

#### views视图中使用url反向解析

```python
#在视图中引入反向解析的方法
from django.urls import reverse

#对urls.py中没有参数的url：path('book_list/', views.book_list, name='book_list')
	反向解析：return redirect(reverse('book_list'))
    
#对urls.py中有无名分组的url：path('book_list/v2/(\d+)/(\d+)', views.book_list, name='book_list')
	反向解析：return redirect(reverse('book_list', args=(11,22)))
    
#对urls.py中有有名分组的url：path('book_list/v2/(?P<year>\d+)/(?P<month>\d+)', views.book_list, name='book_list')
	反向解析：return redirect(reverse('book_list', kwargs={'year':2021,'month':12}))
    

```

> 注：通过redirect进行页面跳转时，redirect方法里面包含了reverse功能，可以直接写url别名
>
> 如：return redirect('book_list')

#### html中使用url反向解析

```html
在html中：
<form action="/book_list/" method="post"></form>
<form action="{% url 'app01:booK_list' %}" method="post"></form>  #app01为apps应用名称

针对无参数的url：path('book_list/', views.book_list, name='book_list')
	反向解析：<a href="{% url 'add_book' %}" class="btn btn-primary">添加书籍</a>

针对有参数url：path('book_list/v2/(\d+)/(\d+)', views.book_list, name='book_list')
			 path('book_list/v2/(?P<year>\d+)/(?P<month>\d+)', views.book_list, name='book_list')
	反向解析：<a href="{% url 'add_book' 2021 11 %}" class="btn btn-primary">添加书籍</a>
```



#### django项目中shell指令的应用

```python
# 在Terminal中 可以使用下方指令，进入django项目
>>>python manage.py shell
>>>from app01 import models
>>>models.Book.objects.filter(price__in=['13.11','1.50'])  #进行简单查询

# 使用 Python Console 直接进入django项目(专业版pycharm)
>>>python manage.py shell
>>>from app01 import models
>>>models.Book.objects.filter(price__in=['13.11','1.50']) 
```



#### 双下滑线模糊查询

```python
Book.objects.filter(price__in=[100,200,300]) 	# price值等于里面的值
示例：
	ret=models.Book.objects.filter(price__in=['13.11','1.50'])  #针对DecimalField字段
    ret=models.Book.objects.filter(price__in=[15, 20])  #针对IntegerField字段 针对float或者int类型
    
Book.objects.filter(price__gt=100)	# 大于100 	price__gte=100表示大于等于100
Book.objects.filter(price__lt=100)	# 小于100
Book.objects.filter(price__range=[100,200])		# 100<=price<=200
Book.objects.filter(title__contains="python")		# title字段包含python
Book.objects.filter(title__icontains="python")		# title字段包含python, 不区分大小写
Book.objects.filter(title__startswith="py")		# title字段包含py开头的, istartswith不区分大小写
Book.objects.filter(title__endswith="2")		# title字段包含2结尾的

# 按照时间查询
Book.objects.filter(pub_date__year=2021)		# pub_date的年分为2021
Book.objects.filter(pub_date__year=2021, pub_date__month=12)# pub_date的年月分为2021/12

# 查询某个空字段的数据
modelsBook.objects.filter(title__isnull=True)	#推荐方式
modelsBook.objects.filter(title=None)	#不合适

# 查询orm语句原生的sql语句
print(models.Book.objects.filter(title__isnull=True).query)
```





#### orm多表操作

+ 一对一关联字段

```mysql
# mysql表格之间关联方式
create table author(
	id = 
    author_detail_id int foreign key references to AuthorDeatil(id) unique on delete cascade
)

```

+ models.py 字段写法

```python
# AuthorDetail和Author 一对一关联
class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    # 生成关联字段 ad_id
    ad = models.ForeignKey(to='AuthorDetail', to_field='id', on_delete=models.CASCADE, unique=True)	#一对一关联id models.CASCADE表示级联删除
    
class AuthorDetail(models.Model):
    birthday = models.DateField()
    telephone = models.CharField(max_length=24)
    address = models.CharField(max_length=64)
    
class Publish(models.Model):
    name=models.CharField(max_length=64)
    city=models.CharField(max_length=64)

class Book(models.Model):
    title=models.CharField(max_length=64)
    pub_date=models.DateField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # Publish和Book一对多关系，to_field='id'可以省略
    pub=models.ForeignKey(to='Publish', on_delete=models.CASCADE, to_field='id')
    #authors在执行数据库同步生成字段，但会生成一个第三方的author和book的多对多关系表：表名book_authors
    authors=models.ManyToManyField(to='Author')
```

+ on_delete级联

```python
'''
book 
id name	pub_id(foreign key)
1	hh	  1
2   hhh   1
3   oo    2


publish
id	address	telephone
1   xx		122
2   yy    	151

#注 book——id为1，2关联到publish的id为1
'''

# on_delete=models.CASCADE 级联删除---就是删除关联所有数据
#不写models.CASCADE是删除其中的一条，不影响关联的数据但会报错
		删除publish id为1的数据，book关联数据保留但查询数据报错
但加上models.CASCADE	删除publish id为1的数据，book关联数据也一并删除

# on_delete=models.SET_NULL 级联删除---删除数据后将关联数据的pub_id设置为null
	删除publish id为1的数据，book关联数据中的pub_id设置为null
    
# on_delete=models.SET(value) 级联删除---删除数据后将关联数据的pub_id设置为vaule(自定义的数值)
	删除publish id为1的数据，book关联数据中的pub_id设置为自定义数值(如：2)
  
# on_delete=models.DO_NOTHING 级联删除---删除数据后将关联数据的pub_id保持不变
	删除publish id为1的数据，book关联数据中的pub_id保持不变，不影响关联数据
```

+ on_delete字段参数说明

```bash
on_delete
当删除关联表中的数据时，当前表与其关联的行的行为。

models.CASCADE
删除关联数据，与之关联也删除


models.DO_NOTHING
删除关联数据，引发错误IntegrityError


models.PROTECT
删除关联数据，引发错误ProtectedError


models.SET_NULL
删除关联数据，与之关联的值设置为null（前提FK字段需要设置为可空）


models.SET_DEFAULT
删除关联数据，与之关联的值设置为默认值（前提FK字段需要设置默认值）


models.SET

删除关联数据，
a. 与之关联的值设置为指定值，设置：models.SET(值)
b. 与之关联的值设置为可执行对象的返回值，设置：models.SET(可执行对象)

关于on_delete参数
```

+ db_containt

```python
#db_constraint=False只加两者的关系，没有强制约束的效果，并且ORM外键相关的接口(方法)还能使用，所以如果将来公司让你建立外键，并且不能有强制的约束关系，那么就可以将这个参数改为False
customer = models.ForeignKey(verbose_name='关联客户', to='Customer',db_constraint=False)

```





#### views视图中对获取数据并更新的方式

```python
# 获取字典带内部带列表
print(request.POST)
<QueryDict: {'title': ['水浒传1'], 'price': ['31.00'], 'pub_date': ['2021-11-01'], 'publish': ['人民出版社1']}>

# 获取完整的字典
print(request.POST.dict())
{'title': '水浒传1', 'price': '31.00', 'pub_date': '2021-11-01', 'publish': '人民出版社1'}

```

> 注：**dict()方法将QueryDict类型数据转换为普通字典类型**

+ 更新数据

```python
# 方式一(逐个字段获取并更新)
title = request.POST.get('title')
price = request.POST.get('price')
pub_date = request.POST.get('pub_date')
publish = request.POST.get('publish')
obj_list.update(
    title=title,
    price=price,
    pub_date=pub_date,
    publish=publish
)
# 方式二(整个字段更新)
obj_list.update(**request.POST.dict())	# dict()方法将QueryDict类型数据转换为普通字典类型
```

+ 存在Decimal字段注意

```python
# Decimal字段只识别普通的字典类型，不能是QueryDict类型
a= '12.22'
import decimal
decimal.Decimal(a)
Decimal('12.22')
aa= ['123','frre']
decimal.Decimal(aa)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ValueError: argument must be a sequence of length 3
    
```

+ 删除delete字段

```python
#查询某个id的数据条，并delete()
models.Book.objects.filter(pk=book_id).delete()
```

+ OneToOneField字段

```python
# ForeignKey表示外键关系，一对多，注意django2.0之后版本额外加上on_delete=models.CASCADE,
# 确定一对多关系，外键字段建立在多的一方
ad=models.ForeignKey('AuthorDetail', on_delete=models.CASCADE, unique=True)
ad=models.OneTOneField('AuthorDetail'， on_delete=models.CASCADE,)	# OneToOneField 相当于ForeignKey + unique 一对一
```



#### 关于多对多表的三种创建方式

+ 方式一：自行创建第三张表(无法使用模型类的方法如add() ,自行对第三张表手动添加sql语句)

```python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")


class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")


# 自己创建第三张表，分别通过外键关联书和作者
class Author2Book(models.Model):
    author = models.ForeignKey(to="Author")
    book = models.ForeignKey(to="Book")

    class Meta:
        unique_together = ("author", "book")
```

+ 方式二：通过ManyToManyField自动创建第三张表

```python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")


# 通过ORM自带的ManyToManyField自动创建第三张表
class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")
    books = models.ManyToManyField(to="Book", related_name="authors")  #自动生成的第三张表我们是没有办法添加其他字段的
```

+ 方式三：设置ManyTomanyField并指定自行创建的第三张表（称为中介模型）

```python
class Book(models.Model):
    title = models.CharField(max_length=32, verbose_name="书名")


# 自己创建第三张表，并通过ManyToManyField指定关联
class Author(models.Model):
    name = models.CharField(max_length=32, verbose_name="作者姓名")
    books = models.ManyToManyField(to="Book", through="Author2Book", through_fields=("author", "book"))
    # through_fields接受一个2元组（'field1'，'field2'）：
    # 其中field1是定义ManyToManyField的模型外键的名（author），field2是关联目标模型（book）的外键名。


class Author2Book(models.Model):
    author = models.ForeignKey(to="Author")
    book = models.ForeignKey(to="Book")
    #可以扩展其他的字段了
    class Meta:
        unique_together = ("author", "book")
```



#### 单表和多表字段说明

+ 创建一对一关系(OneToOneField)

```python
to			# 设置要关联的表
to_field	# 设置要关联的字段
on_delete	# ForeignKey字段的级联删除
```

+ 创建一对多关系(ForeignKey)

```python
to			# 设置要关联的表
to_field	# 设置要关联的字段
on_delete	# ForeignKey字段的级联删除
related_name	# 反向操作时，使用的字段名，用于代替原反向查询的'表名_set'
related_query_name	# 反向查询操作时，使用的连接前缀，用于替换表名
db_containt=False	# 不加强制关系约束
```

+ 创建多对多关系(ManyToManyField)

```python
to			# 设置要关联的表
to_field	# 设置要关联的字段
on_delete	# ForeignKey字段的级联删除
related_name	# 反向操作时，使用的字段名，用于代替原反向查询的'表名_set'
related_query_name	# 反向查询操作时，使用的连接前缀，用于替换表名
through	# 指定第三张表的名称
through_filed	# 设置关联的字段(第三张表里的字段)
db_table		# 默认创建第三张表时，数据库中表名称
db_column		# 指定列名称	针对第三张表的列项名称如 authors_id	修改为 author_authordetail_id
```

+ 元信息(Mate)

```python
# Meta类封装了一些数据库的信息
class Author2Book(models.Model):
    author = models.ForeignKey(to="Author")
    book = models.ForeignKey(to="Book")
    #可以扩展其他的字段了
    class Meta:
        unique_together = ("author", "book")
        db_table = 'tb_author_book'
        ordering = ['-pub_date']
        verbose_name = '信息统计'  
        verbose_name_plural = '信息统计' 
        
db_table		# 重写表名(默认表名为 子应用名_类名(小写) 如：app01_author2book)
index_together	# 联合索引
unique_together	# 联合唯一索引
ordering		# 指定默认排序
verbose_name			# 后台名称
verbose_name_plural		# 后台名称复数形式
```



#### 查询集 QuerySet

##### 概念

Django的ORM中存在查询集的概念，查询集也称为查询结果集，表示从数据库中获取的对象集合

当调用以下的过滤方法时，django会返回查询集：

+ all(): 返回所有数据
+ filter(): 返回满足条件的数据
+ exclude(): 返回满足条件之外的数据
+ order_by(): 对结果进行排序
+ exists(): 判断查询集中是否有数据，有返回True，没有返回False

##### 两大特性

+ 惰性执行

创建查询集不会访问数据库，查询调用数据时，才会访问数据库，调用数据的情况包括迭代，序列化，与if合用

```python
# 如:	创建一个查询集qs
qs = BookInfo.objects.all()
# 继续执行遍历迭代操作后，真正地进行了数据库地查询
for book in qs:
    print(book.btitle)
```

+ 缓存

使用同一个查询集，第一次使用时会发生数据库地查询，然后django会把结果缓存下来，再次使用这个查询集时会使用缓存地数据，减少了数据库地查询次数

```python
# 查询所有书籍id---查询两次数据库
[book.id for book in BookInfo.objects.all()]	# [1,2,3,4]
[book.id for book in BookInfo.objects.all()]	# [1,2,3,4]

# 查询所有书籍id---查询1次数据库---缓存结果
qs=BookInfo.objects.all()
[book.id for book in qs]
[book.id for book in qs]
```

##### 限制查询集

可以对查询集进行取下标或切片操作，等同于sql中事务limit和offset子句

> 注：不支持负数索引

```python
# 如
qs = BookInfo.objects.all()[0:2]

```



#### 关于多表关系中的增删改查使用方式

##### views.py视图写法---增加

```python
def test(request):
# 一对一 Author和AuthorDetail
# 方式一：用模型类的字段来创建
    au_obj=models.AuthorDetail.objects.get(id=1)
    models.Author.objects.create(
    	name='小李',
        age=20,
       	ad=au_obj,
    )
# 方式二：用数据库中的字段创建
	models.Author.objects.create(
    	name='小李',
        age=20,
       	ad_id=1,
    )
    
    
# 一对多 Publish和Book(多)
# 方式一：用模型类的字段来创建
	publish_obj=models.Publish.objects.get(id=1)
    models.Book.objects.create(
    	title='雨后人生',
        pub_date='2021-05-11',
        price=56.00,
        pub=publish_obj
    )
# 方式二：用数据库中的字段创建
    models.Book.objects.create(
    	title='雨后人生',
        pub_date='2021-05-11',
        price=56.00,
        pub_id=1
    )
    
    
# 多对多 Book和Author
# 方式一：写模型对应作者的模型类对象
	book_obj=models.Book.objects.create(
    	title='天空彩虹',
        pub_date='2020-05-11',
        price=22.00,
        pub_id=1
    )
    author_obj1=models.Author.objects.create(
    	name='王真',
        age=20,
       	ad_id=3,
    )
    author_obj2=models.Author.objects.create(
    	name='李维',
        age=20,
       	ad_id=4,
    )
    book_obj.authors.add(author_obj1,author_obj2)
# 方式二：直接写作者author的id
	book_obj.authors.add(3，4)
    
    #book_obj = models.Book.objects.get(id=1)
    #book_obj.authors.add(*[2,3])
    
	return HttpResponse('ok')

'''
mysql数据库中的第三张 多对多关系表
id	book_id	author_id
1	3		3
2	3		4

'''
```

##### 删除

```python
# delete
# 一对一,一对多
models.Author.objects.filter(id=1).delete()
```

##### 更新修改

```python
# 与单表操作一样
# 一对一
models.Author.objects.filter(id=1).update(name='xx', ad_id=2)	

# 一对多
pub_obj = models.Publish.objects.get(id=2)
models.Book.objects.filter(id=1).update(name='xx', pub=pub_obj)		# 模型类对象

# 多对多的更新和删除(即对第三张关系表的操作)
# 先删除remove 
book_obj = models.Book.objects.get(id=1)
book_obj.authors.remove(2)		#删除关联的id=2的作者	单条
book_obj.authors.remove(2,3)	# 多条直接写id号

author_obj = models.Author.objects.get(id=2)
book_obj.authors.remove(author_obj)		# 写模型类对象

# 清空clean
book_obj.authors.clear()	#清空所有关联的记录

# 更新(修改)set
# set()方法先执行clear,后执行add添加
book_obj = models.Book.objects.get(id=4)
book_obj.authors.set('3')	# 注意是字符串形式或列表 
book_obj.authors.set([3, ]) # 列表

```

##### 查询

+ **基于对象的查询**

```python
def check(request):
# 一对一
    # 正向查询：关系属性写在哪张表里，通过这张表的数据去查询关联表的数据，就叫正向查询---使用关联属性的名称
    # 查询叫 小李 这个作者的手机号
    author_obj=models.Author.objects.get(name='小李')
    print(author_obj.ad.telephone)	#关联属性ad
    
    # 反向查询---使用关联他的模型类名称的小写
    # 查询地址在 上海 的作者名字
    author_detail_obj=models.AuthorDetail.objects.filter(address='上海').first()
    print(author_detail_obj.author.name)	# 关联模型类名称

# 一对多
	# 正向查询
    # 查询 雨后人生 是哪个出版社的
    book_obj=models.Book.objects.get(title='雨后人生')
    print(book_obj.pub.name)	#关联属性ad
    
    # 反向查询---使用关联他的模型类名称小写_set
    # 查询 人民出版社 出版了哪些书
    pub_obj=models.Publish.objects.get(name='人民出版社')
    #pub_obj.book_set	# 可能为多条记录，模型类名称小写_set, 等到结果类似objects对象
    print(pub_obj.book_set.all())	# 结果为QuerySet[<Book: Book objects>] 
    print(pub_obj.book_set.all().values('title'))
    
# 多对多
	# 正向查询
    # 查询 雨后人生 的作者是谁
    book_obj=models.Book.objects.get(title='雨后人生')
    print(book_obj.authors.all().values('name')
    
    # 反向查询---使用关联他的模型类名称小写_set
    # 查询 小李 出版了哪些书
    author_obj=models.author.objects.get(name='小李')
    print(author_obj.book_set.all().values('title'))
          
    return HttpResponse('ok')

```

+ 基于双下划线的跨表查询

```python
def check(request):
    # 连表操作
# 一对一
	# 正向
	# 查询作者 小李 的家庭住址
    ret=models.Author.objects.filter(name='小李').values('ad__address')
    print(ret)
    
    # 反向
    # 查询作者 小李 的家庭住址
    ret=models.AuthorDetail.objects.filter(author__name='小李').values('address')
    print(ret)
    
# 一对多
	# 正向查询
    # 查询 雨后人生 是哪个出版社的    
    ret=models.Book.objects.filter(title='雨后人生').values('pub__name')
    print(ret)
    
    # 反向查询
    # 查询 雨后人生 是哪个出版社的 
    ret=models.Publish.objects.filter(book__name='雨后人生').values('name')
    print(ret)
    
# 多对多
	# 正向查询
    # 查询 雨后人生 的作者是谁
    ret=models.Book.objects.filter(title='雨后人生').values('authorss__name ')
    print(ret)
    
    # 反向查询
    # 查询 雨后人生 的作者是谁
    ret=models.Author.objects.filter(book.__title='雨后人生').values('name')
    print(ret)
    
    return HttpResponse('ok')
```

##### 聚合查询(aggregate)

```python
from django.db.models import Max,Min,Count,Sum,Avg
def check(request):
    # 聚合查询
    # 统计所有书籍的平均价格,max min sum count
    ret=models.Book.objects.aggregate(Avg('price'))
    ret=models.Book.objects.all().aggregate(a=Avg('price'),b=Max('price'))
    print(ret)
    
    return HttpResponse('ok')

```

##### 分组查询(annotate)

```python
def check(request):
    # 分组查询
    # 查询一下每个出版社出版书的平均价格
    ret=models.Book.objects.values('pub_id').annotate(a=Avg('price'))#以出版社pub_id分组,只能获取到values指定的字段和统计的结果
    
    #反向查询价格
    ret=models.Publish.objects.annotate(a=Avg('book__price'))	#结果为Publish的模型类对象，包含Publish的所有属性数据，还有annotate的统计结果数据
    ret=models.Publish.objects.annotate(a=Avg('book__price')).values('name','a')
	print(ret)
    
    return HttpResponse('ok')


#sql语句
'''
select Avg(price) from book group by pub_id;

select publish.name,Avg(book.price) from publish inner join book on publish.id=book.pub_id group by publish.id;
''' 
```

##### F查询

+ 主要针对本表不同字段内容之间的比较
+ F查询可以用来对本表数据进行一些统一操作

```python
from django.db.models import F,Q
def check(request):
	# 查询点赞数大于评论数的书籍
    '''
    obj_list=models.Book.objects.all()
    a=[]
    for i in obj_list:
    	if i.dianzan > i.comment:
    		a.append(i)
    print(a)
    '''
    ret=models.Book.objects.filter(dianzan__gt=F('comment'))	#点赞数大于评论数
    print(ret)
    
    # 将所有书籍价格上调10
    ret=models.Book.objects.all().update(price=F('price')+10)
    print(ret)
    return HttpResponse('ok')
```

##### Q查询

+ 可以进行多条件查询，查询关系可以是 或与非

```python
from django.db.models import F,Q
def check(request):
	# 查询title包含 雨后 文字的 并且评论数大于20
    ret=models.Book.objects.filter(title__contains='雨后', comment__gt=20)#逗号表示与
    
    # 查询title包含 雨后 文字的 或者 评论数大于20---Q查询
    ret=models.Book.objects.filter(Q(title__contains='雨后')|Q(comment__gt=20))
    
    # 查询title包含 雨后 文字的 或者 评论数大于20，并且点赞数大于等于80
    ret=models.Book.objects.filter(Q(title__contains='雨后')|Q(comment__gt=20), diamzan__gte=80)	# 并且的条件必须放在Q条件的后面 	# ~表示取反，~Q(dianzan__g)
    print(ret)
    return HttpResponse('ok')
```

##### 查询练习

```python
def query(request):
    # 查询每个作者的姓名以及出版书的最高价---加id避免姓名重名 
    ret=models.Book.objects.values('author__name','author_id').annotate(a=Max('price'))
    
    ret=models.Author.objects.values('name','a').annotate(a=Max('book__prices'))
    print(ret)
    
    # 查询作者id大于2作者的姓名以及出版的书的最高价格
    ret=models.Book.objects.values('author__name','author_id__gt=2').annotate(a=Max('price'))
     			ret=models.Author.objects.filter(id__gt=2).values('name','a').annotate(a=Max('book__prices'))
        
    # 查询作者id大于2或者作者年龄大于等于20岁的女作者的姓名以及出版的书最高价格
    ret=models.Author.objects.filter(Q(id_gt=2)|(Q(age__gte=20,sex='1')).annotate(a=Max('book__price')).values('name','a')
                                     
    # 查询每个作者出版的书的最高价格 的平均值
ret=models.Book.objects.values('authors_id').annotate(a=Max('price')).aggregate(b=Avg('a'))
                                     
	# 每个作者出版的所有书的最高以及最高价格的那本书的名称
ret=models.Author.objects.annotate(a=Max('booK_price')).values('book_title','a')#写法有问题
                                     
'''

'''
    return HttpResponse('ok')
```



#### ORM执行原生sql语句

##### raw()

```python
def query(request):
    ret=models.Book.objects.raw('select * from app01_book;')
    print(ret)		#<RawQuerySet: select * from app01_book> 这里只能执行本表的结果
    for i in ret:
        print(i)	
    return HttpResponse('ok')
```

##### connection连接mysql数据库

```python
from django.db import connection
def query(request):
	
    cursor=connection.curcor()
    cursor.exexute('select * from app01_book;')
    print(cursor.fetchall())		#查询出每条sql语句的结果
    
    return HttpResponse('ok')
```

#### python外部脚本调用django环境

> **python manage.py shell 进入django项目环境**

```python
#外部文件ex.py
# 加载django环境
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
# 运行环境
import django
django.setup()

if __name__ == '__main':
    from app01 import models
    print(models.Book.objects.all())

```

#### ORM锁和事务

+ 加锁写法，必须用在事务里面

```python
models.Book.objects.select_for_update().all()
'''
select * from app01_book for update;
'''
```

+ 全局事务开启

方式一: 在setting.py文件中设置

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxshop',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '123',
        'OPTIONS': {
            "init_command": "SET default_storage_engine='INNODB'",
　　　　　　　#'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", #配置开启严格sql模式


        }
        "ATOMIC_REQUESTS": True, #全局开启事务，绑定的是http请求响应整个过程        			"AUTOCOMMIT":False, #全局取消自动提交，慎用
    },　　
    'other':{'ENGINE': 'django.db.backends.mysql',
             ......　　} #还可以配置其他数据库
}
```

方式二：给视图函数直接加装饰器，表示整个视图逻辑中的sql都捆绑为一个事务操作

```python
from django.db import transaction

# sql一旦出错，会自动回滚（恢复到上一步）
@transaction.atomic
def viewfunc(request):
    # This code executes inside a transaction.
    do_stuff()
```

方式三：给逻辑上下文加视图

```python
from django.db import transaction

def viewfunc(request):
    # This code executes in autocommit mode (Django's default).
    do_stuff()

    with transaction.atomic():   #保存点
        # This code executes inside a transaction.
        do_more_stuff()

    do_other_stuff()
```





### models.py中关键词说明

#### 字段类型

| 类型             | 说明                                                         |
| ---------------- | ------------------------------------------------------------ |
| AutoField        | 自动增长的IntegerField，通常不指定，django默认将id属性设置为自动增长 |
| BooleanField     | 布尔字段，值为True或False                                    |
| NullBooleanField | 支持Null、True、False                                        |
| CharField        | 字符串，参数max_length表示字符串长度最长值                   |
| TextField        | 大文本字段，一般超过4000个字符时使用                         |
| IntegerField     | 整数                                                         |
| DecimalField     | 十进制浮点数，参数max_digits表示总位数，decimal_places表示小数位数 |
| FloatField       | 浮点数                                                       |
| DateField        | 日期，参数auto_now表示创建时当前的日期，不随更新修改而改变，参数auto_now_add总是表示当前日期，内容更新会更新日期 |
| TimeField        | 时间，参数同Datefiled                                        |
| DateTimeField    | 日期时间，参数同上                                           |
| FileField        | 上传文件字段                                                 |
| ImageField       | 继承于FileField，对上传的内容进行校验，确保是有效的图片      |

#### 选项

| 选项        | 说明                                                         |
| ----------- | ------------------------------------------------------------ |
| null        | 如果为True，表示允许为空，默认值是False                      |
| blank       | 如果为True，表示该字段允许为空白，默认为Fasle                |
| db_column   | 字段的名称，如果未指定，则使用默认的属性                     |
| db_index    | 如果为True，则表中会为此字段创建索引，默认值是Fasle          |
| default     | 默认值                                                       |
| primary_key | 如果为True，则该字段会成为模型的主键字段，默认为False，一般作为AutoField的选项使用 |
| unique      | 如果为True，该字段在表中必须有唯一值，默认值为Fasle          |

**null是数据库中的关键字，blank是表单中的(用于后台是否可为空)**

#### 外键

> 在设置外键时，须通过on_delete选项指明主表删除数据时，对外键引用表数据如何处理，在django.db.models中可选的常量

+ **models.CASCADE**级联，删除主表数据时连一起删除外键表中数据
+ **PROTEST**,通过抛出ProtectdError异常，来阻止删除主表中被外键应用的数据
+ **SET_NULL** 设置为Null，仅在该字段null=True允许为null时可用
+ **SET_DEFAULT**设置为默认值，仅在该字段设置默认值时可用
+ **SET()**设置为特定值或者调用特定方法





### setting.py 文件配置

#### LOGGING项目日志配置

+ **打印orm转换过程中的sql**

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}
```

+ **查看sql方式二**

> 通过django配置连接的mysql的管道来查看（pymysql）

```python
from app01 import models

def add_book(request):
    '''
    添加表记录
    :param request: http请求信息
    :return:
    '''
    book_obj = models.Book(title='python',price=123,pub_date='2012-12-12',publish='人民出版社')
    book_obj.save()
    from django.db import connection  #通过这种方式也能查看执行的sql语句
    print(connection.queries)
    return HttpResponse('ok')
```



+ 完整配置

```python
BASE_LOG_DIR = os.path.join(BASE_DIR, "log")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],  # 只有在Django debug为True时才在屏幕打印日志
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'SF': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，根据文件大小自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,  # 备份数为3  xx.log --> xx.log.1 --> xx.log.2 --> xx.log.3
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'TF': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 保存到文件，根据时间自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
            'backupCount': 3,  # 备份数为3  xx.log --> xx.log.2018-08-23_00-00-00 --> xx.log.2018-08-24_00-00-00 --> ...
            'when': 'D',  # 每天一切， 可选值有S/秒 M/分 H/小时 D/天 W0-W6/周(0=周一) midnight/如果没指定时间就默认在午夜
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
        '': {  # 默认的logger应用如下配置
            'handlers': ['SF', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,
        },
        'collect': {  # 名为 'collect'的logger还单独处理
            'handlers': ['console', 'collect'],
            'level': 'INFO',
        }
    },
}
```



### admin 站点

#### 管理界面汉化

##### setting.py 中设置

```python
LANGUAGE_CODE = 'zh-hans' # 使用简体汉字
TIME_ZONE = 'Asia/Shanghai' # 使用中国上海时间
```

##### 创建超级管理员

```python
python manage.py createsuperuser
# 输密码 和 邮箱

# 浏览地址
http://127.0.0.1:8000/admin/
```



#### 注册模型后台应用

> 注意：如果模型已经迁移表中的字段，并且表中已经有数据了，那么后添加的新字段必须可以为空或者给默认值，不然迁移会报错
>
> ImageField 字段依赖python包 Pillow

##### admin.py文件修改

```python
from django.contrib import admin
from .models import BookInfo,HeroInfo

# 拓展BookInfo编辑页面的子表内容 与inlines结合使用 管理对象展示
class HeroInfoStack(admin.TabularInline):
    model = HeroInfo
    extra = 1       # 设置可添加的空格子数量   StackedInline块状  TabularInline表格形式


class BookInfoAdmin(admin.ModelAdmin):
    '''调整书籍数据在站点界面显示'''
    list_display = ['id', 'btitle', 'bread', 'bcomment', 'bpub_date_format']    # 自定义模型的方法bpub_date_format
    
    # 执行框的位置
    actions_on_bottom = True
    actions_on_top = False
    
    # 每页显示条数
    list_per_page = 3
	
    # 列表字段连接
    list_display_links = ['id', 'btitle']
    
    # 设置编辑页面显示的字段内容
    # fields = ['btitle', 'bpub_date']

    # 设置编辑字段分组展示
    fieldsets = [
        ['基础组', {'fields': ['btitle', 'bpub_date', 'image']}],
        ['高级组', {
                    'fields': ['bread', 'bcomment'],
                    'classes': ['collapse']         # 设置该组默认 折叠
                  }]
    ]

    # 展示关联的models字段 放在关联的 主表
    inlines = [HeroInfoStack]       # 在书籍编辑页面关联展示 英雄数据


@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    '''调整英雄数据在站点展示'''

    # 列表内容显示字段
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'hbook', 'read']
    # 设置右侧过滤栏 过滤器字段
    list_filter = ['hbook', 'hgender']
    # 设置搜索框
    search_fields = ['hname', 'id', 'hgender']

# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
# admin.site.register(HeroInfo, HeroInfoAdmin)

# 站点标题修改 全局属性
admin.site.site_header = '小智书城'
admin.site.site_title = '小智书城MIS'
admin.site.index_title = '欢迎使用小智书城MIS'
```

##### models.py 文件中自定义列表字段

```python
from django.db import models

class BookInfo(models.Model):

    btitle = models.CharField(max_length=32, verbose_name='书名')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    image = models.ImageField(verbose_name='图片', null=True, upload_to='book')

    class Meta:
        db_table = 'tb_books'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.btitle
	
    # 自定义BookInfo 列表的bpub_date字段
    def bpub_date_format(self):
        return self.bpub_date.strftime('%Y-%m-%d')      # 时间格式化成指定的样式
    bpub_date_format.short_description = '发布日期'       # 修改方法名在列表中展示成中文
    bpub_date_format.admin_order_field = 'bpub_date'    # 此方法中的数据依据模型的哪个字段进行排序 heroinfo_hname


class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, '女'),
        (1, '男')
    )
    hname = models.CharField(max_length=32, verbose_name='名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, blank=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname
    
	 # 拓展HeroInfo列表的 read字段
    def read(self):
        return self.hbook.bread
    read.short_description = '阅读量'
    read.admin_order_field = 'hbook__bread'         # 反向用 __ 双下划线
```



##### apps.py文件修改

```python
from django.apps import AppConfig


class BooktestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'booktest'
    verbose_name = '书籍'
```

#### 上传图片

> 使用admin站点保存图片，需要安装python的依赖包

```python
pip install Pillow
```

setting.py文件中设置media文件路径

```python
MEDIA_ROOT=os.path.join(BASE_DIR, 'static_files/media')
```

在models.py 文件中添加字段

```python
class BookInfo(models.Model):
	...
    image = models.ImageField(verbose_name='图片', null=True, upload_to='book')
    # book表示一个文件夹，，需要手动在media文件夹下创建，null=True允许数据库为空，避免报错
```



### ajax使用

> js的功能，特点：异步请求，局部刷新
>
> 基于jquery的ajax请求，异步请求不会刷新页面，页面上用户之前输入的数据都不会丢失
>
> 注：在setting.py文件中添加 APPEND_SLASH=False 可省去ajax中路径的 '/'斜杠问题

```html
# 普通的登录信息属性

<div>
<p>ajax请求</p>
<label>
用户：<input type="text" name="username" id="username">
</label>
<label>
密码：<input type="text" name="password" id="password">
<button id="btn">提交</button>
</label>
</div>

<script src="/static/js/jquery.js"></script>
<script>
    $('#btn').click(function (){
        var uname = $('#username').val();
        var pwd = $('#password').val();

        $.ajax({
            url:'/login_ajax/', 		 //相对路径	注意加斜杠/
            //url: '{% url 'login_ajax' %}'		//模板渲染语法在html中可以使用，但不能中纯jsj
            type:'post',				//请求方法
            data:{xx:uname,pp:pwd},    //ajax请求携带数据和格式
            success:function (res){
                //success对应的function表示请求成功（正常）之后自动执行的函数
                //res名字随便写，res就是得到的响应数据
                //console.log(res, typeof(res))
                if (res === 'ok'){
                    location.href = '/home/';
                }
                else{
                    $('#error_msg').text('用户名或者密码错误');
                }
            }
        })
    })
</script>
```

**浏览器控制台分析：XHR全称xmlhttprequest对象**

> from django.shortcuts import render, HttpResponse, redirect
>
> **render**：渲染页面
>
> **HttpResponse**：渲染字符串
>
> **redirect**：渲染对象
>
> from django.http import JsonResponse
>
> JsonResponse：直接访问json数据

#### JsonResponse反序列化

```python
def data(request):
    data_list={'name':'xx','hobby':['女','男']}
    data_list_str=json.dumps(data_list, ensure_ascii=False)
    return HttpResponese(data_lsit_str)
	
    # return JsonResponse(data_list)	//字典数据直接，非字典得 加safe=False
# JsonResponse:
# 1\序列化数据
# 2\加上['content-type']='application/json'响应头键值对

#相当于 手动加上ret['content-type']='application/json'
ret = HttpResponse(data_list_str)
ret['content-type']='application/json'
return ret

```



##### html页面js

```html
<ul></ul>
<p id='btn'>ajax返回数据<p/>
<script src="/static/js/jquery.js"></script>
<script>
    $('#btn').click(function (){
        $.ajax({
            url:'/data/', 		 //相对路径	注意加斜杠/
            type:'get',				//请求方法
            success:function (res){
                console.log(res,typeof res)
                
                //将数据放到li标签中，然后添加到ul标签中进行数据展示
                for (var i =0;i<res.length; i++){
                    var content=res[i];
                    var liEle=document.createElement('li');
                    liEle.innerText = content
                    $('ul').append(liEle);
                    
                    //第二种方式
                    var liStr = `<li>${content}</li>`
                    $('ul').append(liStr);
                }
            }
        })
    })
</script>

```

##### 请求头消息式分析

> 请求消息格式和请求方法没有关系
>
> 和请求头键值对中的这一组键值对有关系

```python
Content-Type:application/x-www-form-urlencoded; #浏览器发送数据ajax或者form表单，默认的格式都是它
    它表示请求携带的数据格式：application/x-www-urlencoded  对应的数据格式a=1&b=2
     
```



```python
# form表单上传文件
# enctype="multipart/form-data" 就是将本次请求的消息格式 content-type 更改为multipart/form-data
<form action="/sub/" method="post" enctype="multipart/form-data">
    xx: <input type="text" name="xx">
    oo: <input type="text" name="oo">
    <input type="file">
    <input type="submit">
</form>

# 另一种消息请求方式：application/json
<script>
    $('#btn').click(function (){
        $.ajax({
            url:'/data/', 		 //相对路径	注意加斜杠/
            type:'get',				//请求方法
            headers:{
                'Content-Type':'application/json',
            },
            success:function (res){
                console.log(res,typeof res)
            }
        })
    })
</script>

```

