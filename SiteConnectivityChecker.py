import requests
import matplotlib.pyplot as plt     

def connect(url):
    try:
        #the required first parameter of the 'get' method is the 'url':
        uri = requests.get(url, timeout=15)
        uri.raise_for_status()
        rt=round((uri.elapsed.total_seconds()),2)
        #print the response (the content of the requested file):
        print('Status Code - '+ str(uri.status_code) + ' , Resp Time - ' + str(rt))
        return rt
    except requests.exceptions.HTTPError as err01:
        print ("HTTP error: ", err01)
    except requests.exceptions.ConnectionError as err02:
        print ("Error connecting: ", err02)
    except requests.exceptions.Timeout as err03:
        print ("Timeout error:", err03)
    except requests.exceptions.RequestException as err04:
        print ("Error: ", err04)
    

def main():
    sum=0
    x = []
    y = []
    plt.xlabel('Iteration')
    plt.ylabel('Response time in secs')
    url=input('Enter URL  ')
    plt.title(url) 
    for i in range (10):
        rt = connect(url)
        sum=sum+rt
        x.append(i)
        y.append(rt)
    print('Average Response time (in secs) for ' + str (i+1) + ' iterations - ' + str(round(sum/i,2)))
    plt.plot(x, y)
    plt.show()
if __name__ == '__main__':
    main()
