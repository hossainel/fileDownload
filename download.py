import os
import requests

def download(url):#{
    response = requests.get(url, stream=True)
    print(response.status_code)
    if response.status_code==200:#{
        g = url.split('/')[0]
        l = url.split('/')[-1]
        if not os.path.exists(g):#{
            os.makedirs(g)
        #}
        with open(g+'/'+l, 'wb') as f:#{
            for chunk in response.iter_content(chunk_size=8192):#{
                f.write(chunk)
            #}
            f.close()
        #}
        print('Download Successful. Size: ',os.path.getsize(g+'/'+r+'/'+r2+l))
    #}
    else:#{
        print('Download Successful. Size: ',os.path.getsize(g+'/'+r+'/'+r2+l))
    #}
#}
