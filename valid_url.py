url = "https://devxmanan.vercel.app"

if (url.startswith("https://") or url.startswith("http://")) and (url.endswith(".app") or url.endswith(".com")):
    print("Valid URL")
else:
    print("Invalid URL")
    