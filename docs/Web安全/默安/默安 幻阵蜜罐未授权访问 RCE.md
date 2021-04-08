# 默安 幻阵蜜罐未授权访问 RCE

## 漏洞描述

默安 幻阵蜜罐存在部署页面未授权访问 ，可执行任意命令

## 漏洞影响

> [!NOTE]
>
> 默安 幻阵蜜罐

## 漏洞复现

产品页面

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/1.png)

安装页面如下

默安 幻阵蜜罐![](resource/默安-幻阵蜜罐未授权访问-RCE/media/2.png)

刷新并抓包

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/3.png)

Drop掉 **/huanzhen/have_installed?**

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/4.png)

进入页面

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/5.png)

点击调试抓包

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/6.png)

执行其他命令

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/7.png)

点击一键诊断泄露 IP数据

![](resource/默安-幻阵蜜罐未授权访问-RCE/media/8.png)