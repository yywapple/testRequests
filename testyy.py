import hashlib
mm=hashlib.md5()
sign_str='@admin123'
sign_bytes_utf8=sign_str.encode(encoding="utf-8")
mm.update(sign_bytes_utf8)
print(mm.hexdigest())
