#CPT网站使用手册


<div id="category"></div>   

##1，基本信息
- Author：  Yunpeng Chen
- Contact： iamchenyp@gmail.com	
- Change log：
	- 2015.01.24 Initial version 

##2，用户说明
###2.1，用户分组
用户组 | 用户组说明
------|------
Guest | 非注册用户，只能访问网站首页
User  | 网站注册用户，只能访问纳新界面等有限功能
Member| 队员账户，可访问大多数功能 
Admin | 管理员，可使管理被授权的部分网站功能
SuperUser | 超级管理员，可以使用所有功能

###2.2，权限列表
权限名称 | 权限功能
------- |-------
contact Is member| 访问通讯录的队员权限
recruit Is manager | 管理纳新流程
task Is member  | 添加新任务，抢任务等
task Is manager | 任务分配权限


###2.3，用户授权
用户组 | 用户组授权
------|------
Guest | 无
User  | 无特殊权限，可访问纳新功能
Member| contact Is member<br>task Is member
Admin | recruit Is manager<br>task Is manager
SuperUser | 网站全部功能

**注：较高权限的用户组拥有较低权限用户组的所有权限


##3，网站功能简介
###3.1，用户注册
所有网站访问者可使用注册功能注册成为普通用户。从而进入纳新界面和查看首页信息。

###3.2，纳新
普通用户可以添加申请资料进入纳新流程。并在此界面实时查看当前申请状态。  
纳新管理员可以在此审核申请者资料，筛选进入下一环节的面试者，完成纳新相关的管理工作。

###3.3，通讯录
所有队伍成员可在此查看队员通讯录，并可编辑自己的资料与大家分享。

###3.4，任务布置
所有队伍成员可在此添加新任务，申请任务和跟踪任务进展。  
管理员可以管理任务状态，选择任务执行者。

##4，用户使用指南
###4.1，游客
[登陆网站首页](http://zjucpt.duapp.com)  
![首页](http://bcs.duapp.com/cptzju/用户手册图片/intro.png)
###4.2，普通注册用户组
[注册界面](http://zjucpt.duapp.com/register/)  
![注册](http://bcs.duapp.com/cptzju/用户手册图片/register.png)  
[登陆界面](http://zjucpt.duapp.com/login/)  
![登陆](http://bcs.duapp.com/cptzju/用户手册图片/login.png)  
登陆后  
![登陆后](http://bcs.duapp.com/cptzju/用户手册图片/afterlogin.png)  
[申请界面](http://zjucpt.duapp.com/join/)  
![申请](http://bcs.duapp.com/cptzju/用户手册图片/recruit.png)   
[填写个人资料](http://zjucpt.duapp.com/join/apply/)  
![申请表格](http://bcs.duapp.com/cptzju/用户手册图片/recruitform.png)  
[查询申请进度](http://zjucpt.duapp.com/join/)  
![申请进度](http://bcs.duapp.com/cptzju/用户手册图片/recruitprocess.png)  

###4.3，队员
####4.3.1，通讯录
队员权限需要管理员在管理界面授权。被分入Member用户组的用户有权访问通讯录界面。但想要将自己的信息加入到通讯录中，还需要在管理界面的Contact表中加入队员信息（目前只有管理员有权限将网站注册用户和队员编号绑定加入Contact表）。  
[通讯录](http://zjucpt.duapp.com/contact/)  
![通讯录界面](http://bcs.duapp.com/cptzju/用户手册图片/member/contact.png)  

####4.3.2，任务布置
具有队员权限的用户可以进入任务布置界面浏览当前任务信息，添加新任务以及申请和处理任务。  
[任务界面](http://zjucpt.duapp.com/task/)  
![任务界面](http://bcs.duapp.com/cptzju/用户手册图片/member/tasks.png)  

查看任务详情   
![任务详情](http://bcs.duapp.com/cptzju/用户手册图片/member/task_info.png)   

申请任务
![申请任务](http://bcs.duapp.com/cptzju/用户手册图片/member/task_apply.png)

###4.4，管理员
超级管理员可以在[管理界面](http://zjucpt.duapp.com/admin)中查看网站后台数据，亦可以对用户权限等进行管理。
####4.4.1，管理用户组  
![Admin](http://bcs.duapp.com/cptzju/用户手册图片/member/admin.png)
####4.4.2，管理网站分区
以纳新管理员为例，其有权进入纳新筛选管理界面。  
![纳新管理](http://bcs.duapp.com/cptzju/用户手册图片/member/recruit_manager.png)


<link rel="stylesheet" href="http://yandex.st/highlightjs/6.2/styles/googlecode.min.css">
<script src="http://code.jquery.com/jquery-1.7.2.min.js"></script>
<script src="http://yandex.st/highlightjs/6.2/highlight.min.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
<script type="text/javascript">
 $(document).ready(function(){
      $("h2,h3,h4,h5,h6").each(function(i,item){
        var tag = $(item).get(0).localName;
        $(item).attr("id","wow"+i);
        $("#category").append('<a class="new'+tag+'" href="#wow'+i+'">'+$(this).text()+'</a></br>');
        $(".newh2").css("margin-left",0);
        $(".newh3").css("margin-left",20);
        $(".newh4").css("margin-left",40);
        $(".newh5").css("margin-left",60);
        $(".newh6").css("margin-left",80);
      });
 });
</script>