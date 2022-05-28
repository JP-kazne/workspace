# Writeup

画像ファイルが与えられる。EXIFの中に何か情報がありそうなので調べてみると、フラグが分割されて埋め込まれていた。

```bash
$ file lake.jpg
lake.jpg: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, Exif Standard: [TIFF image data, big-endian, direntries=13, manufacturer=Apple, model=iPhone 6 Plus, orientation=upper-left, xresolution=190, yresolution=198, resolutionunit=2, software=12.4, datetime=2019:08:11 10:53:16], comment: "lot_of_metadata}", baseline, precision 8, 3264x2448, components 3

$ exiftool lake.jpg
ExifTool Version Number         : 11.88
File Name                       : lake.jpg
Directory                       : .
File Size                       : 676 kB
File Modification Date/Time     : 2022:05:14 19:10:55+09:00
File Access Date/Time           : 2022:05:14 19:16:04+09:00
File Inode Change Date/Time     : 2022:05:14 19:10:55+09:00
File Permissions                : rwxrwxrwx
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
Make                            : Apple
Camera Model Name               : iPhone 6 Plus
Orientation                     : Horizontal (normal)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Software                        : 12.4
Modify Date                     : 2019:08:11 10:53:16
Y Cb Cr Positioning             : Centered
Copyright                       : tjctf{thats_a_
Exposure Time                   : 1/520
F Number                        : 2.2
Exposure Program                : Program AE
ISO                             : 32
Exif Version                    : 0221
Date/Time Original              : 2019:08:11 10:53:16
Create Date                     : 2019:08:11 10:53:16
Components Configuration        : Y, Cb, Cr, -
Shutter Speed Value             : 1/520
Aperture Value                  : 2.2
Brightness Value                : 8.536677379
Exposure Compensation           : 0
Metering Mode                   : Multi-segment
Flash                           : Off, Did not fire
Focal Length                    : 4.2 mm
Subject Area                    : 1631 1223 1795 1077
Run Time Flags                  : Valid
Run Time Value                  : 82332424243958
Run Time Scale                  : 1000000000
Run Time Epoch                  : 0
Acceleration Vector             : -0.9713176498 0.05179892107 -0.1177288144
Sub Sec Time Original           : 172
Sub Sec Time Digitized          : 172
Flashpix Version                : 0100
Color Space                     : sRGB
Exif Image Width                : 3264
Exif Image Height               : 2448
Sensing Method                  : One-chip color area
Scene Type                      : Directly photographed
Exposure Mode                   : Auto
White Balance                   : Auto
Focal Length In 35mm Format     : 29 mm
Scene Capture Type              : Standard
Image Unique ID                 : c479d245731c693a0000000000000000
Lens Info                       : 4.15mm f/2.2
Lens Make                       : Apple
Lens Model                      : iPhone 6 Plus back camera 4.15mm f/2.2
GPS Version ID                  : 2.2.0.0
GPS Latitude Ref                : North
GPS Longitude Ref               : East
GPS Altitude Ref                : Above Sea Level
GPS Time Stamp                  : 02:53:16
GPS Speed Ref                   : km/h
GPS Speed                       : 3.029999971
GPS Img Direction Ref           : True North
GPS Img Direction               : 241.3239441
GPS Dest Bearing Ref            : True North
GPS Dest Bearing                : 241.3239441
GPS Date Stamp                  : 2019:08:11
GPS Horizontal Positioning Error: 5 m
Compression                     : JPEG (old-style)
Thumbnail Offset                : 2282
Thumbnail Length                : 4387
XMP Toolkit                     : XMP Core 5.5.0
Current IPTC Digest             : b443520a10119da99c2550175e6d0efb
Envelope Record Version         : 4
Coded Character Set             : UTF8
Application Record Version      : 4
IPTC Digest                     : b443520a10119da99c2550175e6d0efb
Comment                         : lot_of_metadata}
Image Width                     : 3264
Image Height                    : 2448
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Run Time Since Power Up         : 22:52:12
Aperture                        : 2.2
Image Size                      : 3264x2448
Megapixels                      : 8.0
Scale Factor To 35 mm Equivalent: 7.0
Shutter Speed                   : 1/520
Create Date                     : 2019:08:11 10:53:16.172
Date/Time Original              : 2019:08:11 10:53:16.172
Thumbnail Image                 : (Binary data 4387 bytes, use -b option to extract)
GPS Altitude                    : 848.7 m Above Sea Level
GPS Date/Time                   : 2019:08:11 02:53:16Z
GPS Latitude                    : 23 deg 51' 12.72" N
GPS Longitude                   : 120 deg 56' 14.64" E
Circle Of Confusion             : 0.004 mm
Field Of View                   : 63.7 deg
Focal Length                    : 4.2 mm (35 mm equivalent: 29.0 mm)
GPS Position                    : 23 deg 51' 12.72" N, 120 deg 56' 14.64" E
Hyperfocal Distance             : 1.82 m
Light Value                     : 12.9
```

<!-- tjctf{thats_a_lot_of_metadata} -->
