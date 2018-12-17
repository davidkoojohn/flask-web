
## 认证方案使用的个包。
- Flask-Login: 管理已登录用户的用户会话。
- Werkzeug: 计算密码散列值并进行核对。
- itsdangerous: 生成并核对加密安全令牌。

##  除了认证相关的包之外，本章还用到如下常规用途的扩展。
- Flask-Mail: 发送与认证相关的电子邮件。
- Flask-Bootstrap: HTML 模板。
- Flask-WTF: Web 表单。

1. Werkzeug 实现密码散列.`generate_password_hash, check_password_hash`
2. Flask-Login
