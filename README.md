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
    
 2. [ghostscript命令执行][2]
 
    ### *影响面*

    GhostScript 的安全沙箱可以被绕过，通过构造恶意的图片内容，将可以造成命令执行、文件读取、文件删除等漏洞

    ### *影响版本*
    
    version <= 9.23（全版本、全平台）

    ### *修复版本*
    
    官方未出缓解措施，最新版本受到影响。


  [1]: https://github.com/zhengjim/loophole/tree/master/S2-057
  [2]: https://github.com/zhengjim/loophole/tree/master/ghostscript
