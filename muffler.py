import hpilo

ilo = hpilo.Ilo(host,username,password,hpilo.ILO_HTTP)
health = ilo.get_embedded_health()
print(health['temperature'])
