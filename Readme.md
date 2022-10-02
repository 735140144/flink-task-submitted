#这是一个FLink作业的提交小工具
#This is a Flink task submitted tool
##这个项目总共分为三部分，请认真阅读
##The project consists of three parts，please read it carefully
###1.服务端
###1.Server

###2.客户端
###2.Client

###3.通用设置 ☆
###3.General Settings☆

###1.server 服务端
你需要将以下几个文件放到你的服务器上

you should put the following files are on your server

####1.flinkcommitconf.py
####2.hdfsupload.py
####3.flinkcommitserver.py

在你执行脚本之前，你需要在flinkcommitconf.py中修改你的配置信息，之后你就可以运行服务端了
before you perform this script,you should set yourself conf in the flinkcommitserver.py,
then you can perform 

"nohup python3 flinkcommitserver.py &2>1 &"

###2.Client
你需要将以下这些文件放到一个文件夹中
you should put the following files in one dir

####1.flinkcommit.py
####2.flinkcommitconf.py
####3.flinkcommitdb.py
####4.flinkpost.py
####5.hdfsupload.py
之后在cmd或者终端中执行命令，当然你也可以加上最萌的图标
then you can perform in cmd or terminal 

"pyinstaller -F -w flinkcommit.py" or you can also add youself lovely icon with "-d xxx.ico"

###3.General Settings
####1.你需要一张配置表来存放你得flink任务的相关信息
####1.you need a schema to save your all flink job and some name in it;
你可以在数据库执行以下语句
you can perform this DDL in you database

create table flink_job
(
    id      bigint auto_increment
        primary key,
    jar     varchar(200) default '' not null comment 'jar',
    class   varchar(200) default '' not null comment 'classEntry',
    appname varchar(200) default '' not null comment 'appName',
    ckname  varchar(200) default '' not null comment 'checkpointName'
);

####2.你应该检查文件中所用到的所有的依赖是否具备
####2.you show check all the pyfiles to make sure you server have all the rely

##如果你的设置正确，那么你就可以拥有自己的Flink任务提交工具了
##If you setting is all right,you can use you own flink submit exe
