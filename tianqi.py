    # -*- coding: utf-8 -*-  
    import os  
    import urllib  
      
    #����url�õ�html����  
    def getHtml(url):  
        page = urllib.urlopen(url)  
        html = page.read()  
        return html  
      
    #���ַ����ָ������Ϊ��źͶ�Ӧ���е�dictionary  
    def getDictionary(str):  
        str_split = str.split(',')  
        dics = {}  
        for each in str_split:  
            tmp = each.split('|')  
            dics[tmp[0]] = tmp[1]  
        return dics  
      
    #�õ���źͶ�Ӧ��ʡ��ֱϽ��dictionary  
    def getProvience(url):  
        res = getHtml(url)  
        pro_dic = getDictionary(res)  
        return pro_dic  
      
    #�õ���źͶ�Ӧ�Ķ������е�dictionary  
    def getCity(url):  
        res = getHtml(url)  
        city_dic = getDictionary(res)  
        return city_dic  
      
    #�õ���źͶ�Ӧ�������dictionary  
    def getField(url):  
        res = getHtml(url)  
        field_dic = getDictionary(res)  
        return field_dic  
      
    if __name__ == '__main__':  
        #���ļ�  
        city_code_file = open('city.py', 'w')  
        city_code_file.write('# -*- coding: utf-8 -*-\n')  
        city_code_file.write('city = {}\n')  
        print '��ȡʡ�Լ�ֱϽ�б��'  
        province_url = 'http://m.weather.com.cn/data5/city.xml'  
        pro_dic = getProvience(province_url)  
        #��ȡÿ��ʡ�ĳ��б��  
        print '��ȡ����������'  
        for pro in pro_dic:  
            city_url = 'http://m.weather.com.cn/data5/city' + pro + '.xml'  
            city_dic = getCity(city_url)  
            #��ȡÿ�����еĵ������  
            for city in city_dic:  
                field_url = 'http://m.weather.com.cn/data5/city' + city + '.xml'  
                field_dic = getField(field_url)  
                #����ÿһ����źͶ�Ӧ�ĵ�������dictionary  
                for field in field_dic:  
                    city_code_file.write('city[\'' + field_dic[field] + '\'] = ' + '101' + str(field) + '\n')   
                    print 'city[\'' + field_dic[field].decode('utf-8') + '\'] = ' + '101' + str(field)  
        #�ر��ļ�  
        city_code_file.close()  
        print '��ȡ���'  