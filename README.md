## 用于学习后端Python + 前端Vue+Vite作为后端编写的用户管理系统

#### 版本说明

版本一：编写完所有页面和API后，用于学习Vue页面的编写和API的调用  
版本二：在版本一的基础上增加路由，用于学习Vue路由相关的知识  
版本三：在版本二的基础打包和部署及CROS配置，用于学习Vue打包和部署相关知识  

#### 使用说明

安装Python环境

```bash
cd 项目根目录
pip install -r requirements.txt
```

安装前端环境

```bash
cd 项目根目录/web
npm install
```

运行Python后端

```bash
cd 项目根目录
python main.py
```

运行前端

```bash
cd 项目根目录/web
npm run dev
```

打开浏览器访问http://localhost:5173/

#### 版本一
![可视化](./assets/web_vis.png)

#### 版本二
![可视化](./assets/router.png)