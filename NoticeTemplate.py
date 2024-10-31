# 普通模板
def normalTemplate():
    content = """
🐶 今日：{total_today}🫘，可用：{avail_today}🫘
"""
    return content

# Html模板
def htmlTemplate():
    content = ""
    return content

# markdown模板
def markdownTemplate():
    content = """{content}---
**数据日期:**
```
{date}
```
**今日总收益:**
```
{total_today}
```
**总可用积分:**
```
{avail_today}
```
**绑定账户:**
```
{account}
```
**设备总数:**
```
{devicesCount}
```
**设备信息如下:**
- ***
{detail}
- ***"""
    return content
