import model.instaCrawling as mi

your_instagram_id = ""
your_instagram_pwd = ""
target_instagram_id = ["merumichandayo", "o10913", "yui___i__", "llty_yaya"]

id = mi.instagram(id = your_instagram_id,pwd = your_instagram_pwd,targets = target_instagram_id)
id.login()
id.getFollowers()