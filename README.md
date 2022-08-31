

- [免责声明](#免责声明)
- [部署在个人pc上](#部署在个人pc上)
- [部署在linux服务器上：](#部署在linux服务器上)
- [设置定时任务](#设置定时任务)
  - [windows：](#windows)
  - [macos&&linux：](#macoslinux)

### 免责声明
本项目仅用于学习交流！！！
代码写的很烂，别喷，你指望一个写了一小时多的脚本能把代码写出花来？
请认真如实填报健康情况！！！！



### 部署在个人pc上

* 1.安装chrome浏览器，并查看对应的浏览器版本，自行完成。
* 2.官网下载chromedriver  https://chromedriver.chromium.org/ 对应操作系统版本，会得到一个chromedriver，记住它的pwd（文件路径）
* 3.在auto_check.py中修改第20行的第一个参数，为步骤2中的pwd
* 4.设置定时任务（这块单独讲一下）


### 部署在linux服务器上：
* 1.参考此篇文章：
linux服务器ubuntu中安装chrome浏览器及配置selenium依赖环境
https://blog.csdn.net/weixin_42649856/article/details/103275162
* 同部署在个人pc的方法中的步骤2、3、4


### 设置定时任务
本质都是cmd中运行python文件
#### windows：
windows 定时执行python脚本
https://www.cnblogs.com/sui776265233/p/13602893.html

#### macos&&linux：
crontab -e编辑定时任务：
```bash
30 7/24 * * * * /usr/bin/python3 /path/to/app.py
```

其中，30 7/24 * * * 表示定时任务的运行时间规则为每日的 7:30 执行程序打卡；/path/to/app.py 表示 app.py 的完整路径，最好写死账号密码在脚本里


