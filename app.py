from flask import Flask, request, jsonify, send_file
import time
import imgGen_local

running_flag = False

app = Flask(__name__)
@app.route('/api', methods=['GET'])
def api():
    return jsonify(imgGen_local.txt_get())

@app.route('/jiegua/<param1>/<param2>')
def some_endpoint(param1, param2):
    imgGen_local.local_draw(240, 240, 16, 11, 20, (param1, param2))
    return send_file("img/output_s.jpg", mimetype='image/jpeg', as_attachment=False)

@app.route('/local', methods=['GET'])
def local_draw_api():
    imgGen_local.local_draw(240, 240, 16, 11, 20)
    return send_file("img/output_s.jpg", mimetype='image/jpeg', as_attachment=False)


@app.route('/small')
def get_image():
    if running_flag:
        while running_flag:
            time.sleep(1)
        imgGen_local.small_draw(240, 240, 13, 8, 16)
        return send_file("img/output_s.jpg", mimetype='image/jpeg', as_attachment=False)
    else:
        imgGen_local.small_draw(240, 240, 13, 8, 16)
        return send_file("img/output_s.jpg", mimetype='image/jpeg', as_attachment=False)

@app.route('/image')
def get_image2():
    if running_flag:
        while running_flag:
            time.sleep(1)
        imgGen_local.test_draw(480, 480, 20)
        return send_file("img/output.jpg", mimetype='image/jpeg', as_attachment=False)
    else:
        imgGen_local.test_draw(480, 480, 20)
        return send_file("img/output.jpg", mimetype='image/jpeg', as_attachment=False)

if __name__ == '__main__':
    #ret = suan_fa_yj.suan_yi_gua()
    #local_draw(240, 240, 16, 11, 20, (ret[0][2:], ret[1]))
    app.run(host='0.0.0.0', port=80, debug = True, threaded = True)