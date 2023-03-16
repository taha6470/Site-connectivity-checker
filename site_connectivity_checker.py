#import urllib
#use urlib.request to get data from the url
#write a function that takes a url 
#write a response
import urllib.request as urllib
def main(url):
    print("Checking connectivity")
    response=urllib.urlopen(url)
    print("Connected to url successfully")
    print("The responce code was :",response.getcode())

print("This is a site connectivity checker program")
url=input("Enter url : ")
main(url)

