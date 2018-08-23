# Zhengjim - 漏洞复现

利用[Vulhub](https://github.com/vulhub/vulhub)一个面向大众的开源漏洞靶场，来搭建漏洞环境




## 漏洞

 1. [S2-057命令执行漏洞][1]
    
    ### *影响面*

    确定CVE-2018-11776为高危漏洞。
    实际场景中存在一定局限性，需要满足一定条件。

    ### *影响版本*
    
    Struts 2.3 to 2.3.34
    Struts 2.5 to 2.5.16

    ### *修复版本*
    
    Struts 2.3.35
    Struts 2.5.17
    
 2. ghostscript命令执行


  [1]: https://github.com/zhengjim/loophole/tree/master/S2-057
