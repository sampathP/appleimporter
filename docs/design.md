# Design Patterns
## exiftool execute patters

### For PNG files

 PNG files has different tag name for created date.
```
$ ./tools/Image-ExifTool-11.49/exiftool  -j -CreateDate -DateCreated 107APPLE/IMG_7999.PNG 
[{
  "SourceFile": "107APPLE/IMG_7999.PNG",
  "DateCreated": "2019:05:21 12:42:52"
}]
```

### For JPG, HEIC, MOV files
```
$ ./tools/Image-ExifTool-11.49/exiftool  -j -CreateDate 107APPLE/IMG_7052.HEIC
[{
  "SourceFile": "107APPLE/IMG_7052.HEIC",
  "CreateDate": "2019:01:09 11:47:49"
}]
```

## Image Convert Patterns

### User ImageMagic
HEIC file format is supported from Imagemagic version 6.9.7.4.
[Follow this to build imagemagic for old ubuntu systems.](
https://www.virment.com/install-latest-imagemagick-and-enable-heic/)
