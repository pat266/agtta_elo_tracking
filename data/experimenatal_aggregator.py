import http.client

conn = http.client.HTTPSConnection("www.tabletennisleague.com")
payload = ''
headers = {}
conn.request("GET", "/AGTTA/SessionGroupReportArchive/SessionGroupReport2024July16.HTM", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))