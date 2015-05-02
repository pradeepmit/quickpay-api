import urllib2
import urllib
import hashlib
import xmltodict
import logging

class Api():
    def __init__(self,secret,api_key):
        self.API_URI="https://secure.quickpay.dk/api/"
        self.protocol='7'
        self.secret=secret
        self.api_key=api_key
        self.headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/xml",
            }
		
    def capture(self,merchant,amount,finalize,transaction):
        "This Method is used to capture "
        msg_type='capture'
        md5check_sum_capture= str(hashlib.md5(self.protocol+msg_type+merchant+amount+transaction+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'secret':self.secret,
                'api_key':self.api_key,
                'msgtype':msg_type,
                'merchant': merchant,
                'amount':amount,
                'transaction':transaction,
                'md5check': str(md5check_sum_capture),
                })
        response=self.get_request(params)
        return response	
	
    def authorize(self,merchant,ordernumber,amount,currency,autocapture,cardnumber,expirationdate,cvd):
        "This Method is used to authorize "
        msg_type='authorize'
        md5check_sum_authorize= str(hashlib.md5(self.protocol+msg_type+merchant+ordernumber+amount+currency+autocapture+cardnumber+expirationdate+cvd+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'secret':self.secret,
                'api_key':self.api_key,
                'msgtype':msg_type,
                'merchant': merchant,
                'ordernumber':ordernumber,
                'amount':amount,
                'currency':currency,
                'autocapture':autocapture,
                'cardnumber':cardnumber,
                'expirationdate':expirationdate,
                'cvd':cvd,
                'md5check': str(md5check_sum_authorize),
                })
        response=self.get_request(params)
        return response	
	
    def subscribe(self,merchant,ordernumber,amount,currency,cardnumber,expirationdate,cvd,description):
        "This Method is used to subscribe "
        msg_type='subscribe'
        md5check_sum_subscribe= str(hashlib.md5(self.protocol+msg_type+merchant+ordernumber+amount+currency+cardnumber+expirationdate+cvd+description+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'secret':self.secret,
                'api_key':self.api_key,
                'msgtype':msg_type,
                'merchant': merchant,
                'ordernumber':ordernumber,
                'amount':amount,
                'currency':currency,
                'cardnumber':cardnumber,
                'expirationdate':expirationdate,
                'cvd':cvd,
                'description':description,
                'md5check': str(md5check_sum_subscribe),
                })
        response=self.get_request(params)
        return response	
	
    def recurring(self,merchant,ordernumber,amount,currency,autocapture,transaction):
        "This Method is used to recurring "
        msg_type='recurring'
        md5check_sum_recurring= str(hashlib.md5(self.protocol+msg_type+merchant+ordernumber+amount+currency+autocapture+transaction+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'secret':self.secret,
                'api_key':self.api_key,
                'msgtype':msg_type,
                'merchant': merchant,
                'ordernumber':ordernumber,
                'amount':amount,
                'currency':currency,
                'autocapture':autocapture,
                'transaction':transaction,
                'md5check': str(md5check_sum_recurring),
                })
        response=self.get_request(params)
        return response	
	
	
    def cancel(self,merchant,transaction):
        "This Method is used to cancel "
        msg_type='cancel'
        md5check_sum_cancel= str(hashlib.md5(self.protocol+msg_type+merchant+transaction+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'msgtype':msg_type,
                'merchant': merchant,
                'transaction':transaction,
                'secret':self.secret,
                'api_key':self.api_key,
                'md5check': str(md5check_sum_cancel),
                })
        response=self.get_request(params)
        return response
	
    def refund(self,merchant,amount,transaction):
        "This Method is used to refund "
        msg_type='refund'
        md5check_sum_refund= str(hashlib.md5(self.protocol+msg_type+merchant+amount+transaction+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'msgtype':msg_type,
                'merchant': merchant,
                'amount':amount,
                'transaction':transaction,
                'secret':self.secret,
                'api_key':self.api_key,
                'md5check': str(md5check_sum_refund),
                 })
        response=self.get_request(params)
        return response
	
    def renew(self,merchant,transaction):
        "This Method is used to renew "
        msg_type='renew'
        md5check_sum_renew= str(hashlib.md5(self.protocol+msg_type+merchant+transaction+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'msgtype':msg_type,
                'merchant': merchant,
                'transaction':transaction,
                'secret':self.secret,
                'api_key':self.api_key,
                'md5check': str(md5check_sum_renew),
              })
        response=self.get_request(params)
        return response
	
    def status(self,merchant,transaction):
        "This Method is used to status "
        msg_type='status'
        md5check_sum_status= str(hashlib.md5(self.protocol+msg_type+merchant+transaction+self.secret).hexdigest())
        params = urllib.urlencode({
                'protocol':self.protocol,
                'secret':self.secret,
                'api_key':self.api_key,
                'msgtype':msg_type,
                'merchant': merchant,
                'transaction':transaction,
                'md5check': str(md5check_sum_status),
                })
        response=self.get_request(params)
        return response
	
    def get_request(self,params):
            req = urllib2.Request(self.API_URI, params, self.headers)
            try:
                response = urllib2.urlopen(req)
                the_page = response.read()
                d = dict(xmltodict.parse(str(the_page))['response'])
                return d
            except urllib2.HTTPError, e:
                raise IOError('Got the error during processing the HTTP request. error message : %s , error code : %s' %(str(e.msg), str(e.code)))
            except urllib2.URLError, e:
                raise IOError('It seems like the Input URL is wrong. error code : ' + str(e.reason.errno))
			
			
			
			
	
		
