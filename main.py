import requests
from datetime import datetime
class ScoreGet:
    def __init__(self):
        self.url_get_all_matches="https://cricapi.com/api/matches"
        self.get_score= "https://cricapi.com/api/cricketScore"
        self.apikey = "RbOHylLS89SAhJVN78CVgWTqeHm2"
        self.unique_id = ""
    def get_unique_id(self):
        uri_params = {"apikey":self.apikey}
        request = requests.get(self.url_get_all_matches,params=uri_params)
        print(request.json())
        response = request.json()
        uni_found=0
        for i in response['matches']:
            if (i['team-1'] == 'England' or i['team-2'] == 'England') and (i['matchStarted']) and (i['squad']):
                #today = datetime.today().strftime('%Y-%m-%d')
                today = "2020-07-16"
                print(today)
                if today == i['date'].split('T')[0]:
                    print('yes')
                    self.unique_id = i['unique_id']
                    uni_found = 1
                    break
        if not uni_found:
            self.unique_id=-1;
        send_data  = self.get_score_current(self.unique_id)
        return (send_data)

    def get_score_current(self,unique_id):
        data=""
        if unique_id == -1:
            data = 'NO INDIA MATCHES'
        else:
            uri_params = {'apikey':self.apikey,'unique_id':unique_id}
            request = requests.get(self.get_score,params=uri_params)
            response = request.json()
            try:
                data = "Here's the score : \n "+response['stat']+"\n"+response['score']
            except KeyError as e:
                print(e)
        return data

if __name__ == "__main__":
    obj = ScoreGet()
    message = obj.get_unique_id()
    from twilio.rest import Client
    a_sid="AC961c7e922c579190addb30586941e778"
    auth_token = "4776478985f3029a019cf1a0b949d964"
    client = Client(a_sid,auth_token)
    m = client.messages.create(body=message,from_="whatsapp:+14155238886",to="whatsapp:+917303342255")
