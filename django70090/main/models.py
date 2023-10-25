#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class xuesheng(BaseModel):
    __doc__ = u'''xuesheng'''
    __tablename__ = 'xuesheng'

    __loginUser__='xuehao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='xuehao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xuehao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='学号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    touxiang=models.CharField ( max_length=255, null=True, unique=False, verbose_name='头像' )
    '''
    xuehao=VARCHAR
    mima=VARCHAR
    xingming=VARCHAR
    xingbie=VARCHAR
    shouji=VARCHAR
    yuanxi=VARCHAR
    banji=VARCHAR
    touxiang=VARCHAR
    '''
    class Meta:
        db_table = 'xuesheng'
        verbose_name = verbose_name_plural = '学生'
class yuanxiao(BaseModel):
    __doc__ = u'''yuanxiao'''
    __tablename__ = 'yuanxiao'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yuanxiaobianhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='院校编号' )
    yuanxiaomingcheng=models.CharField ( max_length=255,null=False, unique=False, verbose_name='院校名称' )
    yuanxiaoleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院校类型' )
    yuanxiaodizhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院校地址' )
    fuzeren=models.CharField ( max_length=255, null=True, unique=False, verbose_name='负责人' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    '''
    yuanxiaobianhao=VARCHAR
    yuanxiaomingcheng=VARCHAR
    yuanxiaoleixing=VARCHAR
    yuanxiaodizhi=VARCHAR
    fuzeren=VARCHAR
    lianxidianhua=VARCHAR
    '''
    class Meta:
        db_table = 'yuanxiao'
        verbose_name = verbose_name_plural = '院校'
class pinkunshenqing(BaseModel):
    __doc__ = u'''pinkunshenqing'''
    __tablename__ = 'pinkunshenqing'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    banji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='班级' )
    pinkundengji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='贫困等级' )
    jiatingqingkuang=models.TextField   (  null=True, unique=False, verbose_name='家庭情况' )
    shouruqingkuang=models.TextField   (  null=True, unique=False, verbose_name='收入情况' )
    zhengmingcailiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='证明材料' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    xuehao=VARCHAR
    xingming=VARCHAR
    banji=VARCHAR
    pinkundengji=VARCHAR
    jiatingqingkuang=Text
    shouruqingkuang=Text
    zhengmingcailiao=VARCHAR
    shenqingshijian=DateTime
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'pinkunshenqing'
        verbose_name = verbose_name_plural = '贫困申请'
class zizhuxiangmu(BaseModel):
    __doc__ = u'''zizhuxiangmu'''
    __tablename__ = 'zizhuxiangmu'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    xiangmujine=models.FloatField   (  null=True, unique=False, verbose_name='项目金额' )
    shenqingtiaojian=models.TextField   (  null=True, unique=False, verbose_name='申请条件' )
    xiangmujieshao=models.TextField   (  null=True, unique=False, verbose_name='项目介绍' )
    fabiaoshijian=models.DateField   (  null=True, unique=False, verbose_name='发表时间' )
    xiangmutupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目图片' )
    '''
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    xiangmujine=Float
    shenqingtiaojian=Text
    xiangmujieshao=Text
    fabiaoshijian=Date
    xiangmutupian=VARCHAR
    '''
    class Meta:
        db_table = 'zizhuxiangmu'
        verbose_name = verbose_name_plural = '资助项目'
class zizhushenqing(BaseModel):
    __doc__ = u'''zizhushenqing'''
    __tablename__ = 'zizhushenqing'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    xiangmujine=models.FloatField   (  null=True, unique=False, verbose_name='项目金额' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    shenqingcailiao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='申请材料' )
    shenqingshuoming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='申请说明' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    xiangmujine=Float
    shenqingshijian=DateTime
    shenqingcailiao=VARCHAR
    shenqingshuoming=VARCHAR
    xuehao=VARCHAR
    xingming=VARCHAR
    yuanxi=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'zizhushenqing'
        verbose_name = verbose_name_plural = '资助申请'
