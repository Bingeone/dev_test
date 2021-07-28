1. 在linux中制作desktop快捷链接方式

     

    > vim typora.desktop    # 新建一个连接程序
    >
    > [Desktop Entry]
    > Name=Typora
    > Exec=/opt/Typora/bin/Typora-linux-x64/Typora	# 打开软件路径
    > Type=Application	# 类型
    > Icon=opt/Typora/bin/Typora-linux-x64/resources/assets/iconicon_512x512.png	# 图标位置
    >
    > cp typora.desktop /usr/share/applications/	# 将程序拷贝到目标地址

    > #将可执行的程序链接到终端的可执行命令，即配置环境
    >
    > ln -s /home/robot/software/Typora/bin/Typora-linux-x64/Typora   /usr/sbin/
    >
    > #更改可执行权限  (在./Typora文件中)
    >
    > chown root.root chrome-sandbox
    > chmod 755 chrome-sandbox

2. mkdir的技巧

    > #创建 ～/a/b/c
    >
    > mkdir -p  ~/a/b/c/
    >
    > #创建多个文件夹
    >
    > mkdir  a b c

3. touch

    > #创建文件
    >
    > touch a.txt
    >
    > #在绝对路径中创建文件
    >
    > touch /home/robot/myfile.txt

4. rm 删除

    > #删除文件
    >
    > rm a.txt
    >
    > #删除文件夹
    >
    > rm -rf a
    >
    > 或者 trash-put a  		#将文件移动到回收站 需安装trash-cli

5. cp 复制

    > #复制文件夹到指定位置
    >
    > cp -r myfile/ /home/robot/

6. mv 移动或重命名文件

    > #移动文件夹到指定位置
    >
    > mv myfile /home/robot
    >
    > #重命名文件夹
    >
    > mv myfile myfile01

7. man 查看linux命令手册

    >man ls	#查看ls手册
    >
    >help cd	#查看帮助reboot 

8. reboot  重启linux系统

9. shutdown 立即关机

    > shotdown -h now 立即关机

10.  ctrl + - 缩小命令行字体大小，ctrl + shift + + 放大

11. ctrl + alt + T 在桌面快速启动终端

12. ls -lah    查看当前目录下所有文件详情

13. time  加执行文件，可以计时运行文件消耗时间

