
import zlib, sys

str_object1 = open('/Users/x/PycharmProjects/SmartNinja-Web1a/23_API-vreme/.git/objects/15/f896494441f80d682ffce6363786885c710f53', 'rb').read()
f = zlib.decompress(str_object1)

print f