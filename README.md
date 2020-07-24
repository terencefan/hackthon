# hackthon

## Run docker image

```bash
docker run --publish 7020:7020 stdrickforce/hackthon:latest
```

## APIs

For image recognization:

```bash
curl --location --request POST 'localhost:7020/image' \
--header 'Content-Type: image/jpeg' \
--data-binary '@/C:/Users/tefa/Pictures/1.jpg'
```

For barcode recognization:

```bash
curl --location --request POST 'localhost:7020/barcode' \
--header 'Content-Type: application/json' \
--data-raw '123456789'
```

## GOOD LUCK!