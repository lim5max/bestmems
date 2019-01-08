def b():
    from time import sleep
    import os

    import urllib3
    import requests
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    def thebiggest():

        allgroups = {
            'groups' : [
                {
                  'name' : 'mdk',
                  'id': '-57846937'
                },

                {'name' : 'borsh',
                  'id': '-460389'
          },
           ]
        }
        lengr = len(allgroups['groups'] )

        for m in range(lengr):
            ut = allgroups['groups'][m]['id']
        sss=[]
        
        for m in range(lengr):
                

                ut =  allgroups['groups'][m]['id']
                hh =  allgroups['groups'][m]['name']

                print(ut)
                 
                s = []
                try:
                    r = requests.get('https://api.vk.com/method/wall.get?', params={'owner_id': ut, 'count': '100', 'access_token': 'c85ac67f35af2b1113a812366a9b8f1580ad9d94ce346943777f083958b1b33625b528f9041f51c5b663c', 'v': '5.92'}, verify=False)
                    h = r.json()['response']
                    s.append(h)
                except:
                    print('api error')

                for i in range(len(s)):
                     for name in h['items']:
                       try:
                           likes = name['likes']['count']
                           views = name['views']['count']
                           itog = views // likes

                       except:

                           print('0')


                      
                       if (2<= itog <= 27):
                            jjjjj = {
                                'grip':  hh,
                                'id': name['id'],
                                'idg': ut
                            }
                            sss.append(jjjjj)
        return sss
    vv = thebiggest()

    print(vv)
    def best():
        c = 0
        d = []

        for i in range(len(vv)):
            g =  str(vv[i]['idg'])+'_'+str(vv[i]['id'])
            print(g)

            try:
                r = requests.get('https://api.vk.com/method/wall.getById?', params={'posts': g, 'access_token': 'c85ac67f35af2b1113a812366a9b8f1580ad9d94ce346943777f083958b1b33625b528f9041f51c5b663c','v': '5.92'}, verify=False)
                s = []
                h = r.json()['response']
                s.append(h)        
            except:
                print('')
            
            print(s)
            for name in s:

                for b in name:


                     if ((b['attachments'][0]['type']) == 'photo'):
                        img = 'static/img/img' + str(c) + '.jpg'
                        d.append(img)
                        p = requests.get(b['attachments'][0]['photo']['sizes'][6]['url'])
                        out = open(img, "wb")
                        out.write(p.content)

                        out.close()
                        c = c + 1


        h = {
            'kol': c ,
            'array': d
        }
        return  h

    n = best()
    c = n['kol']
    b= n['array']
    print(c)
    # -*- coding: utf8 -*-
    import json

    name="/static/hjjjj.json"
    file = open(name, mode="w", encoding="Latin-1")
    pl = {
        'enter': [ c , b]
    }
    m=[]
    m.append(pl)
    json.dump(m, file)
    file.close()
    name = '/static/hjjjj.json'
    bv = open(name, mode="r", encoding="Latin-1")
    json_d = json.load(bv)
    for us in json_d:
        for i in us['enter'][1]:
          print(us['enter'] )


    import os

    def fcount(path):
        """ Counts the number of files in a directory """
        count = 0
        for f in os.listdir(path):
            if os.path.isfile(os.path.join(path, f)):
                count += 1

        return count
    h = fcount('static/img/.')
    print(h)
    if h!= pl['enter'][0]:
        u = pl['enter'][0]

        try:

            import glob
            f = glob.glob("static/img/*.jpg")
            print(f)
            while u <= h:
                os.remove(f[u])
                u = u + 1
        except:
            pass
 
import schedule
import time



schedule.every(1).minutes.do(b)



while True:
    schedule.run_pending()
    time.sleep(1)


