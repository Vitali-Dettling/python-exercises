import json
import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    #
    # Once you've done this, return the name of the number 1 top artist in
    # Spain.




    payload = {'country': 'Spain'}
    # data = requests.re(method='GET', url='http://httpbin.org/get', kwargs=payload).text
    data =requests.get(url)
    print(data)

    data['topartists']['artist'][0]['name']

    dic = json.loads(data)
    print(dic)
    tes = dic['country']
    print(tes)

    # return the top artist in Spain
    return tes


api_get_request('http://www.last.fm/api/account/create')
