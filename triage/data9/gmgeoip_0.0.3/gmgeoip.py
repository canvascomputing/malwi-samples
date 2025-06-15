import os
import socket
import json
import geoip2.database
from .IP2Location import IP2Location

class GmGeoip:
    
    def __init__(self):
        self.GEOIP_PATH = '/'
        self.geoip2 = True
        self.is_lite = False
        
    def reader(self, geoip2=True, is_lite=False, path='/'):
        """
        Set Geoip Reader feed
        """
        self.is_lite = is_lite
        self.geoIp2 = geoip2
        self.geoType = 'GeoLite2' if is_lite else 'GeoIP2'
        
        if self.geoIp2:
            self.GEOIP_COUNTRY = '%s/GeoLite2-Country.mmdb'%(path) if self.is_lite  else  '%s/GeoIP2-Country.mmdb'%(path) 
            self.GEOIP_CITY = '%s/GeoLite2-City.mmdb'%(path) if self.is_lite  else '%s/GeoIP2-City.mmdb'%(path)
            self.GEOIP_ASN = '%s/GeoLite2-ASN.mmdb'%(path)  
            self.GEOIP_ISP = '%s/GeoIP2-ISP.mmdb'%(path)
            
        else:
            self.ip2locationv4_all = '%s/IP-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE.BIN'%(path)
            self.ip2locationv6_all = '%s/IPV6-COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE.BIN'%(path)
            self.ip2locationv4_isp = '%s/IP-COUNTRY-ISP.BIN'%(path)
            self.ip2locationv6_isp = '%s/IPV6-COUNTRY-ISP.BIN'%(path)
    
    def parse_addr(self, addr): 
        """ Parses address and returns IP version. Raises exception on invalid argument """
        ipv = 0
        try:
            socket.inet_pton(socket.AF_INET6, addr)
            # Convert ::FFFF:x.y.z.y to IPv4
            if addr.lower().startswith('::ffff:'):
                try:
                    socket.inet_pton(socket.AF_INET, addr)
                    ipv = 4
                except:
                    ipv = 6
            else:
                ipv = 6
        except:
            try:
                socket.inet_pton(socket.AF_INET, addr)
                ipv = 4
            except:
                return 0
        return ipv
        
    def get_ip_info(self, ipaddr):
        if self.geoIp2:
            return self.get_ip_info_geoip2(ipaddr)
        else:
            return self.get_ip_info_ip2location(ipaddr)
    
    def get_ip_info_geoip2(self, ipaddr):
        response = {}
        
        try:
            reader_city = geoip2.database.Reader(self.GEOIP_CITY)
            
            response_city = reader_city.city(ipaddr)
            response['cc'] = response_city.country.iso_code
            response['country_name'] = response_city.country.name
            response['city'] = response_city.city.name
            response['zip'] = response_city.postal.code
            response['stat_name']= response_city.subdivisions.most_specific.name
            response['stat']= response_city.subdivisions.most_specific.iso_code
            
            if self.is_lite:
                reader_asn = geoip2.database.Reader(self.GEOIP_ASN)
                response_asn = reader_asn.asn(ipaddr)
                response['isp'] = None
                response['organization'] = response_asn.autonomous_system_organization    
                response['autonomous_system_number'] = response_asn.autonomous_system_number
            else:
                reader_isp = geoip2.database.Reader(self.GEOIP_ISP)
                response_isp = reader_isp.isp(ipaddr)
                response['isp'] = response_isp.isp 
                response['organization'] = response_isp.organization    
                response['autonomous_system_number'] = response_isp.autonomous_system_number  
            
            response["status"]= True
            
        except Exception as e:
            response["status"]= False
            response["message"] = "Exception: %s"%(e)
                
        return response
    
    def get_ip_info_ip2location(self, ipaddr):
        
        response = {}
        dirpath = os.getcwd()

        try:
            reg_file = open('%s/gmgeoip/region_codes.json'%(dirpath))
            region_codes = json.load(reg_file)
            ipv = self.parse_addr(ipaddr)
            if ipv == 6:
                
                """ Getting ISP detail """
                geo_readerv6_isp = IP2Location(self.ip2locationv6_isp)
                rec = geo_readerv6_isp.get_all(ipaddr)
                response['isp'] = rec.isp.decode('utf-8','ignore')
                
                
                
                """ Getting COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE detail """
                geo_readerv6_all = IP2Location(self.ip2locationv6_all)
                rec = geo_readerv6_all.get_all(ipaddr)
                response['city']     = rec.city.decode('utf-8','ignore')
                response['cc']     = rec.country_short.decode('utf-8','ignore')
                response['zip']    = rec.zipcode.decode('utf-8','ignore')
                response['country_name']    = rec.country_long.decode('utf-8','ignore')
                try:
                    response['stat'] = region_codes[response['cc']][rec.region.decode('utf-8','ignore')]
                except:
                    response['stat'] = rec.region.decode('utf-8','ignore')
                    
            elif ipv == 4:
                """ Getting ISP detail """
                geo_readerv4_isp = IP2Location(self.ip2locationv4_isp)
                rec = geo_readerv4_isp.get_all(ipaddr)
                response['isp'] = rec.isp.decode('utf-8','ignore')
                
                """ Getting COUNTRY-REGION-CITY-LATITUDE-LONGITUDE-ZIPCODE detail """
                geo_readerv4_all = IP2Location(self.ip2locationv4_all)
                rec = geo_readerv4_all.get_all(ipaddr)
                response['city']     = rec.city.decode('utf-8','ignore')
                response['cc']     = rec.country_short.decode('utf-8','ignore')
                response['zip']    = rec.zipcode.decode('utf-8','ignore')
                response['country_name']    = rec.country_long.decode('utf-8','ignore')

                try:
                    response['stat'] = region_codes[response['cc']][rec.region.decode('utf-8','ignore')]
                except:
                    response['stat'] = rec.region.decode('utf-8','ignore')
    
            else:   
                return {"status":False ,"Exception: invalid ipaddr": "%s"%(ipadd) }
            
            response["status"] = True
            
        except Exception as e:
            response["status"] = False
            response["message"] = "Exception: %s"%(e)
          
        return response