import pickle

headers=pickle.load(open('/Users/yoavfreund/.Vault/Decibel.pkl','r'))

applicationID = headers['DecibelAppID']
applicationKey = headers['DecibelAppKey']
apiAddress = 'http://decibel-rest-jazz.cloudapp.net/v1/'

print applicationID,applicationKey
