# Writeup

`docker.hub`のページからイメージをpullして、コンテナを立ち上げる。

```bash
$ docker pull wanictf21spring/nginx_on_ubuntu

$ docker run wanictf21spring/nginx_on_ubuntu

$ docker ps
CONTAINER ID        IMAGE                             COMMAND                  CREATED             STATUS              PORTS               NAMES
a603af8b14be        wanictf21spring/nginx_on_ubuntu   "/usr/sbin/nginx -g …"   22 minutes ago      Up 22 minutes       80/tcp              compassionate_einstein

$ docker exec -it compassionate_einstein bash
```

コンテナ内でファイルを探すと`Flag.txt`が見つかった。

```bash
$ find ./ -type f -name "*.txt"
./var/www/html/Flag.txt

$ cat html/Flag.txt
FLAG{y0u_
```

`.git`も見つかったのでgitを使えるようにする。

```
apt install git
```

branchやcommit logを調べて`Flag.txt`の中身を見ていく。

```bash
$ git branch
* master
  temporary

$ git checkout temporary

$ cat html/Flag.txt 
4r3_p3rf3c7_g1t

$ git log --oneline
1b5bfaf (HEAD -> temporary) edit Flag.txt
6cc0b29 edit Flag.txt
b416014 Flag.txt
a2fed4a initialization of html/assets/*
f007f26 initialization of html/favicon.ico
e4c9da8 initialization of html/index.html
058a502 initialization of docker-compose.yml
1fc314c initialization of Dockerfile

$ git diff b416014
diff --git a/html/Flag.txt b/html/Flag.txt
index ef189e0..f99f791 100644
--- a/html/Flag.txt
+++ b/html/Flag.txt
@@ -1 +1 @@
-_m45t3r}
+4r3_p3rf3c7_g1t
```

すべてつなぎ合わせると`FLAG{y0u_4r3_p3rf3c7_g1t_m45t3r}`となる。

<!-- FLAG{y0u_4r3_p3rf3c7_g1t_m45t3r} -->
