代码几乎是重写的，我对代码的架构进行了一些调整：
1./bin目录用于存放二进制程序，rcrack的执行文件我就放在了这个目录下，我现在将他的名字改为digdata；
2./dic用于存放哈希字典文件，直接copy进去就能用，不过要注意，字典在使用前需要进行sort；
3.我将主要代码都放在了/lib目录下的utils.py文件中了，不同的功能封装在不同的类中了，日后不会出现代码难以维护的问题；
4.我写了一个日志接口：fileoperator.write_log("logstr")，用来记录程序的运行状态及运行过程,这个接口对调试会非常有用，只需要填写需要输出的字符串，日志记录就会添加到/log目录下的runtimelog.log文件中；
5.famer.py文件的接口名字我进行了修改，你在联调时需要进行相应调整。ask_db(data_list,data_type)接口的返回值格式调整为：weak_list,weak_type_list,strong_list,len(unknown_list)
6.md5.data和sha1.data文件是测试是使用的数据，正式部署时可以删除；
7.我在famer.py中增加了一个接口，用于检查hashlist的类型，建议在执行命令前进行一次检查，接口函数为：test_hash_type(data_list)，返回值为：is_md5,is_sha1
8.另外，建议给ubuntu的server端装一个图形界面，上次的bug多数是命令行下改出来的。
9.信息外网的服务器要尽快启动，并启动向日葵服务器控制端，我这里现在连不上，没有办法进行字典调试。
10.我写了一个导入topN的接口：append_knowledge(data_list)，输入为明文列表，调用后分别在md5table、sha1table中增加knowledge记录。你可以在界面上增加一个添加自定义的列表功能，这样可以方便用户进行灵活自定制。
11.数据库的数据结构我导出到/db目录下了，你在部署的时候直接导入到数据库中就行了，倒入后注意修改数据库连接认证信息。

12.happy life everyday！
