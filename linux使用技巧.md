### 1.ubuntu 使用技巧   

1. mkdir的技巧

    ```bash
    #创建 ～/a/b/c
    mkdir -p  ~/a/b/c/
    
    #创建多个文件夹
    mkdir  a b c
    ```

2. touch

    ```bash
    #创建文件
    
    touch a.txt
    
    #在绝对路径中创建文件
    
    touch /home/robot/myfile.txt
    ```

    

3. rm 删除

    ```bash
    #删除文件
    rm a.txt
    
    #删除文件夹
    rm -rf a或者 trash-put a  		#将文件移动到回收站 需安装trash-cli
    ```

    

4. cp 复制

    ```bash
    #复制文件夹到指定位置
    cp -r myfile/ /home/robot/
    ```

5. mv 移动或重命名文件

    ```bash
    #移动文件夹到指定位置
    mv myfile /home/robot
    
    #重命名文件夹
    mv myfile myfile01
    ```

    

6. man 查看linux命令手册

    ```bash
    #查看ls手册
    man ls	
    
    #查看帮助reboot 
    help cd	
    ```

7. reboot  重启linux系统

8. shutdown 立即关机

    ```bash
    # 立即关机
    shotdown -h now 
    ```

9. ctrl + - 缩小命令行字体大小，ctrl + shift + + 放大

10. ctrl + alt + T 在桌面快速启动终端

11. ls -lah    查看当前目录下所有文件详情

12. time  加执行文件，可以计时运行文件消耗时间

13. 查看ubuntu 挂载详情 df -h

14. pip 下载镜像源

     ```bash
     #使用方法：
     pip install requsets -i https://pypi.tuna.tsinghua.edu.cn/simple/ Scipy
     #镜像源列表：
     https://mirrors.aliyun.com/pypi/simple/ //阿里
     https://pypi.tuna.tsinghua.edu.cn/simple/ //清华
     https://pypi.douban.com/ //豆瓣
     https://pypi.hustunique.com/ //华中理工大学
     https://pypi.sdutlinux.org/ //山东理工大学
     https://pypi.mirrors.ustc.edu.cn/ //中国科学技术大学
     ```

     