class zizhufafang(BaseModel):
    __doc__ = u'''zizhufafang'''
    __tablename__ = 'zizhufafang'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    xiangmumingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目名称' )
    xiangmuleixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='项目类型' )
    xiangmujine=models.FloatField   (  null=True, unique=False, verbose_name='项目金额' )
    fafangshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发放时间' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    '''
    xiangmumingcheng=VARCHAR
    xiangmuleixing=VARCHAR
    xiangmujine=Float
    fafangshijian=DateTime
    beizhu=VARCHAR
    xuehao=VARCHAR
    xingming=VARCHAR
    yuanxi=VARCHAR
    '''
    class Meta:
        db_table = 'zizhufafang'
        verbose_name = verbose_name_plural = '资助发放'
class qingongjianxue(BaseModel):
    __doc__ = u'''qingongjianxue'''
    __tablename__ = 'qingongjianxue'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    gangweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='岗位名称' )
    gangweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='岗位类型' )
    gongzuodidian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作地点' )
    gongzuoshijian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='工作时间' )
    xinzi=models.FloatField   (  null=True, unique=False, verbose_name='薪资' )
    gangweijieshao=models.TextField   (  null=True, unique=False, verbose_name='岗位介绍' )
    gangweitupian=models.CharField ( max_length=255, null=True, unique=False, verbose_name='岗位图片' )
    '''
    gangweimingcheng=VARCHAR
    gangweileixing=VARCHAR
    gongzuodidian=VARCHAR
    gongzuoshijian=VARCHAR
    xinzi=Float
    gangweijieshao=Text
    gangweitupian=VARCHAR
    '''
    class Meta:
        db_table = 'qingongjianxue'
        verbose_name = verbose_name_plural = '勤工俭学'
class gangweishenqing(BaseModel):
    __doc__ = u'''gangweishenqing'''
    __tablename__ = 'gangweishenqing'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    gangweimingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='岗位名称' )
    gangweileixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='岗位类型' )
    shenqingshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='申请时间' )
    shenqingshuoming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='申请说明' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    gangweimingcheng=VARCHAR
    gangweileixing=VARCHAR
    shenqingshijian=DateTime
    shenqingshuoming=VARCHAR
    xuehao=VARCHAR
    xingming=VARCHAR
    yuanxi=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'gangweishenqing'
        verbose_name = verbose_name_plural = '岗位申请'
class daikuanshenqing(BaseModel):
    __doc__ = u'''daikuanshenqing'''
    __tablename__ = 'daikuanshenqing'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='是'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    daikuanmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='贷款名称' )
    daikuanjine=models.FloatField   (  null=True, unique=False, verbose_name='贷款金额' )
    daikuanshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='贷款时间' )
    daikuanyuanyin=models.TextField   (  null=True, unique=False, verbose_name='贷款原因' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    sfsh=models.CharField ( max_length=255, null=True, unique=False,default='否', verbose_name='是否审核' )
    shhf=models.TextField   (  null=True, unique=False, verbose_name='审核回复' )
    '''
    daikuanmingcheng=VARCHAR
    daikuanjine=Float
    daikuanshijian=DateTime
    daikuanyuanyin=Text
    xuehao=VARCHAR
    xingming=VARCHAR
    yuanxi=VARCHAR
    sfsh=VARCHAR
    shhf=Text
    '''
    class Meta:
        db_table = 'daikuanshenqing'
        verbose_name = verbose_name_plural = '贷款申请'
class daikuanfafang(BaseModel):
    __doc__ = u'''daikuanfafang'''
    __tablename__ = 'daikuanfafang'



    __authTables__={'xuehao':'xuesheng',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    daikuanmingcheng=models.CharField ( max_length=255, null=True, unique=False, verbose_name='贷款名称' )
    daikuanjine=models.FloatField   (  null=True, unique=False, verbose_name='贷款金额' )
    fafangshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='发放时间' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    xuehao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='学号' )
    xingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='姓名' )
    yuanxi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='院系' )
    '''
    daikuanmingcheng=VARCHAR
    daikuanjine=Float
    fafangshijian=DateTime
    beizhu=VARCHAR
    xuehao=VARCHAR
    xingming=VARCHAR
    yuanxi=VARCHAR
    '''
    class Meta:
        db_table = 'daikuanfafang'
        verbose_name = verbose_name_plural = '贷款发放'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.CharField ( max_length=255,null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=VARCHAR
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '校园资讯'
