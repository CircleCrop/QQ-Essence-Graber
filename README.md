# QQ Essence Graber

* 必须使用Python3，不兼容Python2
* 基于 Requests 库与 lxml 库 进行开发必须使用pip进行安装
## Install:

```bash
> pip install requests
> pip install lxml
```

## Usage:
1、将群号放入第30行<br>
2、将抓到的 cookie 放入到第40行 cookie 中即可。
> 打开 历史精华 时抓包

<br>如图所示，在配置好的情况下 使用以下方式即可获得精华消息
```bash
python essence.py [条数]
``` 
> 为了方便调用所以直接把图片的源地址进行输出
> 只需要判断下标0-9是否为"https://"

如果精华消息是文字图片的混合模式，图文顺序会保持一致

**Nodejs**
```nodejs
const execSync = require('child_process').execSync;
out = execSync('python3 ./essence.py '+1)).toString()
```
## connect
(Main Author)
<br>Discord：Time#4381
<br>QQ: 583416178
