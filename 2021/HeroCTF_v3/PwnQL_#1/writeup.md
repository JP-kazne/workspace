# Writeup

ページのソースを見ると

```
<!-- Hello dev, do not forget to remove login.php.bak before committing your code. -->
```

という記述があるので、http://chall1.heroctf.fr:8080/login.php.bak にアクセスすると、phpのソースコードが得られる。

```
$sql = "SELECT * FROM users WHERE username = :username AND password LIKE :password;";
```

が実行されることが分かる。`password`はLIKE句内にあるので、ワイルドカードである`%`を指定するとログインできる。

```
username = admin
password = %
```

<!-- Hero{pwnQL_b4sic_0ne_129835} -->