14. ubuntu 系统命令行设置投屏显示 

     > ```bash
     > # 使用单显示屏---关闭笔记电脑屏幕（即主屏 LVDS-1不同笔记本可能不一样有eDP-1端口等）
     > xrandr --output LVDS-1 --off  
     > #扩展屏幕模式
     > xrandr --output HDMI-1 --right-of LVDS-1 --auto
     > # 切回主屏命令（或者直接合上笔记本再打开）
     > xrandr --output LVDS-1 --auto
     > 
     > ```

     [Ubuntu系统笔记本投屏显示器方法---参考](https://blog.csdn.net/qq_38863413/article/details/101454236)

### 2.文本编辑器    

+ vi/vim
    + end/home  尾部首部
    + :%  s/8000/8900/g   全局替换
    + /str  全局查找字符串
    + x / del   删除（在普通模式下）
    + yy/p  复制当前行/粘贴下一行
    + dd  删除当前行
    + w/b  按词移动光标
    + 1gg  定位到第一行
    + u   后退撤销
+ gedit
+ nano

+ 常用文本工具命令

    | 命令 | 用途                   |
    | ---- | ---------------------- |
    | echo | 屏幕打印与文本输出     |
    | cat  | 合并文件或查看文件内容 |
    | tail | 显示文件内容的尾部     |
    | grep | 文本过滤工具           |

    > echo "hello"   	# 打印文本内容
    >
    > #将内容写入txt文件中
    >
    > echo "hello,world">hello.txt

    

### 3.GCC编译器

+ 使用gcc编译C代码

+ 使用g++ 编译C++代码

+ man gcc/g++  查看使用手册

+ 编译过程

    1. **预处理-Pre-Proccessing          # .i文件**

        > #-E 选项指示编译器仅对输入文件进行预处理
        >
        > g++ -E test.cpp -o test.i		// .i文件

    2. **编译-Compiling           #.s文件**

        > #-s 编译选项告诉 g++ 在为C++ 代码产生了汇编语言文件后停止编译
        >
        > #g++ 产生的汇编语言文件的缺省扩展名是 .s
        >
        > g++ -S test.i -o test.s

    3. **汇编-Assembling        # .o文件**

        > #-c  选项告诉 g++ 仅把源代码编译为机器语言的目标代码
        >
        > g++ -c test.s -o test.o

    4. **链接-Linking       #bin文件**

        > #-o 编译选项来为将产生的可执行文件用指定文件名
        >
        > g++ test.o -o test

+ g++重要的编译参数

    + -g	编译带调试信息的可执行文件   

        > #带有调试的文件
        >
        > g++ -g text.cpp -o test

    + -0[数字]      优化源代码

        > ##优化即  例如省略代码中从未使用过的变量，直接将变量表达式用结果值代替等等，这些操作会缩减目标文件的所含的代码量，提高最终生成的可执行文件的运行效率。
        >
        > g++  test.cpp -02 -o test

    + -I       指定头文件搜索目录

        > g++  -I/myinclude(路径) test.cpp

    + -Wall   打印警告信息

        > #打印出gcc提供的警告信息
        >
        > g++ -Wall test.cpp 

    + -w   关闭警告信息

        > g++ -w test.cpp

    + -o    输出文件头名

        > g++ test.cpp -o test

    + -std=c++11   设置编译标准

        > g++  -std=c++11 test.cpp 

### 4.Vs code 高频使用快捷键  

| 功能                 | 快捷键               | 功能                 | 快捷键                            |
| -------------------- | -------------------- | -------------------- | --------------------------------- |
| 文件检索             | ctrl + p             | 关闭文件             | ctrl + w                          |
| 打开命令面板         | ctrl + shift + p     | 当前行上下移动       | alt+Up/Down                       |
| 打开终端             | ctrl + `             | 变量名统一命名       | F2                                |
| 关闭侧边栏           | ctrl + B             | 转到变量定义处       | F12                               |
| 复制文本             | ctrl + c             | 保存文本             | ctrl + s                          |
| 粘贴文本             | ctrl + v             | 撤销操作             | ctrl + z                          |
| 删除当前行           | ctrl + d（自定义）   | 代码格式化           | ctrl +shift + i（Format Document) |
| 在当前行向下插入一行 | ctrl + enter         | 光标移到行首/行尾    | home/end                          |
| 在当前行向上插入一行 | ctrl + shift + enter | 根据单词快速移动光标 | ctrl + 左右方向键                 |
| 查找/替换            | ctrl+F/ctrl +H       | 单词小写转大写       | shift + q（自定义）               |
| 全屏                 | F11                  | 单词大写转小写       | shift + w（自定义）               |
| 空间大小缩放         | ctrl + +/-           | 编辑区大小缩放       | ctrl + 鼠标滚轮                   |

### 5.Vim 常用快捷操作	

| 功能(命令模式下) | 快捷键                          | 功能(命令模式下)                       | 快捷键   |
| ---------------- | ------------------------------- | -------------------------------------- | -------- |
| 上下左右移动     | h/j/k/l(方向键)                 | 插入(编辑模式)                         | i        |
| 删除/剪切当前行  | dd                              | 按词向后移动                           | w        |
| 复制当前行       | yy                              | 按词向前移动                           | b        |
| 粘贴(向下)       | p                               | 选中当前行                             | V        |
| 撤销             | u                               | 上一页                                 | ctrl + b |
| 反撤销           | ctrl + r                        | 下一页                                 | ctrl + f |
| 回到首端         | gg / home                       | 重复上一次命令                         | `        |
| 回到尾端         | G / end                         | 删除当前字符                           | x        |
| 全局替换         | :% s/要替内容/内容/g            | 在查找str选中下，向下移动光标定位到str | n        |
| 局部替换         | :开始行,结束行s/要替换内容/内容 | 在查找str选中下，向上移动光标定位到str | N        |
| 定位指定行       | 数字+gg                         |                                        |          |
| 搜索内容         | :/内容                          |                                        |          |
| 自动补全         | ctrl + n (Vim默认)              |                                        |          |
| 删除当前行       | cc                              |                                        |          |

+ 保存文件并退出------ :wq!		# 感叹号

+ 退出不保存------ :q 

+ 模式切换--------- esc

+ Vim 插件下载官网（演示：插件管理器Vundle.vim ,不同管理器下载、卸载方式有差异）----- [Vim Awesome](https://vimawesome.com/plugin/youcompleteme)

    + 在命令模式下，输入: PluginInstall  下载插件(前提：在./vimrc 文件中添加插件名称)
    + 输入：PluginClean 卸载插件(前提：在./vimrc 文件中删除插件或注释)

+ Vim 三种模式

    + 命令模式(Command mode)：启动时默认状态，可以执行移动、复制、删除等操作，不可编辑

    + 插入模式(Insert mode)：按 i 进入编辑模式，正常文本编辑

    + 底行模式(Last line mode)：执行保存、退出以及其他的一些功能。按下Shift+:即可进入底行模式

        

+ Vim键盘快捷键图示[链接](https://www.runoob.com/wp-content/uploads/2015/10/vi-vim-cheat-sheet-sch.gif)

<img src="/home/robot/图片/Vim键盘快捷键图示.gif" alt="Vim键盘快捷键图示" style="zoom: 80%;" />

