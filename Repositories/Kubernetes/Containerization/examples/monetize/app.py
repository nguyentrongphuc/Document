import requests
from flask import Flask, render_template, jsonify
import json
app = Flask(__name__)

def get_response(file_name, timeout=6000, stream=True):
    #curl --data-binary @payload_web_cox_banner_native.json 'https://ib.adnxs.com/openrtb2?member_id=9557'
    with open('json/' + file_name) as user_file:
        file_contents = user_file.read()
    header = {}
    url = 'https://ib.adnxs.com/openrtb2?member_id=9557'  
    return requests.post(url=url, data=file_contents, timeout=timeout, stream=stream)

class Ad:
    title = None
    desc = None 
    sponsored = None 
    icon_url = None 
    img_url = None 
    click_tracker = None 
    impression_tracker = None
    display_url = None
    cta = None

    def format(self):
        return {
            'title' : self.title,
            'desc' : self.desc,
            'sponsored' : self.sponsored,
            'icon_url' : self.icon_url,
            'img_url' : self.img_url,
            'click_tracker' : self.click_tracker,
            'impression_tracker' : self.impression_tracker
        }
        
@app.route('/native')
def native():
    response = get_response('payload_web_cox_native.json')
    if response.status_code == 200:
        response_data = response.json()
        data = response_data["seatbid"][0]["bid"][0]["adm"]

        obj = json.loads(data)
        ad = Ad()
        for item in obj['assets']:
            if item['id'] == 99:
                ad.title = item['title']['text']
            elif item['id'] == 98:
                ad.icon_url = item['img']['url']
            elif item['id'] == 97:
                ad.img_url = item['img']['url']
            elif item['id'] == 1:
                ad.sponsored = item['data']['value']
            elif item['id'] == 2:
                ad.desc = item['data']['value']
            elif item['id'] == 11:
                ad.display_url = item['data']['value']
            elif item['id'] == 12:
                ad.cta = item['data']['value']

        ad.click_tracker = obj['link']['url']
        ad.impression_tracker = obj['imptrackers'][0]

        print ('icon: ' + ad.icon_url)
        return render_template('native.html', data=ad);
    
    return 'NO Bidding'

@app.route('/request')
def request():
    with open('json/payload_web_cox_native.json') as user_file:
        file_contents = user_file.read()
    #file_contents = file_contents.replace('\\', '')
    obj = json.loads( file_contents)
    print('ssss')
    
    return json.loads(obj['imp'][0]['native']['request'])

@app.route('/response')
def response():
    response = get_response('payload_web_cox_native.json')
    if response.status_code == 200:
        response_data = response.json()
        data = response_data["seatbid"][0]["bid"][0]["adm"]
        
        return json.loads(data)
    
    return 'NO Bidding'

@app.route('/')
def homepage():
    return 'Hello, World from Flask!\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
