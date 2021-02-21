from flask import Flask, jsonify, request
import re
app = Flask(__name__)



def add(content, filetoedit):
    open(filetoedit, "a").write(f"{content}\n")

def remove(rem, filetoedit):
    fileopened = open(filetoedit, "w+")
    my_string = fileopened.read()
    text = re.sub(".*"+rem+".*\n?","",my_string)
    fileopened.write(text)

def ipfunc(ip):
    f = open("Pinged\\First.txt", "r")
    first = f.read()
    s = open("Pinged\\Second.txt", "r")
    second = s.read()
    t = open("Pinged\\Third.txt", "r")
    third = t.read()
    if ip in first:
        remove(ip, "Pinged\\First.txt")
        add(ip, "Pinged\\Second.txt")
        return jsonify({"Pinged":"1 Time"}) 
    elif ip in second:
        remove(ip, "Pinged\\Second.txt")
        add(ip, "Pinged\\Third.txt")
        return jsonify({"Pinged":"2 Time"}) 
    elif ip in third:
        return jsonify({"Status":"Access Denied"})
    else:
        add(ip, "Pinged\\First.txt")
        return jsonify({"Status":"WoW, First Time."})


@app.route('/')
def firstuse():
    headers_list = request.headers.getlist("X-Forwarded-For")
    user_ip = headers_list[0] if headers_list else request.remote_addr
    return ipfunc(user_ip)

    
if __name__ == '__main__':
    app.run()