15. ubuntu 系统命令行设置投屏显示 

    ```bash
    # 使用单显示屏---关闭笔记电脑屏幕（即主屏 LVDS-1不同笔记本可能不一样有eDP-1端口等）
    xrandr --output LVDS-1 --off  
    
    #扩展屏幕模式
    xrandr --output HDMI-1 --right-of LVDS-1 --auto
    
    # 切回主屏命令（或者直接合上笔记本再打开）
    xrandr --output LVDS-1 --auto
    ```

    

      [Ubuntu系统笔记本投屏显示器方法---参考](https://blog.csdn.net/qq_38863413/article/details/101454236)

16. 在linux中制作desktop快捷链接方式  

     ```bash
     #新建一个连接程序
     vim typora.desktop
     
     [DesktopEntry]
     Name=Typora
     #打开软件路径
     Exec=/opt/Typora/bin/Typora-linux-x64/Typora	
     #类型
     Type=Application	
     #图标位置
     Icon=opt/Typora/bin/Typora-linux-x64/resources/assets/iconicon_512x512.png	
     
     #将程序拷贝到目标地址
     cp typora.desktop /usr/share/applications/	
     
     #将可执行的程序链接到终端的可执行命令，即配置环境
     ln -s /home/robot/software/Typora/bin/Typora-linux-x64/Typora /usr/sbin/
     
     #更改可执行权限(在./Typora文件中)
     chown root.rootchrome-sandbox
     chmod 755 chrome-sandbox
     
     ```

     

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

        > #-o 编译选项来为将产生的可执行文件用指定文件名==(单一文件编译)==
        >
        > g++ test.o -o test
        >
        > 
        >
        > #==多目录多文件下编译实例如下：==
        >
        > g++ main.cpp src/swap.cpp -Iinclude -o main	----- 编译文件main.cpp swap.cpp ;		头文件(引用的 .h文件)indclude 	可执行文件 main
        
        

+ g++重要的编译参数

    + -g	编译带调试信息的可执行文件   

        > #带有调试的文件
        >
        > g++ -g text.cpp -o test

    + -O[数字]      优化源代码

        > ##优化即  例如省略代码中从未使用过的变量，直接将变量表达式用结果值代替等等，这些操作会缩减目标文件的所含的代码量，提高最终生成的可执行文件的运行效率。
        >
        > g++  test.cpp -O2 -o test

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
    
    
    
    ```bash
    #示例:
    g++ main.cpp src/Gun.cpp src/Soldier.cpp -Iinclude -o myexe -Wall -g -O2		//输出 警告 调试 优化代码
    ```
    
    
    
    
    
    

### 4.CMake 简要使用

#### 	**4.1 编译流程**

==在linux平台上CMake构建 C/C++工程的流程==: 

+ 编写CMakeListstxt
+ 执行命令cmake PATH 生成Makefile(PATH 是顶层CMakeLists.txt 所在目录)
+  执行命令make进行编译

#### 4.2 两种构建方式

+ 内部构建(in-source build): 会在同级目录下产生大量的中间文件，使工程文件杂乱无章

    ```bash
    # 内部构建
    # 在当前工程文件目录下，编译本目录的CMakeists.txt，生成Makefile和其他文件
    cmake .
    # 执行make命令，生成target
    make
    ```

    ==**简单的CMakeLists.txt编写如下：**==

    ```cmake
    # cmake最低版本要求
    cmake_minimum_required(VERSION 3.0)
    # 项目名称
    project(HELLOWORLD)
    # 编译.cpp文件生成可执行文件（如下：helloWorld_cmake）
    add_executable(helloWorld_cmake helloworld.cpp)
    ```

    

+ 外部构建(out-of -source build): 编译输出文件与工程文件不再同一目录下==(推荐使用)==

    ```bash
    ## 外部构建
    # 1.在当前目录下，创建一个build文件夹
    mkdir build
    # 2.进入到build文件夹中
    cd build
    # 3.编译上级目录的CMakeists.txt，生成Makefile和其他文件
    cmake ..
    # 4.执行make命令，生成target
    make
    ```

    ==**复杂多目录下构建CMakeLists.txt编写如下：**==

    ```cmake
    # cmake最低版本要求
    cmake_minimum_required(VERSION 3.0)
    # 项目名称
    project(SWAP)
    # 项目引用的头文件(.h文件)
    include_directories(include)
    # 编译多目录使用的.cpp文件生成可执行文件（如下：main_cmake）
    add_executable(main_cmake main.cpp src/swap.cpp )
    ```

#### 4.3 CMake编写CMakeLists.txt

##### 4.3.1 语法及注意事项

+ 基本语法格式：指令(参数1 参数2)

    + 参数使用==**括弧**==括起
    + 参数之间使用==**空格**==或==**分号**==分开

+ 指令不分大小写

    ```cmake
    # 添加到头文件搜索路径
    include_directories(include)
    INCLUDE_DIRECTORIES(include)
    ```

+ 变量是大小写相关的，使用**${}**方式**取值**。但在**if**语句中是直接使用变量名

    ```cmake
    # 设置一个变量HELLO，值是hello.cpp
    set(HELLO hello.cpp)  
    add_executable(hello main.cpp ${HELLO})
    ```

    

#####  4.3.2 常用变量

==cmake_c_flags==：gcc编译选项
==cmake_cxx_flags==：g++编译选项

```cmake
# 在cmake_cxx_flags编译选项后追加-std=c++14
set(cmake_cxx_flags "${cmake_cxx_flags} -std=c++14")
```

==cmake_build_type==：编译类型(Debug, Release)

```cmake
# 设定编译类型为debug，因为在调试时需要选择debug
set(cmake_build_type Debug)
# 设定编译类型为release，因为在发布时需要选择release
set(cmake_build_type release)
```

==executable_output_path==：可执行文件输出的存放路径

==library_output_path==：库文件输出的存放路径

​	

##### 4.3.3 重要指令

==cmake_minimum_required==：指定CMake的最小版本要求
语法：cmake_minimum_required(VERSION 版本号 [FATAL_ERROR])

```cmake
# CMake最小版本要求为3.0
cmake_minimum_required(VERSION 3.0)
```

==project==：定义工程名称，并可指定工程支持的语言
语法：project(工程名称 [CXX] [C] [java])

```cmake
# 指定工程名为HELLOWORLD
project(HELLOWORLD)
```

==set==：显式的定义变量
语法：set(变量名 [变量值] [CACHE TYPE DOCSTRING [FORCE]])

```cmake
# 定义SRC变量，其值为main.cpp hello.cpp
set(SRC sayhello.cpp hello.cpp)
```

==include_directories==：向工程添加多个特定的头文件搜索路径，相当于指定g++编译器的-I参数
语法：include_directories([AFTER|BEFORE][SYSTEM] dir1 dir2 ...)

```cmake
# 将/usr/include/myincludefolder 和 ./include 添加到头文件搜索路径
include_directories(/usr/include/myincludefolder ./include)
```

==link_directories==：向工程添加多个特定的库文件搜索路径，相当于指定g++编译器的-L参数
语法：link_directories(dir1 dir2 ...)

```cmake
# 将/usr/lib/mylibfolder 和 ./lib 添加到库文件搜索路径
link_directories(/usr/lib/mylibfolder ./lib)
```

==add_library==：生成库文件
语法：add_library(库名 [SHARED|STATIC|MODULE] [EXCLUDE_FROM_ALL] source1 source2 .. sourceN)

```cmake
# 通过变量 SRC 生成 libhello.so 共享库
# SHARED代表动态库，STATIC代表静态库
add_library(hello SHARED ${SRC})
```

==add_compile_options==：添加编译参数
语法：add_compile_options(编译参数)

```cmake
# 添加编译参数 -wall -std=c++11
add_compile_options(-wall -std=c++11 -o2)
```

==add_executable==：生成可执行文件
语法：add_executable(exe文件名 source1 source2 .. sourceN)

```cmake
# 编译main.cpp生成可执行文件main
add_executable(main main.cpp)
```

==target_link_libraries==：为target添加需要链接的共享库，相当于指定g++编译器-l参数
语法：target_link_libraries(target library1<debug|optimized> library2...)

```cmake
# 将hello动态库文件链接到可执行文件main
target_link_libraries(main hello)
```

==add_subdirectory==：向当前工程添加存放源文件的子目录，并可以指定中间二进制和目标二进制存放的位置
语法：add_subdirectory(source_dir [binary_dir] [EXCLUDE_FROM_ALL])

```cmake
# 添加src子目录，src中需要有一个CMakeLists.txt
add_subdirectory(src)
```

==aux_source_directory==：发现一个目录下所有的源代码文件并将列表存储在一个变量中，这个指令临时被用来自动构建源文件列表
语法：aux_source_directory(文件夹路径 变量名)

```cmake
# 定义SRC变量，其值为当前目录下所有的源代码文件
aux_source_directory(. SRC)
# 编译SRC变量所代表的源代码文件，生成main可执行文件
add_executable(main ${SRC})
```

**参考资料**：[CMake 资料](http://www.wang-hj.cn/?p=2629)

##### 4.3.4 Vscode 调试 C++代码

​	==(launch.json 和 tasks.json 文件配置)==

+ launch.json 配置

```c++
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "g++ - 生成和调试活动文件",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/build/main_cmake",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",     
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ],
            // "preLaunchTask": "build",
            "miDebuggerPath": "/usr/bin/gdb"
        }
    ]
}
```

+ tasks.json 配置

```c++
{
	"version": "2.0.0",		//声明最低cmake版本
	"options": {
		"cwd": "${workspaceFolder}/build"    //需要进入到我们执行build任务的文件夹中
	},
	"tasks": [    //tasks包含三个小任务
		{
			"type": "shell",
			"label": "cmake",    //第一个任务的名字叫cmake
			"command": "cmake",    //它要执行的命令是cmake
			"args": [
				".."    //参数是..
			]
		},
		{
			"label": "make",    //第二个任务的名字叫make
			"group": {
				"kind": "build",
				"isDefault": true
			},
			"command": "make",    //它要执行的命令是make
			"args": [
				
			]
		},
		{
			"label": "Build",    //第三个任务的名字叫Build
			"dependsOrder": "sequence",    //顺序执行依赖项
			"dependsOn":[    //依赖的两个项为cmake和make
				"cmake",    //即第一个任务的label
				"make"      //即第二个任务的label
			]
		}
	]
}

```



### 5.Vs code 高频使用快捷键  

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

### 6.Vim 常用快捷操作	

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
    + 常用插件
        + youcompleteme----代码补全
        + NEDRTree------树状目录结构

+ Vim 三种模式

    + 命令模式(Command mode)：启动时默认状态，可以执行移动、复制、删除等操作，不可编辑

    + 插入模式(Insert mode)：按 i 进入编辑模式，正常文本编辑

    + 底行模式(Last line mode)：执行保存、退出以及其他的一些功能。按下Shift+:即可进入底行模式

        

+ Vim键盘快捷键图示[链接](https://www.runoob.com/wp-content/uploads/2015/10/vi-vim-cheat-sheet-sch.gif)

<img src="/home/robot/图片/Vim键盘快捷键图示.gif" alt="Vim键盘快捷键图示" style="zoom: 80%;" />





### 7.算法题库



```python
# array 
https://leetcode.com/tag/array/

#string 
https://leetcode.com/tag/string/

#tree 
https://leetcode.com/tag/tree/ 

#linkedlist 
https://leetcode.com/tag/linked-list/

#math 
https://leetcode.com/tag/math/

# hexo主题
https://github.com/lh1me/hexo-theme-aomori
```

