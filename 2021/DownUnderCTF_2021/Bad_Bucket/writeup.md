# Writeup

https://storage.googleapis.com/the-bad-bucket-ductf/index.html にアクセスする。

`storage.googleapis.com`では、APIを利用して、bucketにあるオブジェクトを参照できる。

[参考]

* https://qiita.com/XPT60/items/2d362af37a64b6418d0as

https://storage.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o にアクセスすると`buckets/.notaflag`というオブジェクトがあることが分かった。

```
{
  "kind": "storage#objects",
  "items": [
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/buckets/.notaflag/1631512648813277",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/buckets%2F.notaflag",
      "mediaLink": "https://storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/buckets%2F.notaflag?generation=1631512648813277&alt=media",
      "name": "buckets/.notaflag",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648813277",
      "metageneration": "1",
      "contentType": "text/plain; charset=utf-8",
      "storageClass": "STANDARD",
      "size": "158",
      "md5Hash": "1mwb5duT97D9emOwH0q+sQ==",
      "crc32c": "bw5j5g==",
      "etag": "CN2VhJ+i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.814Z",
      "updated": "2021-09-13T05:57:28.814Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.814Z"
    },
```

https://storage.googleapis.com/the-bad-bucket-ductf/buckets/.notaflag を見てみると、フラグが書かれていた。

<!-- DUCTF{if_you_are_beggining_your_cloud_journey_goodluck!} -->
