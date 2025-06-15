import aiohttp
import asyncio
from bs4 import BeautifulSoup
import builtwith
import requests
import socket
from urllib.parse import urljoin, urlparse
from datetime import datetime
import urllib.parse
import json

async def fetch_waf(url):
    try:
        result = await asyncio.create_subprocess_exec(
            'wafw00f', url,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await result.communicate()
        waf_detected = 'No WAF detected' if 'No WAF detected' in stdout.decode() else 'WAF detected'
        return waf_detected
    except Exception as e:
        return f'Error detecting WAF: {str(e)}'

def format_technologies(tech_info):
    try:
        if isinstance(tech_info, dict):
            res = "Technology Used: "
            for category, technologies in tech_info.items():
                res += f"\n{category.replace('-', ' ').title()}: "
                res += ", ".join(technologies)
            return res
        else:
            return f"Error: Invalid technology info format."
    except Exception as e:
        return f"Error formatting technologies: {str(e)}"

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        return f"Error fetching URL: {str(e)}"

async def scan_website(url):
    async with aiohttp.ClientSession() as session:
        try:
            start_time = datetime.now()
            html = await fetch(session, url)
            end_time = datetime.now()
            load_time = (end_time - start_time).total_seconds()

            soup = BeautifulSoup(html, 'html.parser')
            title = soup.title.string if soup.title else "N/A"
            description_tag = soup.find('meta', attrs={"name": "description"})
            description = description_tag['content'] if description_tag else "N/A"
        except Exception as e:
            return {"error": f"Error scanning website: {str(e)}"}

        try:
            tech_info = builtwith.parse(url)
        except Exception as e:
            tech_info = f"Error parsing technologies: {str(e)}"

        waf_info = await fetch_waf(url)

        urls = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]

        try:
            parsed_link = urllib.parse.urlparse(url)
            domain = parsed_link.netloc if parsed_link.scheme else url
            ip = socket.gethostbyname(domain)

            geoLocApiKey = "fe1aca39f5e94b60b71e1b4d51c12326"
            geolocation_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={geoLocApiKey}&ip={ip}"
            
            geo_response = requests.get(geolocation_url)
            geo_data = geo_response.json()

        except Exception as e:
            return {"error": f"Error fetching geolocation and proxy info: {str(e)}"}

        try:
            server_response = requests.head(url)
            server_info = server_response.headers.get('Server', 'No server info found')
        except Exception as e:
            server_info = f"Error fetching server info: {str(e)}"
        
        data = {
            "title": title,
            "description": description,
            "server": server_info,
            "ip": ip,
            "country": geo_data.get('country_name', 'N/A'),
            "region": geo_data.get('state_prov', 'N/A'),
            "isp": geo_data.get('isp', 'N/A'),
            "organization": geo_data.get('organization', 'N/A'),
            "technologies": format_technologies(tech_info),
            "waf_info": waf_info,
            "urls": urls,
            "load_time": load_time
        }
        return json.dumps(data, indent=4)
        